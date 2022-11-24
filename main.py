#!/usr/bin/env python3
import argparse
from strings_mod import formatSearch, plainText
from query import searchForTrack, doTheThing
from parseJson import getSongUri
from auto_auth.refresh import refreshAuthorization

def main():
    try:
        parser = argparse.ArgumentParser(description='input file path')
        parser.add_argument('in_path', help='path to tmp input file')
        args = parser.parse_args()
        f = open(args.in_path)
        song_artist = f.read()
        f.close()

        token = refreshAuthorization()
        query = None
        artist = None
        songName = None
        songOnly = False

        if(',' in song_artist):
            deliminated = song_artist.split(',')

            deliminated[0] = plainText(deliminated[0])
            deliminated[1] = plainText(deliminated[1])

            songName = deliminated[0]
            artist = deliminated[1]

            query = " ".join(deliminated)
        else:
            songOnly = True
            query = plainText(song_artist)
            songName = query
            
        print(songName + "|")

        resp_dict = searchForTrack(query, token)
        targetUri = getSongUri(songName, resp_dict, songOnly, artist)

        queueRequest = doTheThing(targetUri, token)

        print(queueRequest.status_code)
    except Exception:
        print(Exception)

def writeTestFile(ob):
    f = open('testLog.txt', 'a')
    f.write(ob)
    f.write('\n')
    f.close()

main()