# -*- coding: utf8 -*-
import os

from settings_local import *

SECRET = os.environ.get('PYBOSSA_SECRET', 'foobar')
SECRET_KEY = os.environ.get('PYBOSSA_SESSION_SECRET', 'my-session-secret')

SQLALCHEMY_DATABASE_URI = os.environ.get('PYBOSSA_DATABASE_URL',
                          'postgresql://pybossa:tester@localhost/pybossa')

ITSDANGEROUSKEY = os.environ.get('PYBOSSA_ITSDANGEROUS_SECRET', 'its-dangerous-key')

BRAND = os.environ.get('PYBOSSA_BRAND', 'PyBossa')
TITLE = os.environ.get('PYBOSSA_TITLE', 'PyBossa')
LOGO = os.environ.get('PYBOSSA_LOGO', 'default_logo.svg')

COPYRIGHT = 'Set Your Institution'
DESCRIPTION = 'Set the description in your config'
TERMSOFUSE = 'http://okfn.org/terms-of-use/'
DATAUSE = 'http://opendatacommons.org/licenses/by/'
CONTACT_EMAIL = 'info@pybossa.com'
CONTACT_TWITTER = 'PyBossa'
