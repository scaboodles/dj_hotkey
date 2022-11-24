#!/usr/bin/env python3
import requests
import json
import base64

CLIENT_CALLBACK_URL  = 'http://localhost:8888/callback'
auth_encoded = 
AUTH_HEADER = "Basic " + auth_encoded
SPOTIFY_ACCOUNTS_ENDPOINT = "https://accounts.spotify.com/api/token"
REFRESH_TOKEN = 
refreshParams = {"grant_type" : "refresh_token"}
refreshParams["refresh_token"] = REFRESH_TOKEN

refreshHeaders = {"Content-Type":"application/x-www-form-urlencoded"}
refreshHeaders["Accept"] = "application/json"
refreshHeaders["Authorization"] = AUTH_HEADER

def refreshAuthorization():
    resp = requests.post(SPOTIFY_ACCOUNTS_ENDPOINT, params=refreshParams, headers=refreshHeaders)
    token = parseToken(json.dumps(resp.json()))
    return token

def parseToken(jsonOb):
    return json.loads(jsonOb).get("access_token")