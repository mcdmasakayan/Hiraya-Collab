from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InsertTable(db.Model):
    __tablename__ = 'tixsys'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Integer, primary_key=True, autoincrement=True)