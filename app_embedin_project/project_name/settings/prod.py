#!/usr/bin/env python
# encoding: utf-8

# need use python manager.py collectstatic collect static files to STATIC_ROOT folder
# render engine not support Chinese ....
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
