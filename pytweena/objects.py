# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

# Twitter doc:
# https://dev.twitter.com/docs/platform-objects


#General object
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

# https://dev.twitter.com/docs/platform-objects/users
class UsersObject(PytweenaObject):
	pass

# https://dev.twitter.com/docs/platform-objects/tweets
class TweetsObject(PytweenaObject):

	#TODO: Object?
	#https://dev.twitter.com/docs/platform-objects/tweets#obj-contributors
	contributors = {}

	#TODO: Object?
	#https://dev.twitter.com/docs/platform-objects/tweets#obj-coordinates 
	coordinates = {}
 
	created_at = str()
	current_user_retweet = {}
	entities = EntitiesObject()
	favorite_count = int()
	favorited = bool()
	filter_level = str()
	geo = {} #DEPRECATED
	id = long() #int64 signed Can be Null
	id_str = str()
	in_reply_to_screen_name = str()
	in_reply_to_status_id = long() #int64 Can be Null
	in_reply_to_status_id_str = str()
	in_reply_to_user_id = long() #int64
	in_reply_to_user_id_str = str()
	lang = str()
	place = {} # Places Obj https://dev.twitter.com/docs/platform-objects/places
	possibly_sensitive = bool()
	scopes = {}
	retweet_count = int()
	retweeted = bool()
	source = str()
	text = str()
	truncated = bool()
	user = UsersObject()
	withheld_copyright = bool()
	withheld_in_countries = []
	withheld_scope = str()

	def build_object():
		self.contributors = self.jsondata['contributors'] #TODO: Convert into Object?
		self.coordinates = self.jsondata['coordinates'] # TODO: Object?
		self.created_at = str(self.jsondata['created_at'])
		self.current_user_retweet = self.jsondata['current_user_retweet']
		self.entities.load(self.jsondata['entities'])
		self.favorite_count = int(self.jsondata['favorite_count'])
		self.favorited = bool(self.jsondata['favorited']) or None #Bug? keep waching
		self.filter_level = str(self.jsondata['filter_level'])
		self.geo = self.jsondata['geo'] #DEPRECATED
		self.id = long(self.jsondata['id']) # or None?
		self.id_str = str(self.jsondata['id_str'])
		self.in_reply_to_screen_name = self.jsondata['in_reply_to_screen_name']
		self.in_reply_to_status_id = long(self.jsondata['in_reply_to_status_id'])#or None?
		self.in_reply_to_status_id_str = str(self.jsondata['in_reply_to_status_id_str'])
		self.in_reply_to_user_id = long(self.jsondata['in_reply_to_user_id'])#or None?
		self.in_reply_to_user_id_str = str(self.jsondata['in_reply_to_user_id_str'])
		self.lang = str(self.jsondata['lang'])
		self.place.load(self.jsondata['place']) #It can be Null, so be carefully
		self.possibly_sensitive = bool(self.jsondata['possibly_sensitive'])#Or None?
		self.scopes = self.jsondata['scopes']
		self.retweet_count = int(self.jsondata['retweet_count'])
		self.retweeted = bool(self.jsondata['retweeted'])
		self.source = str(self.jsondata['source'])
		self.text = str(self.jsondata['text'])
		self.truncated = bool(self.jsondata['truncated'])
		self.user.load(self.jsondata['user'])
		self.withheld_copyright = bool(self.jsondata['withheld_copyright'])
		self.withheld_in_countries = self.jsondata['withheld_in_countries']
		self.withheld_scope = str(self.jsondata['withheld_scope'])


class EntitiesObject(PytweenaObject):
	# https://dev.twitter.com/docs/platform-objects/entities
	pass

class PlacesObject(PytweenaObject):
	# https://dev.twitter.com/docs/platform-objects/places
	pass
