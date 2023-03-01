import os

SECRET_KEY = 'hirayamnl'

SESSION_PERMANENT = False

SESSION_TYPE = 'filesystem'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/tixsys'

SQLALCHEMY_TRACK_MODIFICATIONS = False

JSON_SORT_KEYS = False