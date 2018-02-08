# -*- coding: utf8 -*-
import os
import re

from settings_local import *

def set_boolean(env_value):
   return bool(re.match(r'yes|true|t', env_value, re.IGNORECASE))

# Do not set these to True on a public facing website.
# Doing so will disclose all secrets set by the config!
DEBUG = False
ENABLE_DEBUG_TOOLBAR = False

## webserver host and port
# Actually, this is served by NGINX proxying to a uWSGI domain socket.
# So setting these doesn't affect how server is reached.
#HOST = '0.0.0.0'
#PORT = 5000

SECRET = os.environ.get('PYBOSSA_SECRET', 'foobar')
SECRET_KEY = os.environ.get('PYBOSSA_SESSION_SECRET', 'my-session-secret')

SQLALCHEMY_DATABASE_URI = os.environ.get('PYBOSSA_DATABASE_URL',
                          'postgresql://pybossa:tester@localhost/pybossa')

ITSDANGEROUSKEY = os.environ.get('PYBOSSA_ITSDANGEROUS_SECRET', 'its-dangerous-key')

BRAND = os.environ.get('PYBOSSA_BRAND', 'PyBossa')
TITLE = os.environ.get('PYBOSSA_TITLE', 'PyBossa')
LOGO = os.environ.get('PYBOSSA_LOGO', 'default_logo.svg')

TERMSOFUSE = os.environ.get('PYBOSSA_TERMSOFUSE', 'http://okfn.org/terms-of-use/')
DATAUSE = os.environ.get('PYBOSSA_DATAUSE', 'http://opendatacommons.org/licenses/by/')

# Only seems to be used in account_validation.html template
CONTACT_EMAIL = os.environ.get('PYBOSSA_CONTACT_EMAIL', 'info@pybossa.com')
# Templates still hard-coded with twitter.com/PyBossa as of v2.7.0
CONTACT_TWITTER = os.environ.get('PYBOSSA_CONTACT_TWITTER', 'PyBossa')

## External Auth providers
# GOOGLE_CLIENT_ID=''
# GOOGLE_CLIENT_SECRET=''

## list of administrator emails to which error emails get sent
# Use space, semi-colon, or comma to separate
admin_emails = os.environ.get('PYBOSSA_ADMIN_EMAILS', '')
ADMINS = re.split(r'[ ;,]+', admin_emails)

## set path to enable
# LOG_FILE = '/path/to/log/file'
## Optional log level
# import logging
# LOG_LEVEL = logging.DEBUG

## Mail setup (see https://pythonhosted.org/Flask-Mail/)
MAIL_SERVER = os.environ.get('PYBOSSA_MAIL_SERVER', 'localhost')
MAIL_PORT = int(os.environ.get('PYBOSSA_MAIL_PORT', 25))
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('PYBOSSA_MAIL_USERNAME', None)
MAIL_PASSWORD = os.environ.get('PYBOSSA_MAIL_PASSWORD', None)
MAIL_DEFAULT_SENDER = os.environ.get('PYBOSSA_MAIL_DEFAULT_SENDER', 'PyBossa Support <info@pybossa.com>')

# Unused Pybossa setting?
MAIL_FAIL_SILENTLY = False

# Disable new account confirmation (via email)
ACCOUNT_CONFIRMATION_DISABLED = set_boolean(os.environ.get('PYBOSSA_ACCOUNT_CONFIRMATION_DISABLED', 'True'))

# When a PYBOSSA project publishes a blog post, users will get an email.
# You can disable this behavior with the following flag:
DISABLE_EMAIL_NOTIFICATIONS = set_boolean(os.environ.get('PYBOSSA_DISABLE_EMAIL_NOTIFICATIONS', 'True'))

# Send emails weekly update every
WEEKLY_UPDATE_STATS = os.environ.get('PYBOSSA_WEEKLY_UPDATE_STATS', 'Sunday')

## Announcement messages
## Use any combination of the next type of messages: root, user, and app owners
## ANNOUNCEMENT = {'admin': 'Root Message', 'user': 'User Message', 'owner': 'Owner Message'}

## Enforce Privacy Mode, by default is disabled
## This config variable will disable all related user pages except for admins
## Stats, top users, leaderboard, etc
ENFORCE_PRIVACY = set_boolean(os.environ.get('PYBOSSA_ENFORCE_PRIVACY', 'True'))

## If you want to use the local uploader configure which folder
UPLOAD_METHOD = 'local'
UPLOAD_FOLDER = os.environ.get('PYBOSSA_UPLOAD_FOLDER', 'uploads')

# Expiration time for password protected project cookies in seconds
PASSWD_COOKIE_TIMEOUT = 60 * 60 * 24

# Add here any other ATOM feed that you want to get notified.
NEWS_URL = []

# Email notifications for background jobs.
FAILED_JOBS_MAILS = 7
FAILED_JOBS_RETRIES = 3

# Mailchimp API key
# MAILCHIMP_API_KEY = "your-key"
# MAILCHIMP_LIST_ID = "your-list-ID"

# Enable two factor authentication
# ENABLE_TWO_FACTOR_AUTH = True

# Strong password policy for user accounts
# ENABLE_STRONG_PASSWORD = True

# Create new leaderboards based on info field keys from user
# LEADERBOARDS = ['foo', 'bar']

# Unpublish inactive projects
UNPUBLISH_PROJECTS = set_boolean(os.environ.get('PYBOSSA_UNPUBLISH_PROJECTS', 'True'))

# Use this config variable to create valid URLs for your SPA
# SPA_SERVER_NAME = 'https://yourserver.com'

# IGNORE_FLAT_KEYS = [ 'geojson', 'key1', ...]

# Specify which key from the info field of task, task_run or result is going to be used as the root key
# for exporting in CSV format
# TASK_CSV_EXPORT_INFO_KEY = 'key'
# TASK_RUN_CSV_EXPORT_INFO_KEY = 'key2'
# RESULT_CSV_EXPORT_INFO_KEY = 'key3'
