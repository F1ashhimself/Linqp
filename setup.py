# -*- coding: utf-8 -*-

#    Copyright (c) 2018 Max Biloborodko.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

__author__ = 'f1ashhimself@gmail.com'

from os import path

from setuptools import setup


def package_env(file_name, strict=False):
    file_path = path.join(path.dirname(__file__), file_name)
    if path.exists(file_path) or strict:
        return open(file_path).read()
    else:
        return ''


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


if __name__ == '__main__':
    setup(
        name='Linqp',
        version='1.0.1',
        description='Simple LINQ implementation for python.',
        long_description=package_env('README.rst'),
        author='Max Biloborodko',
        author_email='f1ashhimself@gmail.net',
        packages=['linqp'],
        include_package_data=True,
        install_requires=[],
        zip_safe=False,
        entry_points={}
    )
