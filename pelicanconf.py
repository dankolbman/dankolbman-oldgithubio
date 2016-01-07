#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dan Kolbman'
SITENAME = 'Dan Kolbman'
SITESUBTITLE = ''
SITEURL = ''

MD_EXTENSIONS = ['codehilite', 'extra']

GITHUBURL = 'https://github.com/dankolbman'
TWITTERURL = 'https://twitter.com/DanKolbman'
TRACKERURL = 'http://dankolbman.com'

PATH = 'content'
THEME = 'theme'

STATIC_PATHS = ['posts']
ARTICLE_PATHS = ['posts']

ARTICLE_SAVE_AS = '{slug}/post.html'
ARTICLE_URL = '{slug}/post.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

MENUITEMS = (('About', '#'),
             ('Contact', '#'),)

DEFAULT_PAGINATION = 5

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
