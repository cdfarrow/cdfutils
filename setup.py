# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='cdfutils',
    version='1.0.2',
    description='General utility library of miscellaneous functions and classes',
    long_description=readme,
    author='Craig Farrow',
    author_email='cdfkiwi@gmail.com',
    url='https://github.com/cdfarrow/cdfutils',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'configparser',
    ],
)
