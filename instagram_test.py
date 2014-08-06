# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:03:25 2014

@author: ayip
"""

from instagram.client import InstagramAPI
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'local':
    try:
        from test_settings import *

        InstagramAPI.host = test_host
        InstagramAPI.base_path = test_base_path
        InstagramAPI.access_token_field = "access_token"
        InstagramAPI.authorize_url = test_authorize_url
        InstagramAPI.access_token_url = test_access_token_url
        InstagramAPI.protocol = test_protocol
    except Exception:
        pass

client_id = 'XX'
client_secret = 'XX'
redirect_uri = 'https://instagram.com'
raw_scope = 'basic'
scope = raw_scope.split(' ')
# For basic, API seems to need to be set explicitly
if not scope or scope == [""]:
    scope = ["basic"]

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
redirect_uri = api.get_authorize_login_url(scope = scope)

print "Visit this page and authorize access in your browser:\n", redirect_uri

code = raw_input("Paste in code in query string after redirect: ").strip()

access_token = api.exchange_code_for_access_token(code)
print "access token:\n", access_token

#important functions to generate instagram metrics
u = api.user_search('FAGE')  #creates user object
m = api.user_recent_media(user_id=u[0].id,count=10)    #creates array of media objects
m = api.user_recent_media(user_id=u[0].id,count=10,max_id=m[0][9].id)  #creates array of media objects
likes = m[0][0].like_count
comments = m[0][0].comment_count
tags = m[0][0].tags
