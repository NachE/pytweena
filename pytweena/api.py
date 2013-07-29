# Tweepy
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import json
from pytweena.auth import PytweenaAuth

class PytweenaAPI():

	apibaseurl="http://api.twitter.com/1.1/"
	response = ""
	data = ""
	jsondata = ""

	def auth(self, consumer_key, consumer_secret, access_token, access_token_secret):
		self.client = PytweenaAuth.login(consumer_key, consumer_secret, access_token, access_token_secret)

	def req_GET(self,resource):

		ret = self.client.request(self.apibaseurl+resource+".json")
		self.response, self.data = ret
		self.jsondata = json.loads(self.data)
		return ret

	#Timelines

	def mentions_timeline(self):
		return self.req_GET('statuses/mentions_timeline')

	def user_timeline(self):
		return self.req_GET('statuses/user_timeline')

	def home_timeline(self):
		return self.req_GET('statuses/home_timeline')

	def retweets_of_me(self):
		return self.req_GET('statuses/retweets_of_me')
		
