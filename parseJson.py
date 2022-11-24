#!/usr/bin/env python3
import json

def getReturnedItems(respDict):
    dict = json.loads(respDict)
    items = dict.get("tracks").get("items")
    return items

def getUriSongOnly(songName, items):
    for i in range(len(items)):
        if items[i].get("name").lower() == songName.lower():
            printArtists(items[i])
            return items[i].get("uri")

def getUriFullSearch(songName, artist, items):
    for i in range(len(items)):
        if items[i].get("name").lower() == songName.lower():
            for j in range(len(items[i].get("artists"))):
                if(items[i].get("artists")[j].get("name").lower() == artist.lower()):
                    printArtists(items[i])
                    return items[i].get("uri")

def printArtists(track):
    artistsStr = ""
    artistsLst = track.get("artists")
    if(len(artistsLst) > 1):
        for i in range(len(artistsLst)):
            if(i == len(artistsLst) - 1):
                artistsStr = artistsStr + artistsLst[i].get("name")
            elif(i == len(artistsLst) - 2):
                artistsStr = artistsStr + artistsLst[i].get("name") + ", and "
            else:
                artistsStr = artistsStr + artistsLst[i].get("name") + ", "
    else:
        artistsStr = artistsStr + artistsLst[0].get("name")
    print(artistsStr + "|")


def getSongUri(song, respDict, songOnly, artist):
    tracks = getReturnedItems(respDict)
    if(songOnly):
        return getUriSongOnly(song, tracks)
    else:
        return getUriFullSearch(song, artist, tracks)

def testUriFetch():
    f = open('httpResponse.json')
    data = f.read()
    f.close()
    print(getSongUri("zoloft", data, True, "unknown"))

def testVisualParse():
    f = open('httpResponse.json')
    data = f.read()
    data = json.loads(data)
    f.close()
    printAllElements(data)

def checkList(ele, prefix):
    for i in range(len(ele)):
        if (isinstance(ele[i], list)):
            checkList(ele[i], prefix+"["+str(i)+"]")
        elif (isinstance(ele[i], str)):
            printField(ele[i], prefix+"["+str(i)+"]")
        else:
            checkDict(ele[i], prefix+"["+str(i)+"]")

def checkDict(jsonObject, prefix):
    for ele in jsonObject:
        if (isinstance(jsonObject[ele], dict)):
            checkDict(jsonObject[ele], prefix+"."+ele)

        elif (isinstance(jsonObject[ele], list)):
            checkList(jsonObject[ele], prefix+"."+ele)

        elif (isinstance(jsonObject[ele], str)):
            printField(jsonObject[ele],  prefix+"."+ele)

def printField(ele, prefix):
    print (prefix, ":" , ele)


#Iterating all the fields of the JSON
def printAllElements(data):
    for element in data:
    #If Json Field value is a Nested Json
        if (isinstance(data[element], dict)):
            checkDict(data[element], element)
        #If Json Field value is a list
        elif (isinstance(data[element], list)):
            checkList(data[element], element)
        #If Json Field value is a string
        elif (isinstance(data[element], str)):
            printField(data[element], element)