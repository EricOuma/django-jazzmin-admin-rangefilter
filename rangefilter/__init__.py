# -*- coding: utf-8 -*-

import django

__author__ = "Eric Ouma"
__version__ = "1.0.1"

if django.VERSION < (3, 2):
    default_app_config = "rangefilter.apps.RangeFilterConfig"


VERSION = __version__
