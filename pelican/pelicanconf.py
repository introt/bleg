from datetime import datetime

AUTHOR = 'introt'
SITENAME = 'introt bleg'
SITETITLE = SITENAME
SITESUBTITLE = 'stuff I care to share'
SITEDESCRIPTION = SITESUBTITLE
SITEURL = ''
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.ico"

# not needed; we don't want to alter the default crawling behaviour. see:
# https://moz.com/learn/seo/robots-meta-directives
#ROBOTS = "index, follow"

COPYRIGHT_YEAR = f"""{datetime.now().year} - This work is licensed under a <a href="https://creativecommons.org/licenses/by-nd/4.0/">Creative Commons Attribution-NoDerivatives 4.0 International License</a>."""

#CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('GitHub', 'https://github.com/introt/'),
        ('Docs', 'https://introt.github.io/docs/'),
        ('Feedback', 'https://github.com/introt/bleg/discussions'),
        ('Issues?', 'https://github.com/introt/bleg/issues'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'Flex'
# https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
HOME_HIDE_TAGS = True
USE_GOOGLE_FONTS = False

# Path to Plugins
PLUGIN_PATHS = ['pelican-plugins']
# Enable i18n plugin, probably you already have some others here.
PLUGINS = ['i18n_subsites']
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"

LOCALE = ("en_US", "en_US.utf8")
OG_LOCALE = LOCALE

I18N_SUBSITES = {
        "fi": {
            "SITENAME": "introt blegi",
            "LOCALE": "fi_FI",
            },
        }

