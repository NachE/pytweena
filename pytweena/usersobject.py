# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

from pytweena.pytweenaobject import PytweenaObject
from pytweena.entitiesobject import EntitiesObject
from pytweena.tweetsobject import TweetsObjects


# https://dev.twitter.com/docs/platform-objects/users
class UsersObject(PytweenaObject):

	contributors_enabled = bool()
	created_at = str()
	default_profile = bool()
	default_profile_image = bool()
	description = str()
	entities = EntitiesObject()
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
	#status = TweetsObject()
	statuses_count = int()
	time_zone = str()
	url = str()
	utc_offset = int()
	verified = bool()
	withheld_in_countries = str()
	withheld_scope = str()


	def build_object():
		self.contributors_enabled = bool(self.jsondata['contributors_enabled'])
		self.created_at = str(self.jsondata['created_at'])
		self.default_profile = bool(self.jsondata['default_profile'])
		self.default_profile_image = bool(self.jsondata['default_profile_image'])
		self.description = str(self.jsondata['description'])
		self.entities.load(self.jsondata['entities'])
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
		self.status.load(self.jsondata['status'])
		self.statuses_count = int(self.jsondata['statuses_count'])
		self.time_zone = str(self.jsondata['time_zone'])
		self.url = str(self.jsondata['url'])
		self.utc_offset = int(self.jsondata['utc_offset'])
		self.verified = bool(self.jsondata['verified'])
		self.withheld_in_countries = str(self.jsondata['withheld_in_countries'])
		self.withheld_scope = str(self.jsondata['withheld_scope'])

