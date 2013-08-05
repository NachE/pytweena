#!/usr/bin/env python

#Import pytweena lib
import pytweena

#Set the keys and tokens
consumerkey = ""
consumersecret = ""
accesstoken = ""
accesstokensecret = ""

#Get the api
myapi = pytweena.PytweenaEasy()

#Auth the api
myapi.auth(consumerkey, consumersecret, accesstoken, accesstokensecret)

#make a consult GET statuses/home_timeline
tweets = myapi.statuses_home_timeline({'count': 5})

#tweets is a TweetsObject, can be iterated
for tweet in tweets:
	print tweet.user.name
	print tweet.text
	print "****\n"
print "No more tweets in a for iteration\n\n\n"


# put cursor at the first (-1)
# You always use .netx() before
# .current()
tweets.resetcursor()

#Tweets can be access manually
try:
	print tweets.next().user.name
	print tweets.current().text + "\n\n"

	print tweets.next().user.name
	print tweets.current().text + "\n\n"
except StopIteration:
	print "\nNo more tweets in a manual way\n\n\n"

print "\nEnd of manual way\n\n\n"



tweets.resetcursor()


# You also can use while
while True:
	try:
		print tweets.next().user.name
		print tweets.current().text + "\n\n"
	except StopIteration:
		print "\nNo more tweets in a while"
		break
		




