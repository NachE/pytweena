# Tweepy
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import json, urllib
from pytweena.auth import PytweenaAuth

class PytweenaAPI():

	apibaseurl="https://api.twitter.com/1.1/"
	response = ""
	data = ""
	jsondata = ""

	def auth(self, consumer_key, consumer_secret, access_token, access_token_secret):
		self.client = PytweenaAuth.login(consumer_key, consumer_secret, access_token, access_token_secret)

	def req_POST(self, resource, parameters = {}):
		return self.req_resource(resource, "POST", parameters)

	def req_GET(self, resource, parameters = {}):
		return self.req_resource(resource, "GET", parameters)

	def req_resource(self, resource, http_method, parameters = {}):
		if len(parameters) > 0:
			if http_method == "GET":
				options = "?"+urllib.urlencode(parameters)
				post_data = ""
			elif http_method == "POST":
				post_data = urllib.urlencode(parameters)
				options = ""
		else:
			options = ""
			post_data = ""

		self.response, self.data = self.client.request(
			self.apibaseurl+resource+".json"+options, 
			method=http_method,
			body = post_data 
		)

		self.jsondata = json.loads(self.data)
		return [self.response, self.data]


	# Timelines
	# =========

	def mentions_timeline(self, parameters = {}):
		return self.req_GET('statuses/mentions_timeline', parameters)

	def user_timeline(self, parameters = {}):
		return self.req_GET('statuses/user_timeline', parameters)

	def home_timeline(self, parameters = {}):
		return self.req_GET('statuses/home_timeline', parameters)

	def retweets_of_me(self, parameters = {}):
		return self.req_GET('statuses/retweets_of_me', parameters)


	# Tweets
	# ======

	def retweets(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_GET('statuses/retweets/'+id, parameters)

	def show(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_GET('statuses/show/'+id, parameters)

	def destroy(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_POST('statuses/destroy/'+id, parameters)

	def update(self, parameters = {}):
		return self.req_POST('statuses/update', parameters)

	def retweet(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_POST('statuses/retweet/'+id, parameters)

	#TODO: see later, media[] need raw image bytes
	def update_with_media(self, parameters = {}):
		return self.req_POST('statuses/update_with_media', parameters)

	def oembed(self, parameters = {}):
		return self.req_GET('statuses/oembed', parameters)

	def retweeters_ids(self, parameters = {}):
		return self.req_GET('statuses/retweeters/ids', parameters)


	# Search
	# ======

	def search_tweets(self, parameters = {}):
		return self.req_GET('search/tweets', parameters)







