# Tweepy
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import json, urllib
from pytweena.auth import PytweenaAuth
from pytweena.util import PytweenaUtil

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

	def req_resource(self, resource, http_method, parameters = {}, body = '', headers = None):
		#TODO: Take a break to improve these if else

		if len(body) > 0:
			post_data = body
			options = ""
		else:
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
			body = post_data,
			headers = headers
		)

		self.jsondata = json.loads(self.data)
		return [self.response, self.data]


	# Timelines
	# =========

	def statuses_mentions_timeline(self, parameters = {}):
		return self.req_GET('statuses/mentions_timeline', parameters)

	def statuses_user_timeline(self, parameters = {}):
		return self.req_GET('statuses/user_timeline', parameters)

	def statuses_home_timeline(self, parameters = {}):
		return self.req_GET('statuses/home_timeline', parameters)

	def statuses_retweets_of_me(self, parameters = {}):
		return self.req_GET('statuses/retweets_of_me', parameters)


	# Tweets
	# ======

	def statuses_retweets(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_GET('statuses/retweets/'+id, parameters)

	def statuses_show(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_GET('statuses/show/'+id, parameters)

	def statuses_destroy(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_POST('statuses/destroy/'+id, parameters)

	def statuses_update(self, parameters = {}):
		return self.req_POST('statuses/update', parameters)

	def statuses_retweet(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_POST('statuses/retweet/'+id, parameters)

	#TODO: see later, media[] need raw image bytes
	def statuses_update_with_media(self, parameters = {}):
		img_path = parameters.pop('media[]')
		hdr, bdy = PytweenaUtil.mkMultipartImageHeaders(img_path, parameters)
		return self.req_resource('statuses/update_with_media','POST',{},bdy,hdr)

	def statuses_oembed(self, parameters = {}):
		return self.req_GET('statuses/oembed', parameters)

	def statuses_retweeters_ids(self, parameters = {}):
		return self.req_GET('statuses/retweeters/ids', parameters)


	# Search
	# ======

	def search_tweets(self, parameters = {}):
		return self.req_GET('search/tweets', parameters)


	# Streaming
	# =========
	# :O TODO


	# Direct Messages
	# ===============

	def direct_messages(self, parameters = {}):
		return self.req_GET('direct_messages', parameters)

	def direct_messages_sent(self, parameters = {}):
		return self.req_GET('direct_messages/sent', parameters)

	def direct_messages_show(self, parameters = {}):
		return self.req_GET('direct_messages/show', parameters)

	def direct_messages_destroy(self, parameters = {}):
		return self.req_POST('direct_messages/sent', parameters)

	def direct_messages_new(self, parameters = {}):
		return self.req_POST('direct_messages/new', parameters)


	# Friends & Followers
	# ===================

	def friendships_no_retweets_ids(self, parameters = {}):
		return self.req_GET('friendships/no_retweets/ids', parameters)

	def friends_ids(self, parameters = {}):
		return self.req_GET('friends/ids', parameters)

	def followers_ids(self, parameters = {}):
		return self.req_GET('followers/ids', parameters)

	def friendships_lookup(self, parameters = {}):
		return self.req_GET('friendships/lookup', parameters)

	def friendships_incoming(self, parameters = {}):
		return self.req_GET('friendships/incoming', parameters)

	def friendships_outgoing(self, parameters = {}):
		return self.req_GET('friendships/outgoing', parameters)

	def friendships_create(self, parameters = {}):
		return self.req_POST('friendships/create', parameters)

	def friendships_destroy(self, parameters = {}):
		return self.req_POST('friendships/destroy', parameters)

	def friendships_update(self, parameters = {}):
		return self.req_POST('friendships/update', parameters)

	def friendships_show(self, parameters = {}):
		return self.req_GET('friendships/show', parameters)

	def friends_list(self, parameters = {}):
		return self.req_GET('friends/list', parameters)

	def followers_list(self, parameters = {}):
		return self.req_GET('followers/list', parameters)


	# Users
	# =====

	def account_settings(self, parameters = {}):
		return self.req_GET('account/settings', parameters)

	def account_verify_credentials(self, parameters = {}):
		return self.req_GET('account/verify_credentials', parameters)

	def account_settings(self, parameters = {}):
		return self.req_POST('account/settings', parameters)

	def account_update_delivery_device(self, parameters = {}):
		return self.req_POST('account/update_delivery_device', parameters)

	def account_update_profile(self, parameters = {}):
		return self.req_POST('account/update_profile', parameters)

	def account_update_profile_background_image(self, parameters = {}):
		return self.req_POST('account/update_profile_background_image', parameters)

	def account_update_profile_colors(self, parameters = {}):
		return self.req_POST('account/update_profile_colors', parameters)

	def account_update_profile_image(self, parameters = {}):
		return self.req_POST('account/update_profile_image', parameters)

	def blocks_list(self, parameters = {}):
		return self.req_GET('blocks/list', parameters)

	def blocks_ids(self, parameters = {}):
		return self.req_GET('blocks/ids', parameters)

	def blocks_create(self, parameters = {}):
		return self.req_POST('blocks/create', parameters)

	def blocks_destroy(self, parameters = {}):
		return self.req_POST('blocks/destroy', parameters)

	def users_lookup(self, parameters = {}):
		return self.req_GET('users/lookup', parameters)

	def users_show(self, parameters = {}):
		return self.req_GET('users/show', parameters)

	def users_search(self, parameters = {}):
		return self.req_GET('users/search', parameters)

	def users_contributees(self, parameters = {}):
		return self.req_GET('users/contributees', parameters)

	def users_contributors(self, parameters = {}):
		return self.req_GET('users/contributors', parameters)

	def account_remove_profile_banner(self, parameters = {}):
		return self.req_POST('account/remove_profile_banner', parameters)

	def account_update_profile_banner(self, parameters = {}):
		return self.req_POST('account/update_profile_banner', parameters)

	def users_profile_banner(self, parameters = {}):
		return self.req_GET('users/profile_banner', parameters)


	# Suggested Users
	# ===============

	def users_suggestions_slug(self, parameters = {}):
		slug = str(parameters.pop('slug'))	
		return self.req_GET('users/suggestions/'+slug, parameters)

	def users_suggestions(self, parameters = {}):
		return self.req_GET('users/suggestions', parameters)

	def users_suggestions_slug_members(self, parameters = {}):
		slug = str(parameters.pop('slug'))
		return self.req_GET('users/suggestions/'+slug+'/members', parameters)


