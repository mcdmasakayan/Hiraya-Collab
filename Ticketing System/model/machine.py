import hashlib
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()
engine = create_engine('mysql://root:root@localhost/tixsys', echo = True)

if not database_exists(engine.url):
    create_database(engine.url)

cursor = engine.connect()
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

def login_user(username, password):
    status = "Login Failed."
    system_msg = "SYSTEM: Account not found in database."

    pw_hash = hashlib.md5(password.encode()).hexdigest()

    for x in User.query.all():
        if x.username == username and x.password == pw_hash:
            system_msg = "SYSTEM: Account found in database."
            status = f"Login Successful. Welcome {x.first_name} {x.last_name}!"
            break

    print(system_msg)

    return status
 
def register_user(email, username, password, first_name, last_name, verified, archived):
    status = "Registration Successful."
    add_user = False
    pw_hash = hashlib.md5(password.encode()).hexdigest()

    user = User(email=email, username=username, password=pw_hash, first_name=first_name,
                           last_name=last_name, verified=verified, archived=archived)

    for x in User.query.all():
        if email == x.email or username == x.username:
            add_user = False
            status = "Registration Failed."
            print("SYSTEM: Account already existing in database.")
            break
        else:
            add_user = True

    if add_user == True or bool(User.query.all()) == False:
        db.session.add(user)
        db.session.commit()
        print("SYSTEM: Account inserted in database.")

    return status