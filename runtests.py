#!/usr/bin/env python
from django.conf import settings
from django.test.utils import setup_test_environment
import django
from django.core.management import call_command

settings.configure(
    INSTALLED_APPS=('typedmodels',),
    MIDDLEWARE_CLASSES=(),
    DATABASES={
        'default': {'ENGINE': 'django.db.backends.sqlite3'}
    })

setup_test_environment()

if django.VERSION > (1, 7):
    django.setup()

call_command('test', 'typedmodels')
