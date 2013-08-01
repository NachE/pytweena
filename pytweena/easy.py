# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

from pytweena.api import PytweenaAPI
from pytweena.tweetsobject import TweetsObject

class PytweenaEasy(PytweenaAPI):

#contributors = Tweets

	def test(self):
		cosa = TweetsObject()


	def req_POST(self, resource, parameters = {}):
		response, data = self.req_resource(resource, "POST", parameters)

	def req_GET(self, resource, parameters = {}):
                res = self.req_resource(resource, "GET", parameters)




