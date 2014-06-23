#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import pyeasyga

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = ['tox']

setup(
    name='pyeasyga',
    version=pyeasyga.__version__,
    description='An easy-to-use Genetic Algorithm implementation in Python',
    long_description=readme + '\n\n' + history,
    author='Ayodeji Remi-Omosowon',
    author_email='remiomosowon@gmail.com',
    url='https://github.com/remiomosowon/pyeasyga',
    packages=[
        'pyeasyga',
    ],
    package_dir={'pyeasyga':
                 'pyeasyga'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pyeasyga',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
