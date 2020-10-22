#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ast
import os
import re

from setuptools import setup, find_packages

PACKAGE_NAME = 'img_processing'
SOURCE_DIR = 'img_processing'
MAIN_MODULE = 'img_processing'

with open(os.path.join(SOURCE_DIR, '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]
reqs = parse_requirements('requirements.txt')

setup(
    # metadata
    name=PACKAGE_NAME,
    version=version,
    description="Image Processing Module",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Yuta Ishikawa.",
    author_email="iy.24.bump.09@gmail.com",
    url="https://github.com/yuta316/img_processing",

    # options
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=reqs,
    extras_require={
        'dev': [
            'pytest>=3',
        ],
    },
    entry_points='''
        [console_scripts]
        {app}={src}.{main}:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), src=SOURCE_DIR, main=MAIN_MODULE),
)
