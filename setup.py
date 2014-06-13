#!/usr/bin/env python
# -*- coding: utf8 -*-

"""setup
(C) Franck Barbenoire <contact@franck-barbenoire.fr>
License : GPL v3"""

from distutils.core import setup
from setuptools import find_packages

setup(name = "roofer",
    version = "0.0.1",
    description = "",
    author = "Franck Barbenoire",
    author_email = "conatct@franck-barbenoire.fr",
    url = "https://github.com/franckinux/roofer",
    packages = find_packages(),
    include_package_data = True,
    #zip_safe = False,
    install_requires = ['Pillow',],
    classifiers = ['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Multimedia :: Graphics :: Graphics Conversion']
)
