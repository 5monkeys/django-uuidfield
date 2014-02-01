# coding=utf-8
# flake8: noqa
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-uuidfield').version
except Exception as e:
    VERSION = 'unknown'

from uuidfield.fields import UUIDField
