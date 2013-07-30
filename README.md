pytweena
========

Python library for twitter API. 

Pytweena try to be very transparent: you send query and get json response to manage with your own app. Instead maybe in a future we'll work on a class to be less transparent but more easy.


**Documentation**

The core of pytweena is ALPHA, so it can be changed completly.

Pytweena wrap transparently the twitter REST API v1.1 using the same names.
- GET statuses/mentions_timeline  ->  api.mentions_timeline()
- GET statuses/user_timeline  ->  api.user_timeline()

Also you can send the same options documented on twitter api v1.1:
- api.mentions_timeline({'count' : 10, 'since_id' : 12345, 'trim_user' : 'true'})


**Roadmap**
- Support for REST API v1.1
- Support for Streaming APIs
- Add error control, pytweena never should crash
- Study if we can wrap json 
  responses into python object
  for easy manage this.

**Status**
 * REST API v1.1:
- Timelines support: OK
- Tweets support: OK except media upload
- Search support: OK
- Streaming support: TODO
- Direct Messages support: OK
- Friends & Followers support: TODO
- Users support: TODO
- Suggested Users support: TODO
- Favorites support: TODO
- Lists support: TODO
- Saved searches support: TODO
- Places & Geo support: TODO
- Trends support: TODO
- Spam Reporting support: TODO
- OAuth support: OK with python-oauth2 lib
- Help support: TODO 
