# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

# Twitter doc:
# https://dev.twitter.com/docs/platform-objects

# TODO: boolN('true') and bool('false') are True
# Bug? json.loads() should return False when 'false'
# and True when 'true'. Keep watching

# TODO: Keep watching Objects like
# contributors or Sizes (Entities)
# Need classes?
# For now, it are represented by {}

# functions to safe type or None
def strN(s):
	return s if s == None else unicode(s)
def longN(l):
	return l if l == None else long(l)
def boolN(b):
	return b if b == None else bool(b)
def intN(i):
	return i if i == None else int(i)

#General object
#class PytweenaObject(object):
class PytweenaObject:

	jsondata = {}

	def __init__(self, jsondata = {}):
		if jsondata == None:
			pass
		elif len(jsondata) > 0:
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

	def build_object(self):
		self.hashtags = self.jsondata.get('hashtags')
		self.media = self.jsondata.get('media')
		self.urls = self.jsondata.get('urls')
		self.user_mentions = self.jsondata.get('user_mentions')


# https://dev.twitter.com/docs/platform-objects/places
class PlacesObject(PytweenaObject):
	attributes = {}
	bounding_box = {} #have coordinates[] and type unicode()
	country = unicode()
	country_code = unicode()
	full_name = unicode()
	id = unicode()
	name = unicode()
	place_type = unicode()
	url = unicode()

	def build_object(self):
		self.attributes = self.jsondata.get('attributes')
		self.bounding_box = self.jsondata.get('bounding_box')
		self.country = strN(self.jsondata.get('country'))
		self.country_code = strN(self.jsondata.get('country_code'))
		self.full_name = strN(self.jsondata.get('full_name'))
		self.id = strN(self.jsondata.get('id'))
		self.name = strN(self.jsondata.get('name'))
		self.place_type = strN(self.jsondata.get('place_type'))
		self.url = strN(self.jsondata.get('url'))


# https://dev.twitter.com/docs/platform-objects/users
class UsersObject(PytweenaObject):
	
	contributors_enabled = bool()
	created_at = unicode()
	default_profile = bool()
	default_profile_image = bool()
	description = unicode()
	entities = None
	favourites_count = int()
	follow_request_sent = bool() # Doc say "Type"
	following = bool() # Doc say "Type" again
	followers_count = int()
	friends_count = int()
	geo_enabled = bool()
	id = long()
	id_str = unicode()
	is_translator = bool()
	lang = unicode()
	listed_count = int()
	location = unicode()
	name = unicode()
	notifications = bool()
	profile_background_color = unicode()
	profile_background_image_url = unicode()
	profile_background_image_url_https = unicode()
	profile_background_tile = bool()
	profile_banner_url = unicode()
	profile_image_url = unicode()
	profile_image_url_https = unicode()
	profile_link_color = unicode()
	profile_sidebar_border_color = unicode()
	profile_sidebar_fill_color = unicode()
	profile_text_color = unicode()
	profile_use_background_image = bool()
	protected = bool()
	screen_name = unicode()
	show_all_inline_media = bool()
	status = None 
	statuses_count = int()
	time_zone = unicode()
	url = unicode()
	utc_offset = int()
	verified = bool()
	withheld_in_countries = unicode()
	withheld_scope = unicode()
	
	def build_object(self):
		self.contributors_enabled = boolN(self.jsondata.get('contributors_enabled'))
		self.created_at = strN(self.jsondata.get('created_at'))
		self.default_profile = boolN(self.jsondata.get('default_profile'))
		self.default_profile_image = boolN(self.jsondata.get('default_profile_image'))
		self.description = strN(self.jsondata.get('description'))
		self.entities = EntitiesObject(self.jsondata.get('entities'))
		self.favourites_count = int(self.jsondata.get('favourites_count'))
		self.follow_request_sent = boolN(self.jsondata.get('request_sent')) # Doc say "Type"
		self.following = boolN(self.jsondata.get('following')) # Doc say "Type" again
		self.followers_count = int(self.jsondata.get('followers_count'))
		self.friends_count = int(self.jsondata.get('friends_count'))
		self.geo_enabled = boolN(self.jsondata.get('geo_enabled'))
		self.id = long(self.jsondata.get('id'))
		self.id_str = strN(self.jsondata.get('id_str'))
		self.is_translator = boolN(self.jsondata.get('is_translator'))
		self.lang = strN(self.jsondata.get('lang'))
		self.listed_count = int(self.jsondata.get('listed_count'))
		self.location = strN(self.jsondata.get('location'))
		self.name = strN(self.jsondata.get('name'))
		self.notifications = boolN(self.jsondata.get('notifications'))
		self.profile_background_color = strN(self.jsondata.get('profile_background_color'))
		self.profile_background_image_url = strN(self.jsondata.get('profile_background_image_url'))
		self.profile_background_image_url_https = strN(self.jsondata.get('profile_background_image_url_https'))
		self.profile_background_tile = boolN(self.jsondata.get('profile_background_tile'))
		self.profile_banner_url = strN(self.jsondata.get('profile_banner_url'))
		self.profile_image_url = strN(self.jsondata.get('profile_image_url'))
		self.profile_image_url_https = strN(self.jsondata.get('profile_image_url_https'))
		self.profile_link_color = strN(self.jsondata.get('profile_link_color'))
		self.profile_sidebar_border_color = strN(self.jsondata.get('profile_sidebar_border_color'))
		self.profile_sidebar_fill_color = strN(self.jsondata.get('profile_sidebar_fill_color'))
		self.profile_text_color = strN(self.jsondata.get('profile_text_color'))
		self.profile_use_background_image = boolN(self.jsondata.get('profile_use_background_image'))
		self.protected = boolN(self.jsondata.get('protected'))
		self.screen_name = strN(self.jsondata.get('screen_name'))
		self.show_all_inline_media = boolN(self.jsondata.get('show_all_inline_media'))
		self.status = TweetsObject(self.jsondata.get('status'))
		self.statuses_count = int(self.jsondata.get('statuses_count'))
		self.time_zone = strN(self.jsondata.get('time_zone'))
		self.url = strN(self.jsondata.get('url'))
		self.utc_offset = int(self.jsondata.get('utc_offset'))
		self.verified = boolN(self.jsondata.get('verified'))
		self.withheld_in_countries = strN(self.jsondata.get('withheld_in_countries'))
		self.withheld_scope = strN(self.jsondata.get('withheld_scope'))



# https://dev.twitter.com/docs/platform-objects/tweets
class TweetsObject(PytweenaObject):

	#TODO: Object?
	#https://dev.twitter.com/docs/platform-objects/tweets#obj-contributors
	contributors = {}

	#TODO: Object?
	#https://dev.twitter.com/docs/platform-objects/tweets#obj-coordinates 
	coordinates = {}
 
	created_at = unicode()
	current_user_retweet = {}
	entities = None 
	favorite_count = int()
	favorited = bool()
	filter_level = unicode()
	geo = {} #DEPRECATED
	id = long() #int64 signed Can be Null
	id_str = unicode()
	in_reply_to_screen_name = unicode()
	in_reply_to_status_id = long() #int64 Can be Null
	in_reply_to_status_id_str = unicode()
	in_reply_to_user_id = long() #int64
	in_reply_to_user_id_str = unicode()
	lang = unicode()
	place = {} # Places Obj https://dev.twitter.com/docs/platform-objects/places
	possibly_sensitive = bool()
	scopes = {}
	retweet_count = int()
	retweeted = bool()
	source = unicode()
	text = unicode()
	truncated = bool()
	user = None
	withheld_copyright = bool()
	withheld_in_countries = []
	withheld_scope = unicode()

	def build_object(self):
		self.contributors = self.jsondata.get('contributors') #TODO: Convert into Object?
		self.coordinates = self.jsondata.get('coordinates') # TODO: Object?
		self.created_at = strN(self.jsondata.get('created_at'))
		self.current_user_retweet = self.jsondata.get('current_user_retweet')
		self.entities = EntitiesObject(self.jsondata.get('entities'))
		self.favorite_count = int(self.jsondata.get('favorite_count'))
		self.favorited = boolN(self.jsondata.get('favorited')) or None #Bug? keep waching
		self.filter_level = strN(self.jsondata.get('filter_level'))
		self.geo = self.jsondata.get('geo') #DEPRECATED
		self.id = long(self.jsondata.get('id')) # or None?
		self.id_str = strN(self.jsondata.get('id_str'))
		self.in_reply_to_screen_name = self.jsondata.get('in_reply_to_screen_name')
		self.in_reply_to_status_id = longN(self.jsondata.get('in_reply_to_status_id'))#or None?
		self.in_reply_to_status_id_str = strN(self.jsondata.get('in_reply_to_status_id_str'))
		self.in_reply_to_user_id = longN(self.jsondata.get('in_reply_to_user_id'))#or None?
		self.in_reply_to_user_id_str = strN(self.jsondata.get('in_reply_to_user_id_str'))
		self.lang = strN(self.jsondata.get('lang'))
		self.place = PlacesObject(self.jsondata.get('place')) #It can be Null, so be carefully
		self.possibly_sensitive = boolN(self.jsondata.get('possibly_sensitive'))
		self.scopes = self.jsondata.get('scopes') # Dict or None 
		self.retweet_count = int(self.jsondata.get('retweet_count'))
		self.retweeted = boolN(self.jsondata.get('retweeted'))
		self.source = strN(self.jsondata.get('source'))
		self.text = strN(self.jsondata.get('text'))
		self.truncated = boolN(self.jsondata.get('truncated'))
		self.user = UsersObject(self.jsondata.get('user'))
		self.withheld_copyright = boolN(self.jsondata.get('withheld_copyright'))
		self.withheld_in_countries = self.jsondata.get('withheld_in_countries') # [] or None
		self.withheld_scope = strN(self.jsondata.get('withheld_scope'))
