#!/usr/bin/env python
#
# Copyright (C) 2010, 2011 Linaro Limited
#
# Author: Zygmunt Krynicki <zygmunt.krynicki@linaro.org>
#
# This file is part of json-document
#
# json-document is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# json-document is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with json-document.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import sys

try:
    from setuptools import setup, find_packages
except ImportError as exc:
    print("This package requires setuptools to be configured")
    print("It can be installed with debian/ubuntu package python-setuptools")
    print(exc)
    raise


if sys.version_info[0] > 2:
    jsv_min_version = '2.4'
else:
    jsv_min_version = '2.1'

setup(
    name='json-document',
    version=":versiontools:json_document:",
    author="Zygmunt Krynicki",
    author_email="zkrynicki@gmail.com",
    url="http://github.com/zyga/json-document/",
    packages=find_packages(),
    description="Powerful and intuitive document bridge for JSON",
    test_suite='unittest2.collector',
    license="LGPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General Public"
         " License (LGPL)"),
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Testing"],
    install_requires=[
        'json-schema-validator >= ' + jsv_min_version,
        'simplejson'],
    setup_requires=[
        'versiontools >= 1.8.2'],
    tests_require=[
        'unittest2',
        'mockfs >= 0.2'],
    zip_safe=True)
