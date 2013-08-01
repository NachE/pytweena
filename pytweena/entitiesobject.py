# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

from pytweena.pytweenaobject import PytweenaObject


# https://dev.twitter.com/docs/platform-objects/entities
class EntitiesObject(PytweenaObject):

	hashtags = {} # Here is an array of objects
	media = {}    # Look if need clases for
	urls = {}     # these Objects
	user_mentions = {}

	def build_object():
		self.hashtags = self.jsondata['hashtags']
		self.media = self.jsondata['media']
		self.urls = self.jsondata['urls']
		self.user_mentions = self.jsondata['user_mentions']

