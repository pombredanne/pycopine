#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time


extensions = ['sphinx.ext.autodoc']
master_doc = 'index'
project = u'Pycopine'
copyright = unicode('2009-%s, %s' % (time.strftime('%Y'), pycopine.__author__))
release = '0.1-dev' # Do not edit (see VERSION file)
version = ".".join(release.split(".")[:2])
add_function_parentheses = True
add_module_names = False
pygments_style = 'sphinx'
autodoc_member_order = 'bysource'
exclude_patterns = ['_build']
