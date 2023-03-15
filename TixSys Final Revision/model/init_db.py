from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

url = 'mysql://root:root@localhost/tixsys'
db = SQLAlchemy()

engine = create_engine(url, echo = True)

if not database_exists(engine.url):
    create_database(engine.url)