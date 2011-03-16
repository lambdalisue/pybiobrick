#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  16-Mar-2011.
#
from distutils.core import setup

setup(
    name='pybiobrick',
    version='0.11',
    description="Generate BioBrick sequence image eps file from XML/String formatted sequence.",
    author="Alisue",
    author_email="alisue@hashnote.tk",
    url=r"http://www.hashnote.tk/",
    packages=['pybiobrick', 'pybiobrick.bricks', 'pybiobrick.parser', 'pybiobrick.utils'],
    scripts = ['bin/pybiobrick'],
    install_requires=[
        'PyXML', 'pyx'
    ],
)
