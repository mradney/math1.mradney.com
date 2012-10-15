# -*- coding: utf-8 -*-
#: settings for liquidluck

# Required to import from _base
import sys, os
sys.path.append(os.getcwd())

# Import settings from base-site
from _base.settings import *

site = {
    'name': "SBCD Math 1 Int.", # your site name
    'url': "http://math1.mradney.com/",  # your site url
    'prefix': "blog",
}

theme = {
    'name': 'default',
    'vars': {
        'disqus': "mradney",
        'analytics': "UA-35532935-2",
        'navigation': [ 
            {'name': "Blog", 'link': "/blog/"},
            {'name': "Files", 'link': "/pages/files.html"},
            {'name': "Resources", 'link': "/pages/resources.html"},
            {'name': "Schedule", 'link': "/pages/schedule.html"},
            {'name': "[topics]", 'link': "/blog/tag/"},
        ],
    }
}
