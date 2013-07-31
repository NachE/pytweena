# Pytweena
# Copyright 2013 J.A. Nache
# See LICENSE for details.

import os
import random
import string
import mimetypes

class PytweenaUtil:

	@staticmethod
	def mkMultipartImageHeaders(img_path, parameters = {}):
		#set vars
		filename = os.path.basename(img_path)
		file = open(img_path, 'rb')
		content_type =  mimetypes.guess_type(img_path)[0] or 'application/octet-stream'

		char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
		boundary = ''.join(random.sample(char_set*30,30))
		
		# This var will contain body
		mpart = []

		#build others parameters before image
		for key,value in parameters.iteritems():
			mpart.append('--'+boundary)
			mpart.append('Content-Disposition: form-data; name="'+key+'"')
			#TODO: Maybe content type here?
			mpart.append('')
			mpart.append(value)

		#Now build the img body
		mpart.append('--'+boundary)
		mpart.append('Content-Disposition: form-data; name="media[]"; filename="'+filename+'"')
		mpart.append('Content-Transfer-Encoding: binary')
		mpart.append('Content-Type: '+str(content_type))
		mpart.append('')
		mpart.append(file.read())

		#Finish the data
		mpart.append('--'+boundary+'--')

		#the body to send in request
		body = '\r\n'.join(mpart) 

		# the header to send in request
		# htmllib (oauth2) expects a dict
		# for headers
		header = {'Content-Length' : str(len(body)), 
				'Content-Type' : 'multipart/form-data; boundary='+boundary}

		#return results
		return header, body

