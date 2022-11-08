from pelican.plugins import avatar, webassets, sitemap
from urllib.parse import quote_plus

AUTHOR = 'Gissel'
SITENAME = "Gunnar's blog"
SITEURL = 'http://localhost:8080'
#SITEURL = 'https://www.gunnargissel.com

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

THEME = '../straight-laced'

DISPLAY_PAGES_ON_MENU = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGINS = [ 'avatar','webassets','sitemap']

AVATAR_AUTHOR_EMAIL='monknomo@gmail.com'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
DEVTO_USERNAME = 'monknomo'
DEVTO_ALT_TEXT = 'Gunnar Gissel\'s DEV Profile'

LOGO = {'small': "<div class='logo logo--small'></div>",
    'medium': "<div class='logo logo--medium'></div>",
    'large': "<div class='logo logo--large'></div>",
    'xtralarge':"<div class='logo logo--xtralarge'></div>",
    'png':"theme/images/logo.png"}
JINJA_FILTERS= {'url_quote':lambda u: quote_plus(u)}

TWITTER_USERNAME='monknomo'
TWEET_CAPTION='Another great blog post!\n'

FACEBOOK_ID='4801181'
FACEBOOK_APP_ID='962146893962636'
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
