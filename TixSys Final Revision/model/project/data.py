from datetime import datetime
from model.init_db import db
from model.task.data import Task

class Project(db.Model):
    __tablename__ = 'projects'
    _id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.public_id'))
    name = db.Column(db.VARCHAR(255))
    description = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    archived = db.Column(db.Boolean)
    tasks = db.relationship(Task, backref='project')