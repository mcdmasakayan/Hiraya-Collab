from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()
engine = create_engine('mysql://root:root@localhost/tixsys', echo = True)
cursor = engine.connect()
class User(db.Model):
     
    __tablename__ = 'tixsys_accounts'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.VARCHAR(255), nullable=False)
    username = db.Column(db.VARCHAR(255), nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    first_name = db.Column(db.VARCHAR(255), nullable=False)
    last_name = db.Column(db.VARCHAR(255), nullable=False)
    verified = db.Column(db.Boolean, nullable=False)
    archived = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<_id %r>' % self._id

def create_table():
    db.create_all()
    db.session.commit()

users = User()

def login_user(username, password):
    status = "Login Successful."

    if status == "Login Successful.":
        print("SYSTEM: Account found in database.")
    elif status == "Login Failed.":
        print("SYSTEM: Account not found in database.")

    return status
 
def register_user(email, username, password, first_name, last_name, verified, archived):
    user = User(email=email, username=username, password=password, first_name=first_name,
                           last_name=last_name, verified=verified, archived=archived)

    db.session.add(user)
    db.session.commit()

    print("SYSTEM: Account inserted in database.")

    return f"Registration Successful."