#!/usr/bin/env python3
import requests
import json

SEARCH_PLAYLIST_ENDPOINT ='https://api.spotify.com/v1/search?type=track'
PLAYBACK_ENDPOINT = 'https://api.spotify.com/v1/me/player/queue'

def searchForTrack(query, token): #returns a dictionary of responses
    searchParams = {'type': 'track'}
    searchParams['q'] = query
    searchParams['market'] = 'US'
    searchParams['limit'] = 50
    myheaders = {"Accept":"application/json"}
    myheaders["Content-Type"] = "application/json"
    myheaders["Authorization"] = "Bearer " + token
    resp = requests.get(SEARCH_PLAYLIST_ENDPOINT, params=searchParams, headers=myheaders)
    #writeToFile(json.dumps(resp.json()))
    return json.dumps(resp.json())

def doTheThing(uri, token):
    myheaders = {"Accept":"application/json"}
    myheaders["Content-Type"] = "application/json"
    myheaders["Authorization"] = "Bearer " + token
    searchParams = {'uri':uri}
    resp = requests.post(PLAYBACK_ENDPOINT, params=searchParams, headers=myheaders)
    return resp

def testQueue():
    doTheThing('spotify:track:3okk47CKOqAm1TXmVPzNYf')

def testSearch():
    testQ = "Something About Us Daft Punk"
    tok = 'BQArMtuw7RqCYEOG4ZIO2EnsQJV9_l8gpWl9CTWeQTB9ClYc5VDasCf7Kag_kODpCK3s1OoXXIePzJ15WjyVyPmKLlQtuy_vRHt2dpObg35AijY-N77yj71nuP7Y3eDTvLpAy20vA8zCzDMAOYR2LHF6EAOWygx_GBwpGMJRUD7N1zDM3wSXIpAGmP4'
    log = open('testLog.txt', 'w')
    response = searchForTrack(testQ, tok)
    log.close()
    print(response)

def writeToFile(dict):
    f = open('httpResponse.json', 'w')
    f.write(dict)
    f.close()