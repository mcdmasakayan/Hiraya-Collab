from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask import json, jsonify

db = SQLAlchemy()
engine = create_engine('mysql://root:@localhost/tixsys', echo = True)

if not database_exists(engine.url):
    create_database(engine.url)

cursor = engine.connect()
content = {}
users = []

class User(db.Model):    
    __tablename__ = 'tixsys_accounts'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    username = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    first_name = db.Column(db.VARCHAR(255), nullable=False)
    last_name = db.Column(db.VARCHAR(255), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        all_data = (f"[{self._id}, {self.email}, {self.username}, {self.password}, " + 
                    f"{self.first_name}, {self.last_name}, {self.verified}, {self.archived}]")
        return all_data
    
    def get_users(self):
        for x in User.query.all():
            content = {
                'id': x._id,
                'email': x.email,
                'username': x.username,
                'password': x.password,
                'firstname': x.first_name,
                'lastname': x.last_name,
                'verified': x.verified,
                'archived': x.archived
            }
            users.append(content)
            content = {}
        print(json.dumps(users))
        return jsonify(users)