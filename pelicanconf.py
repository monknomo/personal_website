#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gunnar Gissel'
AUTHOR_EMAIL = 'monknomo@gmail.com'
SITENAME = "Gunnar's Blog"
SITEURL = 'http://www.gunnargissel.com'
#SITEURL = 'http://localhost:8080'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['assets', 'gravatar','sitemap']
SITEDESCRIPTION='Gunnar Gissel is a programmer for the government.  He writes about Java, living with enterprise idiosyncrasies, automation and building.  Gunnar is his office\'s Jenkins cheerleader and is comfortable with his boots on while dealing with a big ball of mud'
TIMEZONE = 'America/Juneau'

DEFAULT_LANG = 'en'

THEME = '../straight-laced'

PAGE_PATHS=['content/pages']
ARTICLE_PATHS=['content']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None  
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
        },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
        }
    }