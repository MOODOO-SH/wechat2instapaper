import os
import sys
import urllib2
import urlparse
import simplejson as json
import oauth2 as oauth
from lxml import etree
from urllib import urlencode

from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc

__author__= "Chanjh <jiahao0408@gmail.com>"

__changeFrom__ = "https://github.com/nickbarnwell/Instapaper-py"

__doc__ = """
A Python wrapper for adding new url to the Instapaper.

http://www.instapaper.com/api/full
"""


_BASE_ = "https://www.instapaper.com"
_API_VERSION_ = "api/1"
_ACCESS_TOKEN_ = "oauth/access_token"
_BOOKMARKS_ADD_ = "bookmarks/add"


class Bookmark(object):
    def __init__(self, parent, params):
        self.parent = parent
        self.__text = None
        self.__html = None
        self.__dict__.update(params)

    @property
    def html(self):
        if self.__html is None:
            response, html = self.parent.http.request(
                        "/".join([_BASE_, _API_VERSION_, _BOOKMARKS_TEXT_]),
                        method='POST',
                        body=urlencode({ 
                            'bookmark_id': self.bookmark_id, 
                            }))
            if response.get("status") == "200":
                self.__html = html
        return self.__html

    @property
    def text(self):
        if self.__text is None:
            self.__text = dehtml(self.html)
        return self.__text

    def star(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError


class Instapaper(object):
    def __init__(self, oauthkey, oauthsec):
        self.consumer = oauth.Consumer(oauthkey, oauthsec)
        self.client = oauth.Client(self.consumer)
        self.token = None
        self.http = None

    def login(self, username, password):
        response, content = self.client.request(
                    "/".join([_BASE_, _API_VERSION_, _ACCESS_TOKEN_]),
                    "POST", urlencode({
                    'x_auth_mode': 'client_auth',
                    'x_auth_username': username,
                    'x_auth_password': password}))
        _oauth = dict(urlparse.parse_qsl(content))
        self.token = oauth.Token(_oauth['oauth_token'], 
                                 _oauth['oauth_token_secret'])
        self.http = oauth.Client(self.consumer, self.token)

    def add(self, url):
        response, data = self.http.request(
                    "/".join([_BASE_, _API_VERSION_, _BOOKMARKS_ADD_]),
                    method='POST',
                    body=urlencode({ 
                        'url':url
                        }))
        marks = []
        items = json.loads(data)
        for item in items:
            if item.get("type") == "error":
                raise Exception(item.get("message"))
                return 0,marks
            elif item.get("type") == "bookmark":
                marks.append(Bookmark(self, item))
                return 1,marks

