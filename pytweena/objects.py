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

	def build_object(self):
		pass
		# This method is defined 
		# on each specific object
		# (UsersObject, TweetObject, etc)


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


# https://dev.twitter.com/docs/platform-objects/places
class PlacesObject(PytweenaObject):
	attributes = {}
	bounding_box = {} #have coordinates[] and type str()
	country = str()
	country_code = str()
	full_name = str()
	id = str()
	name = str()
	place_type = str()
	url = str()

	def build_object(self):
		self.attributes = self.jsondata['attributes']
		self.bounding_box = self.jsondata['bounding_box']
		self.country = str(self.jsondata['country'])
		self.country_code = str(self.jsondata['country_code'])
		self.full_name = str(self.jsondata['full_name'])
		self.id = str(self.jsondata['id'])
		self.name = str(self.jsondata['name'])
		self.place_type = str(self.jsondata['place_type'])
		self.url = str(self.jsondata['url'])


# https://dev.twitter.com/docs/platform-objects/users
class UsersObject(PytweenaObject):
	
	contributors_enabled = bool()
	created_at = str()
	default_profile = bool()
	default_profile_image = bool()
	description = str()
	entities = None
	favourites_count = int()
	follow_request_sent = bool() # Doc say "Type"
	following = bool() # Doc say "Type" again
	followers_count = int()
	friends_count = int()
	geo_enabled = bool()
	id = long()
	id_str = str()
	is_translator = bool()
	lang = str()
	listed_count = int()
	location = str()
	name = str()
	notifications = bool()
	profile_background_color = str()
	profile_background_image_url = str()
	profile_background_image_url_https = str()
	profile_background_tile = bool()
	profile_banner_url = str()
	profile_image_url = str()
	profile_image_url_https = str()
	profile_link_color = str()
	profile_sidebar_border_color = str()
	profile_sidebar_fill_color = str()
	profile_text_color = str()
	profile_use_background_image = bool()
	protected = bool()
	screen_name = str()
	show_all_inline_media = bool()
	status = None 
	statuses_count = int()
	time_zone = str()
	url = str()
	utc_offset = int()
	verified = bool()
	withheld_in_countries = str()
	withheld_scope = str()
	
	def build_object(self):
		self.contributors_enabled = bool(self.jsondata['contributors_enabled'])
		self.created_at = str(self.jsondata['created_at'])
		self.default_profile = bool(self.jsondata['default_profile'])
		self.default_profile_image = bool(self.jsondata['default_profile_image'])
		self.description = str(self.jsondata['description'])
		self.entities = EntitiesObject(self.jsondata['entities'])
		self.favourites_count = int(self.jsondata['favourites_count'])
		self.follow_request_sent = bool(self.jsondata['request_sent']) # Doc say "Type"
		self.following = bool(self.jsondata['following']) # Doc say "Type" again
		self.followers_count = int(self.jsondata['followers_count'])
		self.friends_count = int(self.jsondata['friends_count'])
		self.geo_enabled = bool(self.jsondata['geo_enabled'])
		self.id = long(self.jsondata['id'])
		self.id_str = str(self.jsondata['id_str'])
		self.is_translator = bool(self.jsondata['is_translator'])
		self.lang = str(self.jsondata['lang'])
		self.listed_count = int(self.jsondata['listed_count'])
		self.location = str(self.jsondata['location'])
		self.name = str(self.jsondata['name'])
		self.notifications = boolean(self.jsondata['notifications'])
		self.profile_background_color = str(self.jsondata['profile_background_color'])
		self.profile_background_image_url = str(self.jsondata['profile_background_image_url'])
		self.profile_background_image_url_https = str(self.jsondata['profile_background_image_url_https'])
		self.profile_background_tile = bool(self.jsondata['profile_background_tile'])
		self.profile_banner_url = str(self.jsondata['profile_banner_url'])
		self.profile_image_url = str(self.jsondata['profile_image_url'])
		self.profile_image_url_https = str(self.jsondata['profile_image_url_https'])
		self.profile_link_color = str(self.jsondata['profile_link_color'])
		self.profile_sidebar_border_color = str(self.jsondata['profile_sidebar_border_color'])
		self.profile_sidebar_fill_color = str(self.jsondata['profile_sidebar_fill_color'])
		self.profile_text_color = str(self.jsondata['profile_text_color'])
		self.profile_use_background_image = bool(self.jsondata['profile_use_background_image'])
		self.protected = bool(self.jsondata['protected'])
		self.screen_name = str(self.jsondata['screen_name'])
		self.show_all_inline_media = bool(self.jsondata['show_all_inline_media'])
		self.status = TweetsObject(self.jsondata['status'])
		self.statuses_count = int(self.jsondata['statuses_count'])
		self.time_zone = str(self.jsondata['time_zone'])
		self.url = str(self.jsondata['url'])
		self.utc_offset = int(self.jsondata['utc_offset'])
		self.verified = bool(self.jsondata['verified'])
		self.withheld_in_countries = str(self.jsondata['withheld_in_countries'])
		self.withheld_scope = str(self.jsondata['withheld_scope'])



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
	entities = None 
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
	user = None
	withheld_copyright = bool()
	withheld_in_countries = []
	withheld_scope = str()

	def build_object(self):
		self.contributors = self.jsondata['contributors'] #TODO: Convert into Object?
		self.coordinates = self.jsondata['coordinates'] # TODO: Object?
		print self.jsondata['created_at']
		self.created_at = str(self.jsondata['created_at'])
		self.current_user_retweet = self.jsondata['current_user_retweet'] or None
		self.entities = EntitiesObject(self.jsondata['entities'])
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
		self.user = UsersObject(self.jsondata['user'])
		self.withheld_copyright = bool(self.jsondata['withheld_copyright'])
		self.withheld_in_countries = self.jsondata['withheld_in_countries']
		self.withheld_scope = str(self.jsondata['withheld_scope'])
