from flask import request, jsonify
from model.machine import db
from model.machine import Project as projects, Task as tasks, Subtask as subtasks
from view.login.service import Client
from view.functions.sys import add_entity, open_entity, move_task
from view.functions.msg import Message
from view.functions.entities import Client, Board, Activity, Todo

def logout_logic():
    if bool(Client.active):
        Client.active = 0
        auth = 0
        msg = Message.logout_in
    else:
        auth = 0
        msg = Message.logout_out
    
    return jsonify({'auth':auth,
                    'message':msg,
                    'first_name':Client.first_name,
                    'last_name':Client.last_name,
                    'username':Client.username})

def pcreate_logic():
    if bool(Client.active):
        try:
            name = request.args.get('name')
            description = request.args.get('description')
            
            project = projects(name=name, user_id=Client.active, description=description, progress=0, archived=False)
            table = projects.query.filter_by(user_id=Client.active).all()

            if (bool(table) == False):
                    auth, state, msg = add_entity(table, project)
            else:
                for x in projects.query.filter_by(user_id=Client.active).all():
                    if (name == x.name):
                        state = 0
                        msg = Message.project_not
                        break 
                    else:
                        auth, state, msg = add_entity(table, project)
                        

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
    else:
        state = 0
        msg = Message.login_not
        Board.name = ""

    content = {project.name:project.description for project in projects.query.filter_by(user_id=Client.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'first_name':Client.first_name,
                    'last_name':Client.last_name,
                    'username':Client.username,
                    'created_project':Board.name,
                    'projects': content})

def popen_logic():
    if bool(Client.active):
        try:
            name = request.args.get('name')
            table = projects.query.filter_by(user_id=Client.active).all()
            
            if(bool(table) == False):
                state = 0
                msg = Message.project_out

            else:
                for x in table:
                    if (name == x.name):
                        auth, state, msg = open_entity(table, x)
                        description = x.description
                        break
                    else:
                        state = 0
                        msg = Message.project_out

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
 
    else:
        state = 0
        msg = Message.login_not
        Board.active = 0
        Board.name = ""

    content = {task.name:Activity.status[int(task.progress)] for task in tasks.query.filter_by(
               user_id=Client.active, project_id=Board.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'project_opened':Board.name,
                    'description':description,
                    'tasks':content})

def tcreate_logic():
    if bool(Board.active):
        try:
            name = request.args.get('name')
            description = request.args.get('description')
            
            task = tasks(name=name, user_id=Client.active, project_id=Board.active, description=description, progress=0, attachments=None,archived=False)
            table = tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()

            if (bool(table) == False):
                    auth, state, msg = add_entity(table, task)
            else:
                for x in table:
                    if (name == x.name):
                        state = 0
                        msg = Message.task_not
                        break
                    else:
                        auth, state, msg = add_entity(table, task)

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
    else:
        state = 0
        msg = Message.project_out
        Activity.name = ""
    
    content = {subtask.name:subtask.description for subtask in subtasks.query.filter_by(
                user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'created_task':Activity.name,
                    'subtasks':content})

def topen_logic():
    if bool(Board.active):
        try:
            name = request.args.get('name')
            table = tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()

            if(bool(tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()) == False):
                state = 0
                msg = Message.task_out

            else:
                for x in table:
                    if (name == x.name):
                        auth, state, msg = open_entity(table, x)
                        description = x.description
                        break
                    else:
                        state = 0
                        msg = Message.task_out

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
 
    else:
        state = 0
        msg = Message.project_not
        Activity.active = 0
        Activity.name = ""

    content = {subtask.name:Todo.status[int(subtask.progress)] for subtask in subtasks.query.filter_by(
               user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'description':description,
                    'subtasks':content})

def tmove_logic():
    if bool(Board.active):
        try:
            name = request.args.get('name')
            progress = request.args.get('progress')
            table = tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()
            for x in table:
                if (name == x.name):
                    auth, state, msg = move_task(x, progress)
                    description = x.description
                    break
                else:
                    state = 0
                    msg = Message.task_out

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
 
    else:
        state = 0
        msg = Message.project_not
        Activity.active = 0
        Activity.name = ""

    content = {task.name:Activity.status[int(task.progress)] for task in tasks.query.filter_by(
               user_id=Client.active, project_id=Board.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'project_opened':Board.name,
                    'description':description,
                    'tasks':content})

def screate_logic():
    if bool(Activity.active):
        try:
            name = request.args.get('name')
            description = request.args.get('description')

            subtask = subtasks(name=name, user_id=Client.active,
                               task_id=Activity.active, description=description, progress=0, archived=False)
            table = subtasks.query.filter_by(user_id=Client.active, task_id=Activity.active).all()

            if (bool(table) == False):
                auth, state, msg = add_entity(table, subtask)    
            else:
                for x in subtasks.query.filter_by(user_id=Client.active,
                                                  task_id=Activity.active).all():
                    if (name == x.name):
                        state = 0
                        msg = Message.subtask_out
                        desc = x.description
                        break
                    else:
                        auth, state, msg = add_entity(table, subtask)

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
    else:
        state = 0
        msg = Message.task_out
        Todo.name = ""
    
    content = {subtask.name:Todo.status[int(subtask.progress)] for subtask in subtasks.query.filter_by(
               user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'created_subtask':Todo.name,
                    'description':desc,
                    'subtasks':content})

def sopen_logic():
    if bool(Activity.active):
        try:
            name = request.args.get('name')
            table = subtasks.query.filter_by(user_id=Client.active, task_id=Activity.active).all()
            
            if(bool(table) == False):
                state = 0
                msg = Message.subtask_out

            else:
                for x in table:
                    if (name == x.name):
                        auth, state, msg = open_entity(table, x)
                        description = x.description
                        break
                    else:
                        state = 0
                        msg = Message.subtask_out

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
 
    else:
        state = 0
        msg = Message.task_out

    content = {item.name:Todo.status[int(item.progress)] for item in subtasks.query.filter_by(
                user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'opened_subtask':Todo.name,
                    'description':description,
                    'subtasks':content})

def smove_logic():
    if bool(Activity.active):
        try:
            name = request.args.get('name')
            progress = request.args.get('progress')
            table = subtasks.query.filter_by(user_id=Client.active, task_id=Activity.active).all()
            for x in table:
                if (name == x.name):
                    auth, state, msg = move_task(x, progress)
                    description = x.description
                    break
                else:
                    state = 0
                    msg = Message.subtask_out

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
 
    else:
        state = 0
        msg = Message.subtask_not
       
    content = {subtask.name:Todo.status[int(subtask.progress)] for subtask in subtasks.query.filter_by(
               user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'description':description,
                    'subtasks':content})