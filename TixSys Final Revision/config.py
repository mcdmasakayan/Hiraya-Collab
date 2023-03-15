import os
from model.init_db import db, url

SECRET_KEY = 'hirayamnl'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = url

SQLALCHEMY_TRACK_MODIFICATIONS = False

PERMANENT_SESSION_LIFETIME = False

SESSION_PERMANENT = False

SESSION_TYPE = 'sqlalchemy'

SESSION_SQLALCHEMY = db

JSON_SORT_KEYS = False