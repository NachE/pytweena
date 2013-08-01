# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.


# Twitter doc:
# https://dev.twitter.com/docs/platform-objects

# TODO: bool('true') and bool('false') are True
# Bug? json.loads() should return False when 'false'
# and True when 'true'. Keep watching

# TODO: Keep watching Objects like
# contributors or Sizes (Entities)
# Need classes?
# For now, it are represented by {}

#from pytweena.objects import EntitiesObject, UsersObject, TweetsObject, PlacesObject, PytweenaObject

#General object
#class PytweenaObject(object):
class PytweenaObject:

	jsondata = {}

	def __init__(self, jsondata = {}):
		if len(jsondata) > 0:
			self.load(jsondata)

	def load (self, jsondata):
		self.jsondata = jsondata
		self.build_object()

	def build_object():
		pass
		# This method is defined
		# on each specific object
		# (UsersObject, TweetObject, etc)
