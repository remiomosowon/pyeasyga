#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                version_file, re.M)
    if version_match:
        return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = ['six']

test_requirements = ['tox']

setup(
    name='pyeasyga',
    version=find_version('pyeasyga', '__init__.py'),
    description='A simple and easy-to-use implementation of a Genetic Algorithm library in Python',
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
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
