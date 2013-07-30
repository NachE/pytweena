#!/usr/bin/env python

#Import pytweena lib
import pytweena

#Set the keys and tokens
consumerkey = ""
consumersecret = ""
accesstoken = ""
accesstokensecret = ""

#Get the api
myapi = pytweena.api

#Auth the api
myapi.auth(consumerkey, consumersecret, accesstoken, accesstokensecret)

#Get latest 10 twits from timeline
myapi.home_timeline({'count': 10})
for tweet in myapi.jsondata:
    print tweet['text']

#Send a tweet
myapi.update({'status': 'Hi!, im an app with pytweena lib!'})
