from flask import request, session, jsonify
from model.machine import db, User as users, Project as projects
from view.functions.sys import get_users, login_creds, register_creds
from view.functions.sys import add_entity, open_entity
from view.functions.msg import Message
from view.functions.entities import Client

def admin_logic():
    return get_users()

def index_logic():
    return jsonify({'msg':'Hi'})

def login_logic():
    try:
        username, pw_hash = login_creds()
        table = users.query.all()

        if (bool(table) == False):
            auth = 0
            msg = Message.login_out
            Client.active = 0
        else:
            for x in table:
                if x.username == username and x.password == pw_hash:
                    session['active_user'] = x._id
                    auth, state, msg = open_entity(table, x)
                    Client.active = session.get('active_user')
                    break
                else:
                    auth = 0
                    msg = Message.login_out
                    Client.active = 0

    except (UnboundLocalError, AttributeError):
        auth = 0
        msg = Message.error
        Client.active = 0
        Client.username = "Guest"
        Client.first_name = "Guest"
        Client.last_name = "Guest"

    content = {project.name:project.description for project in projects.query.filter_by(user_id=Client.active).all()}

    return jsonify({"auth":auth,
                    "message":msg,
                    "first_name":Client.first_name,
                    "last_name":Client.last_name,
                    "user_name":Client.username,
                    "projects":content})

def register_logic():
    try:
        email, username, first_name, last_name, pw_hash = register_creds()
        user = users(email=email, username=username, password=pw_hash, first_name=first_name,
                            last_name=last_name, verified=False, archived=False)
        table = users.query.all()

        if (bool(table) == False):
            auth, state, msg = add_entity(table, user)
        else:
            for x in table:
                if (email == x.email or username == x.username):
                    auth = 0
                    msg = Message.register_out
                    break 
                else:
                    auth, state, msg = add_entity(table, user)

    except (UnboundLocalError, AttributeError):
        auth = 0
        msg = Message.error
        Client.username = ""

    return jsonify({"auth":auth,
                    "message":msg,
                    'created_user':Client.username})