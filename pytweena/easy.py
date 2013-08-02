# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

from pytweena.api import PytweenaAPI
from pytweena.objects import *

class PytweenaEasy(PytweenaAPI):

#contributors = Tweets

	def test(self):
		self.statuses_show({'id':8062317551})
		cosa = TweetsObject(self.jsondata)

	def req_POST(self, resource, parameters = {}):
		response, data = self.req_resource(resource, "POST", parameters)

	def req_GET(self, resource, parameters = {}):
		response, data = self.req_resource(resource, "GET", parameters)

