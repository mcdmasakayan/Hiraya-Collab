from datetime import datetime
from model.init_db import db

class Subtask(db.Model):
    __tablename__ = 'subtasks'
    _id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    task_id = db.Column(db.String(50), db.ForeignKey('tasks.public_id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    priority_level = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    date_due = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    done = db.Column(db.Boolean)
    archived = db.Column(db.Boolean)