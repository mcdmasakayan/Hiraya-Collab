from flask import request, session, jsonify
from model.machine import db, User as users, Project as projects
from view.functions.sys import hash_string, get_users

class Client:
    active = 0

class Message:
    error = "SYSTEM: An error has occurred."
    login_in = "SYSTEM: Login successful."
    login_out = "SYSTEM: Login failed."
    register_in = "SYSTEM: Account inserted in database."
    register_out = "SYSTEM: Account not inserted in database."

def index_logic():
    return get_users()

def login_logic():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        pw_hash = hash_string(password)

        if (bool(users.query.all()) == False):
            auth = 0
            msg = Message.login_out
            Client.active = 0
        else:
            for x in users.query.all():
                if x.username == username and x.password == pw_hash:
                    session['active_user'] = x._id
                    Client.active = session.get('active_user')
                    auth = 1
                    msg = Message.login_in
                    break
                else:
                    auth = 0
                    msg = Message.login_out
                    Client.active = 0

    except (UnboundLocalError, AttributeError):
        auth = 0
        msg = Message.error
        Client.active = 0

    content = [y.name for y in projects.query.filter_by(user_id=Client.active).all()]

    return jsonify({"auth":auth,
                    "message":msg,
                    "project_data":content})

def register_logic():
    try:
        email = request.args.get('email')
        username = request.args.get('username')
        password = request.args.get('password')
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        pw_hash = hash_string(password)
        user = users(email=email, username=username, password=pw_hash, first_name=first_name,
                            last_name=last_name, verified=False, archived=False)

        if (bool(users.query.all()) == False):
            db.session.add(user)
            db.session.commit()
            auth = 1
            msg = Message.register_in
        else:
            for x in users.query.all():
                if (email == x.email or username == x.username):
                    auth = 0
                    msg = Message.register_out
                    break 
                else:
                    db.session.add(user)
                    db.session.commit()
                    auth = 1
                    msg = Message.register_in
                
    except (UnboundLocalError, AttributeError):
        auth = 0
        msg = Message.error

    return jsonify({"auth":auth,
                    "message":msg})