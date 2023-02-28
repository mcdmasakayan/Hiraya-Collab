from flask import request, session, jsonify
from model.machine import db, User as users
from view.functions.sys import hash_string, get_users

def index_logic():
    return get_users()

def login_logic():
    try:
        username = request.args.get('username')
        password = request.args.get('password')
        pw_hash = hash_string(password)

        if (bool(users.query.all()) == False):
            auth = 0
            msg = "SYSTEM: Account not found in database."
        else:
            for x in users.query.all():
                if x.username == username and x.password == pw_hash:
                    session['active_user'] = x._id
                    auth = 1
                    msg = "SYSTEM: Account found in database."
                    break
                else:
                    auth = 0
                    msg = "SYSTEM: Account not found in database."

    except (UnboundLocalError, AttributeError):
        auth = 0
        msg = "SYSTEM: An error has occurred."

    return jsonify({"auth":auth,
                    "message":msg})

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
            msg = "SYSTEM: Account inserted in database."
        else:
            for x in users.query.all():
                if (email == x.email or username == x.username):
                    auth = 0
                    msg = "SYSTEM: Account not inserted in database. (Account already existing)"
                    break 
                else:
                    auth = 1
                    msg = "SYSTEM: Account inserted in database."
                
    except (UnboundLocalError, AttributeError):
        auth = 0
        msg = "SYSTEM: An error has occurred."

    return jsonify({"auth":auth,
                    "message":msg})