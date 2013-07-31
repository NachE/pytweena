pytweena
========

Python library for twitter API. 

Pytweena try to be very transparent: send query, get json. API v1.1. 


**Documentation**

The core of pytweena is ALPHA, so it can be changed completly.

Pytweena wrap transparently the twitter REST API v1.1 using the same names.
- GET statuses/mentions_timeline  ->  api.statuses_mentions_timeline()
- GET statuses/user_timeline  ->  api.statuses_user_timeline()

Also you can send the same options documented on twitter api v1.1:
- api.statuses_mentions_timeline({'count' : 10, 'since_id' : 12345, 'trim_user' : 'true'})
- api.statuses_update({'status' : 'Hey, this is a tweet!'})
- api.statuses_update_with_media({'status': 'Hi!, do you like this img? (4)', 'media[]': 'copperhead-snake-head.jpg'})


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
- Tweets support: OK 
- Search support: OK
- Streaming support: TODO
- Direct Messages support: OK
- Friends & Followers support: OK
- Users support: OK
- Suggested Users support: OK
- Favorites support: OK
- Lists support: OK
- Saved searches support: OK
- Places & Geo support: OK
- Trends support: OK
- Spam Reporting support: OK
- OAuth support: OK with python-oauth2 lib
- Help support: OK
