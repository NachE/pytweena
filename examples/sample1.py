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


########################################
print ("\n\n\nGet latest 10 tweets from timeline")
myapi.statuses_home_timeline({'count': 10})
for tweet in myapi.jsondata:
	print tweet['text']
########################################



########################################
print ("\n\n\nGet tweet by id")
myapi.statuses_show({'id':8062317551})
print myapi.jsondata['text']
#######################################



##########################################
print ("\n\n\nSearch 'my search string', show only 10")
myapi.search_tweets({'q': 'my search string','count': 10})
for tweet in myapi.jsondata['statuses']:
	print tweet['text']
##########################################



###########################################
print("\n\n\nSend a tweet")
myapi.statuses_update({'status': 'Hi!, im an app with pytweena lib!'})
###########################################
