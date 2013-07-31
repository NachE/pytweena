#!/usr/bin/env python

#Import pytweena lib
import pytweena
#Import Pretty Printer
import pprint

#configure Pretty Printer
pp = pprint.PrettyPrinter(indent=4)


#Set the keys and tokens
consumerkey = ""
consumersecret = ""
accesstoken = ""
accesstokensecret = ""

#Get the api
myapi = pytweena.api

#Auth the api
myapi.auth(consumerkey, consumersecret, accesstoken, accesstokensecret)


print ("\n\n\nGet latest 10 tweets from timeline")
myapi.statuses_home_timeline({'count': 10})
for tweet in myapi.jsondata:
	print tweet['text']
	#print all json datas with pretty printer
	pp.pprint(tweet)
	


