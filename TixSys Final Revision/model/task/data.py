from datetime import datetime
from model.init_db import db
from model.subtask.data import Subtask

class Task(db.Model):
    __tablename__ = 'tasks'
    _id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    project_id = db.Column(db.String(50), db.ForeignKey('projects.public_id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    progress = db.Column(db.String(20))
    priority_level = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    date_due = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    archived = db.Column(db.Boolean)
    tasks = db.relationship(Subtask, backref='task')