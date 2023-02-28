from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

class ID:
    user = "users._id"
    project = "projects._id"
    task = "tasks._id"
    subtask = "subtasks._id"

db = SQLAlchemy()
engine = create_engine('mysql://root:root@localhost/tixsys', echo = True)

if not database_exists(engine.url):
    create_database(engine.url)

class User(db.Model):    
    __tablename__ = 'users'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    username = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    first_name = db.Column(db.VARCHAR(255), nullable=False)
    last_name = db.Column(db.VARCHAR(255), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)
    projects = db.relationship('Project', backref='user') 
class Project(db.Model):
    __tablename__ = 'projects'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(ID.user))
    name = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority_level = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    date_start = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_due = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_end = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    to_do = db.Column(db.Boolean, nullable=False)
    in_progress = db.Column(db.Boolean, nullable=False)
    for_checking = db.Column(db.Boolean, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)
    tasks = db.relationship('Task', backref='project') 
class Task(db.Model):
    __tablename__ = 'tasks'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey(ID.project))
    user_id = db.Column(db.Integer, db.ForeignKey(ID.user))
    name = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority_level = db.Column(db.Integer, autoincrement=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    date_start = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_due = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_end = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    to_do = db.Column(db.Boolean, nullable=False)
    in_progress = db.Column(db.Boolean, nullable=False)
    for_checking = db.Column(db.Boolean, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)
    subtasks = db.relationship('Subtask', backref='task') 
class Subtask(db.Model):
    __tablename__ = 'subtasks'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey(ID.task))
    user_id = db.Column(db.Integer, db.ForeignKey(ID.user))
    name = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    priority_level = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.now)
    date_start = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_due = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    date_end = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    to_do = db.Column(db.Boolean, nullable=False)
    in_progress = db.Column(db.Boolean, nullable=False)
    for_checking = db.Column(db.Boolean, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)