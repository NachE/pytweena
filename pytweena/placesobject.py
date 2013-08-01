# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.



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

	def build_object():
		self.attributes = self.jsondata['attributes']
		self.bounding_box = self.jsondata['bounding_box']
		self.country = str(self.jsondata['country'])
		self.country_code = str(self.jsondata['country_code'])
		self.full_name = str(self.jsondata['full_name'])
		self.id = str(self.jsondata['id'])
		self.name = str(self.jsondata['name'])
		self.place_type = str(self.jsondata['place_type'])
		self.url = str(self.jsondata['url'])
