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
        return f"{self}"

def create_table():
    db.create_all()
    db.session.commit()

def login_user(username, password):
    status = "Login Failed."
    system_msg = "SYSTEM: Account not found in database."
    for x in User.query.all():
        if x.username == username and x.password == password:
            system_msg = "SYSTEM: Account found in database."
            status = f"Login Successful. Welcome {x.first_name} {x.last_name}!"
            break
            
    print(system_msg)

    return status
 
def register_user(email, username, password, first_name, last_name, verified, archived):
    status = "Registration Successful."
    user = User(email=email, username=username, password=password, first_name=first_name,
                           last_name=last_name, verified=verified, archived=archived)

    for x in User.query.all():
        if email == x.email or username == x.username:
            add_user = False
            status = "Registration Failed."
            print("SYSTEM: Account already existing in database.")
            break
        else:
            add_user = True
    
    if add_user == True:
        db.session.add(user)
        db.session.commit()
        print("SYSTEM: Account inserted in database.")

    return status