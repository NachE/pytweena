# Pytweena 
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import json, urllib
from pytweena.auth import PytweenaAuth
from pytweena.util import PytweenaUtil

class PytweenaAPI():

	apibaseurl = "https://api.twitter.com/1.1/"
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

		response, data = self.client.request(
			self.apibaseurl+resource+".json"+options, 
			method=http_method,
			body = post_data,
			headers = headers
		)

		#Prevent overwride
		self.response = response
		self.data = data
		jsondata = json.loads(data)
		self.jsondata = jsondata
		return response, data


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
		if 'slug' in parameters:
			return self.users_suggestions_slug(parameters)
		else:
			return self.req_GET('users/suggestions', parameters)

	def users_suggestions_slug_members(self, parameters = {}):
		slug = str(parameters.pop('slug'))
		return self.req_GET('users/suggestions/'+slug+'/members', parameters)


	# Favorites
	# =========

	def favorites_list(self, parameters = {}):
		return self.req_GET('favorites/list', parameters)
	def favorites_destroy(self, parameters = {}):
		return self.req_POST('favorites/destroy', parameters)
	def favorites_create(self, parameters = {}): 
		return self.req_POST('favorites/create', parameters)


	# Lists
	# =====

	def lists_list(self, parameters = {}):
		return self.req_GET('lists/list', parameters)
	def lists_statuses(self, parameters = {}):
		return self.req_GET('lists/statuses', parameters)
	def lists_members_destroy(self, parameters = {}):
		return self.req_POST('lists/members/destroy', parameters)
	def lists_memberships(self, parameters = {}):
		return self.req_GET('lists/memberships', parameters)
	def lists_subscribers(self, parameters = {}):
		return self.req_GET('lists/subscribers', parameters)
	def lists_subscribers_create(self, parameters = {}):
		return self.req_POST('lists/subscribers', parameters)
	def lists_subscribers_show(self, parameters = {}):
		return self.req_GET('lists/subscribers/show', parameters)
	def lists_subscribers_destroy(self, parameters = {}):
		return self.req_POST('lists/subscribers/destroy', parameters)
	def lists_members_create_all(self, parameters = {}):
		return self.req_POST('lists/members/create_all', parameters)
	def lists_members_show(self, parameters = {}):
		return self.req_GET('lists/members/show', parameters)
	def lists_members(self, parameters = {}):
		return self.req_GET('lists/members', parameters)
	def lists_members_create(self, parameters = {}):
		return self.req_POST('lists/members/create', parameters)
	def lists_destroy(self, parameters = {}):
		return self.req_POST('lists/destroy', parameters)
	def lists_update(self, parameters = {}):
		return self.req_POST('lists/update', parameters)
	def lists_create(self, parameters = {}):
		return self.req_POST('lists/create', parameters)
	def lists_show(self, parameters = {}):
		return self.req_GET('lists/show', parameters)
	def lists_subscriptions(self, parameters = {}):
		return self.req_GET('lists/subscriptions', parameters)
	def lists_members_destroy_all(self, parameters = {}):
		return self.req_POST('lists/members/destroy_all', parameters)
	def lists_ownerships(self, parameters = {}):
		return self.req_GET('lists/ownerships', parameters)


	# Saved Searches
	# ==============

	def saved_searches_list(self, parameters = {}):
		 return self.req_GET('saved_searches/list', parameters)
	def saved_searches_show(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_GET('saved_searches/show/'+id, parameters)
	def saved_searches_create(self, parameters = {}):
		return self.req_POST('saved_searches/create', parameters)
	def saved_searches_destroy(self, parameters = {}):
		id = str(parameters.pop('id'))
		return self.req_POST('saved_searches/destroy/'+id, parameters)


	# Places & Geo
	# ============

	def geo_id(self, parameters = {}):
		place_id = str(parameters.pop('place_id'))
		return self.req_GET('geo/id/'+place_id, parameters)
	def geo_reverse_geocode(self, parameters = {}):
		return self.req_GET('geo/reverse_geocode', parameters)
	def geo_search(self, parameters = {}):
		return self.req_GET('geo/search', parameters)
	def geo_similar_places(self, parameters = {}):
		return self.req_GET('geo/similar_places', parameters)
	def geo_place(self, parameters = {}):
		return self.req_POST('geo/place', parameters)


	# Trends
	# ======

	def trends_place(self, parameters = {}):
		return self.req_GET('trends/place', parameters)
	def trends_available(self, parameters = {}):
		return self.req_GET('trends/available', parameters)
	def trends_closest(self, parameters = {}):
		return self.req_GET('trends/closest', parameters)


	# Spam Reporting
	# ==============

	def users_report_spam(self, parameters = {}):
		return self.req_POST('users/report_spam', parameters)


	# OAuth
	# =====
	# TODO or not TODO


	# Help
	# ====

	def help_configuration(self, parameters = {}):
		return self.req_GET('help/configuration', parameters)
	def help_languages(self, parameters = {}):
		return self.req_GET('help/languages', parameters)
	def help_privacy(self, parameters = {}):
		return self.req_GET('help/privacy', parameters)
	def help_tos(self, parameters = {}):
		return self.req_GET('help/tos', parameters)
	def application_rate_limit_status(self, parameters = {}):
		return self.req_GET('application/rate_limit_status', parameters)


	# Extra methods
#	def query(resource, parameters {}):
#		if resource == 'statuses/mentions_timeline':
#		elif resource == 'statuses/user_timeline':
#		elif resource == 'statuses/home_timeline':
#		elif resource == 'statuses/retweets_of_me':
#		elif resource == 'statuses/retweets/:id':
#		elif resource == 'statuses/show/:id':
#		elif resource == 'statuses/destroy/:id':
#		elif resource == 'statuses/update':
#		elif resource == 'statuses/retweet/:id':
#		elif resource == 'statuses/update_with_media':
#		elif resource == 'statuses/oembed':
#		elif resource == 'statuses/retweeters/ids':
#		elif resource == 'search/tweets':
#		elif resource == 'statuses/filter':
#		elif resource == 'statuses/sample':
#		elif resource == 'statuses/firehose':
#		elif resource == 'user':
#		elif resource == 'site':
#		elif resource == 'direct_messages':
#		elif resource == 'direct_messages/sent':
#		elif resource == 'direct_messages/show':
#		elif resource == 'direct_messages/destroy':
#		elif resource == 'direct_messages/new':
#		elif resource == 'friendships/no_retweets/ids':
#		elif resource == 'friends/ids':
#		elif resource == 'followers/ids':
#		elif resource == 'friendships/lookup':
#		elif resource == 'friendships/incoming':
#		elif resource == 'friendships/outgoing':
#		elif resource == 'friendships/create':
#		elif resource == 'friendships/destroy':
#		elif resource == 'friendships/update':
#		elif resource == 'friendships/show':
#		elif resource == 'friends/list':
#		elif resource == 'followers/list':
#		elif resource == 'account/settings':
#		elif resource == 'account/verify_credentials':
#		elif resource == 'account/settings':
#		elif resource == 'account/update_delivery_device':
#		elif resource == 'account/update_profile':
#		elif resource == 'account/update_profile_background_image':
#		elif resource == 'account/update_profile_colors':
#		elif resource == 'account/update_profile_image':
#		elif resource == 'blocks/list':
#		elif resource == 'blocks/ids':
#		elif resource == 'blocks/create':
#		elif resource == 'blocks/destroy':
#		elif resource == 'users/lookup':
#		elif resource == 'users/show':
#		elif resource == 'users/search':
#		elif resource == 'users/contributees':
#		elif resource == 'users/contributors':
#		elif resource == 'account/remove_profile_banner':
#		elif resource == 'account/update_profile_banner':
#		elif resource == 'users/profile_banner':
#		elif resource == 'users/suggestions/:slug':
#		elif resource == 'users/suggestions':
#		elif resource == 'users/suggestions/:slug/members':
#		elif resource == 'favorites/list':
#		elif resource == 'favorites/destroy':
#		elif resource == 'favorites/create':
#		elif resource == 'lists/list':
#		elif resource == 'lists/statuses':
#		elif resource == 'lists/members/destroy':
#		elif resource == 'lists/memberships':
#		elif resource == 'lists/subscribers':
#		elif resource == 'lists/subscribers/create':
#		elif resource == 'ists/subscribers/show':
#		elif resource == 'lists/subscribers/destroy':
#		elif resource == 'lists/members/create_all':
#		elif resource == 'lists/members/show':
#		elif resource == 'lists/members':
#		elif resource == 'lists/members/create':
#		elif resource == 'lists/destroy':
#		elif resource == 'lists/update':
#		elif resource == 'lists/create':
#		elif resource == 'lists/show':
#		elif resource == 'lists/subscriptions':
#		elif resource == 'lists/members/destroy_all':
#		elif resource == 'lists/ownerships':
#		elif resource == 'saved_searches/list':
#		elif resource == 'saved_searches/show/:id':
#		elif resource == 'saved_searches/create':
#		elif resource == 'saved_searches/destroy/:id':
#		elif resource == 'geo/id/:place_id':
#		elif resource == 'geo/reverse_geocode':
#		elif resource == 'geo/search':
#		elif resource == 'geo/similar_places':
#		elif resource == 'geo/place':
#		elif resource == 'trends/place':
#		elif resource == 'trends/available':
#		elif resource == 'trends/closest':
#		elif resource == 'users/report_spam':
#		elif resource == 'oauth/authenticate':
#		elif resource == 'oauth/authorize':
#		elif resource == 'oauth/access_token':
#		elif resource == 'oauth/request_token':
#		elif resource == 'oauth2/token':
#		elif resource == 'oauth2/invalidate_token':
#		elif resource == 'help/configuration':
#		elif resource == 'help/languages':
#		elif resource == 'help/privacy':
#		elif resource == 'help/tos':
#		elif resource == 'aplication/rate_limit_status':
