from datetime import datetime
from model.init_db import db
from model.project.data import Project

class User(db.Model):
    __tablename__ = 'users'
    _id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    email = db.Column(db.VARCHAR(255))
    username = db.Column(db.VARCHAR(255))
    password = db.Column(db.VARCHAR(255))
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    verified = db.Column(db.Boolean)
    archived = db.Column(db.Boolean)
    projects = db.relationship(Project, backref='user') 