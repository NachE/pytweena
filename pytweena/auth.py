# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

#require for python-oauth2
#twitter api v1.1 oauth2
import oauth2 as oauth

class PytweenaAuth:

	@staticmethod
	def login(consumer_key, consumer_secret, access_token, access_token_secret):
		consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
		access_token = oauth.Token(key=access_token, secret=access_token_secret)
		client = oauth.Client(consumer, access_token)
		return client			
