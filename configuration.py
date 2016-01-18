#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Kolbman'
SITENAME = 'Daniel Kolbman'
SITESUBTITLE = ''
SITEBLURB = '''<p>Hey! I'm Dan Kolbman. I studied Physics at the Rochester Institute
            of Technology where I created a
            <a href="https://github.com/dankolbman/BCIM">dynamics simulation</a>
            using high performance computing to model
            <a href="/KolbmanCapII.pdf">cancer cell mechanics</a>.
            </p>

            <p>
            In my free time, I like take a break from the all that serious science
            and make silly web apps to help me find
            <a href="https://github.com/foodsnag/foodsnag-web">free food</a>
            or write bots to crawl through
            <a href="https://github.com/dankolbman/CleverTind">dating apps</a>.
            </p>
            
            <p>
            I'm an advocate of Open Source/Open Science and publish most of my work
            <a href="https://github.com/dankolbman">freely</a>.
            I gorge on tea and coffee, listen to techno religiously, and 
            <a href="http://dankolbman.xyz">travel the world</a>.
            </p>

            <p>I'm currently looking for my next challenge, so if you're in 
            need of an engineer or data scientist, give me a shout!</p>
            '''
SITEURL = ''

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'ipynb']

MD_EXTENSIONS = ['codehilite', 'extra']

GITHUBURL = 'https://github.com/dankolbman'
#TWITTERURL = 'https://twitter.com/DanKolbman'
TRACKERURL = 'http://dankolbman.xyz'
EMAIL = 'dan@kolbman.com'
PGP = 'dankolbman.asc'

PATH = 'content'
THEME = 'theme'

# I'm storing each post and it's images inside a subfolder inside posts
# so I'd like to both create pages from the posts as well as preserve the other
# files and their paths in the post's directory
STATIC_PATHS = ['posts', 'extra/favicon.ico', 'extra/CNAME', 'extra/'+PGP,
                'extra/KolbmanCapII.pdf']

ARTICLE_PATHS = ['posts']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/README.md' : {'path': 'README.md'},
    'extra/CNAME' : {'path': 'CNAME'},
    'extra/'+PGP : {'path': PGP},
    'extra/KolbmanCapII.pdf' : {'path': 'KolbmanCapII.pdf'}
}

ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
ARTICLE_URL = 'articles/{slug}/index.html'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 6

USE_FOLDER_AS_CATEGORY = False

GA = 'UA-37300370-1'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
