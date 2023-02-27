from model.database.machine import User, db, users
from flask import json
import hashlib

def login_user(username, password):
    status = "Login Failed."
    system_msg = "SYSTEM: Account not found in database."
    p_hash = hashlib.md5(password.encode()).hexdigest()

    for x in User.query.all():
        if x.username == username and x.password == p_hash:
            system_msg = "SYSTEM: Account found in database."
            status = f"Login Successful. Welcome {x.first_name} {x.last_name}!"
            break
    print(system_msg)
    
    return status
 
def register_user(email, username, password, first_name, last_name, verified, archived):
    status = "Registration Successful."
    add_user = False
    p_hash = hashlib.md5(password.encode()).hexdigest()
   
    user = User(email=email, username=username, password=p_hash, first_name=first_name,
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
        get_users()

    return status

def get_users():
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