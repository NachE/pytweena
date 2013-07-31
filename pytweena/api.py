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





