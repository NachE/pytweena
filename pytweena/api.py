# Tweepy
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import json, urllib
from pytweena.auth import PytweenaAuth

class PytweenaAPI():

	apibaseurl="http://api.twitter.com/1.1/"
	response = ""
	data = ""
	jsondata = ""

	def auth(self, consumer_key, consumer_secret, access_token, access_token_secret):
		self.client = PytweenaAuth.login(consumer_key, consumer_secret, access_token, access_token_secret)

	def req_GET(self, resource, parameters = {}):
		if len(parameters) > 0:
			options = "?"+urllib.urlencode(parameters)
		else:
			options = ""
		self.response, self.data = self.client.request(self.apibaseurl+resource+".json"+options)
		self.jsondata = json.loads(self.data)
		return [self.response, self.data]

	#Timelines

	def mentions_timeline(self, parameters = {}):
		return self.req_GET('statuses/mentions_timeline', parameters)

	def user_timeline(self, parameters = {}):
		return self.req_GET('statuses/user_timeline', parameters)

	def home_timeline(self, parameters = {}):
		return self.req_GET('statuses/home_timeline', parameters)

	def retweets_of_me(self, parameters = {}):
		return self.req_GET('statuses/retweets_of_me', parameters)
		
