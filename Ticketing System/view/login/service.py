from flask import render_template, jsonify
from model.machine import db, User as users
import hashlib

def hash_string(str):
    hash_str = hashlib.md5(str.encode()).hexdigest()

    return hash_str

def index_logic():
    data = {}
    for x in users.query.all():
        data.update({x._id:{
                    'email': x.email,
                    'username': x.username,
                    'password': x.password,
                    'firstname': x.first_name,
                    'lastname': x.last_name,
                    'verified': x.verified,
                    'archived': x.archived
                }})
        
    return jsonify(data)

def login_logic(username, password):
    system_msg = "SYSTEM: Account not found in database."
    pw_hash = hash_string(password)

    for x in users.query.all():
        if x.username == username and x.password == pw_hash:
            system_msg = "SYSTEM: Account found in database."
            break

    return system_msg

def register_logic(email, username, password, first_name, last_name, verified, archived):
    add_user = False
    pw_hash = hash_string(password)
    system_msg = "SYSTEM: Account already existing in database."
    user = users(email=email, username=username, password=pw_hash, first_name=first_name,
                           last_name=last_name, verified=verified, archived=archived)

    for x in users.query.all():
        if email == x.email or username == x.username:
            add_user = False
            break 
        else:
            add_user = True

    if add_user == True or bool(users.query.all()) == False:
        db.session.add(user)
        db.session.commit()
        system_msg = "SYSTEM: Account inserted in database."
        
    return system_msg