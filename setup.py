#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django-yacaptcha',
    version='0.1',
    description='Yandex captcha',
    author='Yaroslav Muravsky',
    author_email='y@myarik.com',
    url='',
    py_modules=['django', 'requests', 'xml'],
    packages=['yacaptcha', ]
)
