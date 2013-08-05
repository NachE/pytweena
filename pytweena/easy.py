# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import json
from pytweena.api import PytweenaAPI
from pytweena.objects import *

class PytweenaEasy(PytweenaAPI):

# json.contributors = Tweet
# json[0].contributors = Tweet (json list of tweets)
# contributors_enabled = Users
# hashtags = Entities
# attributes = Places


	#def test(self):
	#	self.statuses_show({'id':8062317551})
	#	cosa = TweetsObject(self.jsondata)
	#	print cosa.text

	def build(self, req_resource):
		response, data = req_resource
		# check if Tweets, Places, Users, Entities
		# contributors = Tweets

		#if type() == list:	
		#	jsondata = json.loads(data)
		jsondata = json.loads(data)
		self.jsondata = jsondata

		# The next code is so ugly
		# TODO: make better code
		try:
			jsondata['contributors']
			return TweetObject(jsondata)
		except NameError:
			pass
		except TypeError:
			pass

		try:
			jsondata[0]['contributors']
			return TweetsObject(jsondata)
		except NameError:
			pass
		
		try:
			jsondata['contributors_enabled']
			return UsersObject(jsondata)
		except NameError:
			pass

		try:
			jsondata['hashtags']
			return UsersObject(jsondata)
		except NameError:
			pass

		try:
			jsondata['attributes']
			return PlacesObject(jsondata)
		except NameError:
			pass


	def req_POST(self, resource, parameters = {}):
		return self.build(self.req_resource(resource, "POST", parameters))

	def req_GET(self, resource, parameters = {}):
		return self.build(self.req_resource(resource, "GET", parameters))

