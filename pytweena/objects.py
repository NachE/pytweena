# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

# Twitter doc:
# https://dev.twitter.com/docs/platform-objects

class PytweenaObject:
	def json_load (self, jsondata):
		pass


class UsersObject(PytweenaObject):
	# https://dev.twitter.com/docs/platform-objects/users
	pass

class TweetsObject(PytweenaObject):
	# https://dev.twitter.com/docs/platform-objects/tweets
	contributors = {}
	coordinates = {}
	created_at = str()
	current_user_retweet = {}
	entities = EntitiesObject()
	favorite_count = int()
	favorited = bool()
	filter_level = str()
	geo = {} #DEPRECATED
	id = long() #int64 signed
	id_str = str()
	in_reply_to_screen_name = str()
	in_reply_to_status_id
	in_reply_to_status_id_str
	in_reply_to_user_id
	in_reply_to_user_id_str
	lang
	place
	possibly_sensitive
	scopes
	retweet_count
	retweeted
	source
	text
	truncated
	user
	withheld_copyright
	withheld_in_countries
	withheld_scope	

class EntitiesObject(PytweenaObject):
	# https://dev.twitter.com/docs/platform-objects/entities
	pass

class PlacesObject(PytweenaObject):
	# https://dev.twitter.com/docs/platform-objects/places
	pass






