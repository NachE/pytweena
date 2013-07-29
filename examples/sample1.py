#!/usr/bin/env python

#Import the pytweena lib
import pytweena

#Set the keys and tokens
consumerkey = ""
consumersecret = ""
accesstoken = ""
accesstokensecret = ""

#Get the api
myapi = pytweena.api

#Auth
myapi.auth(consumerkey, consumersecret, accesstoken, accesstokensecret)

#Run home_timeline
myapi.home_timeline()

#foreach json response
for tweet in myapi.jsondata:
    print tweet['text']
