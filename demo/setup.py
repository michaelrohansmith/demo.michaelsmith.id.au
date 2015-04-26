#!/usr/bin/env python

from distutils.core import setup

setup(name='michaelsmith',
      version='1.0',
      description='Demo for Nothing but web',
      author='Michael Smith',
      author_email='smithm@netapps.com.au',
      url='http://www.python.org/sigs/distutils-sig/',
      packages=['demo'],
      package_data={'demo': ['templates/demo/*.html']},
     )
