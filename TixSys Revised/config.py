import os
from model.data import db

SECRET_KEY = 'hirayamnl'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/tixsys'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SESSION_PERMANENT = False

SESSION_TYPE = 'sqlalchemy'

SESSION_SQLALCHEMY = db

JSON_SORT_KEYS = False