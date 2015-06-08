#!/usr/bin/env python

from distutils.core import setup

setup(
    name = 'unblog',
    version = '0.0.1',
    author = 'Leon du Toit',
    author_email = 'dutoit.leon@gmail.com',
    packages = ['unblog'],
    url = 'https://github.com/leondutoit/unblog',
    license = 'LICENSE',
    description = 'unblog your blog',
    long_description = open('README.md').read(),
    install_requires = [
        "pytumblr = 0.0.6",
        "bs4 = 4.3.2"
    ],
)
