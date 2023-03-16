import os
from model.init_db import db, url

SECRET_KEY = 'hirayamnl'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = url

SQLALCHEMY_TRACK_MODIFICATIONS = False

SESSION_PERMANENT = True

SESSION_TYPE = 'sqlalchemy'

SESSION_SQLALCHEMY = db

JSON_SORT_KEYS = False