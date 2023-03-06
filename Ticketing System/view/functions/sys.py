import hashlib
from flask import request, jsonify
from model.machine import db, User as users, Project as projects, Task as tasks, Subtask as subtasks
from view.functions.msg import Message
from view.functions.entities import Client, Board, Activity, Todo

def hash_string(str):
    hash_str = hashlib.md5(str.encode()).hexdigest()

    return hash_str

def login_creds():
    username = request.args.get('username')
    password = request.args.get('password')
    pw_hash = hash_string(password)

    return username, pw_hash

def register_creds():
    email = request.args.get('email')
    username = request.args.get('username')
    password = request.args.get('password')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    pw_hash = hash_string(password)

    return email, username, first_name, last_name, pw_hash

def get_users():
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

def add_entity(table, entity):
    auth = 1
    state = 1

    if table == users.query.all():
        msg = Message.register_in
        Client.username = entity.username
    
    elif table == projects.query.filter_by(user_id=Client.active).all():
        msg = Message.project_exist
        Board.name = entity.name
    
    elif table == tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all():
        msg = Message.task_exist
        Activity.name = entity.name

    elif table == subtasks.query.filter_by(user_id=Client.active, task_id=Activity.active).all():
        msg = Message.subtask_exist
        Todo.name = entity.name
    
    db.session.add(entity)
    db.session.commit()

    return auth, state, msg

def open_entity(table, row):
    auth = 1
    state = 1
    
    if table == users.query.all():
        Client.first_name = row.first_name
        Client.last_name = row.last_name
        Client.username = row.username
        msg = Message.login_in
    elif table == projects.query.filter_by(user_id=Client.active).all():
        msg = Message.project_in
        Board.active = row._id
        Board.name = row.name
    elif table == tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all():
        msg = Message.task_in
        Activity.active = row._id
        Activity.name = row.name
    elif table == subtasks.query.filter_by(user_id=Client.active, task_id=Activity.active).all():
        msg = Message.subtask_in
        Todo.name = row.name

    return auth, state, msg

def move_task(row, progress):
    progress = int(progress)

    if progress in range(0,4):
        row.progress = progress
        auth = 1
        state = 1
        
        if progress == 0:
            msg = Message.move_todo
        
        elif progress == 1:
            msg = Message.move_inprogress
        
        elif progress == 2:
            msg = Message.move_forchecking

        elif progress == 3:
            msg = Message.move_done
    
    else:
        auth = 0
        state = 0
        msg = Message.move_not
    
    return auth, state, msg