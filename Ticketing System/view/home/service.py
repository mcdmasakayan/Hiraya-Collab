from flask import request, jsonify
from model.machine import db
from model.machine import Project as projects, Task as tasks, Subtask as subtasks
from view.login.service import Client

class Board:
    active = 0
    name = ""

class Activity:
    active = 0
    name = ""

class Todo:
    active = 0
    name = ""

class Message:
    error = "SYSTEM: An error has occurred."
    login_not = "SYSTEM: Must login first."
    logout_in = "SYSTEM: Logout successful."
    logout_out = "SYSTEM: You are not logged in."
    project_exist = "SYSTEM: Project inserted in database."
    project_not = "SYSTEM: Project not inserted in database."
    project_in = "SYSTEM: Project opened."
    project_out = "SYSTEM: Project not opened."
    task_exist = "SYSTEM: Task inserted in database."
    task_not = "SYSTEM: Task not inserted in database."
    task_in = "SYSTEM: Task opened."
    task_out = "SYSTEM: Task not opened."
    subtask_exist = "SYSTEM: Subtask inserted in database."
    subtask_not = "SYSTEM Subtask not inserted in database."
    subtask_in = "SYSTEM: Subtask opened."
    subtask_out = "SYSTEM: Subtask not opened."

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

            project = projects(name=name, user_id=Client.active, description=description, to_do=True, in_progress=False,
                            for_checking=False, done=False, archived=False)

            if (bool(projects.query.filter_by(user_id=Client.active).all()) == False):
                    db.session.add(project)
                    db.session.commit()
                    state = 1
                    msg = Message.project_exist
                    Board.name = project.name
            else:
                for x in projects.query.filter_by(user_id=Client.active).all():
                    if (name == x.name):
                        state = 0
                        msg = Message.project_not
                        break 
                    else:
                        db.session.add(project)
                        db.session.commit()
                        state = 1
                        msg = Message.project_exist
                        Board.name = project.name

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

            if(bool(projects.query.filter_by(user_id=Client.active).all()) == False):
                state = 0
                msg = Message.project_out

            else:
                for x in projects.query.filter_by(user_id=Client.active).all():
                    if (name == x.name):
                        state = 1
                        msg = Message.project_in
                        Board.active = x._id
                        Board.name = x.name
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

    content = {task.name:task.description for task in tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'project_opened':Board.name,
                    'tasks':content})

def tcreate_logic():
    if bool(Board.active):
        try:
            name = request.args.get('name')
            description = request.args.get('description')

            task = tasks(name=name, user_id=Client.active, project_id=Board.active, description=description, to_do=True, in_progress=False,
                            for_checking=False, done=False, archived=False)

            if (bool(tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()) == False):
                    db.session.add(task)
                    db.session.commit()
                    state = 1
                    msg = Message.task_exist
                    Activity.name = task.name
            else:
                for x in tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all():
                    if (name == x.name):
                        state = 0
                        msg = Message.task_not
                        break
                    else:
                        db.session.add(task)
                        db.session.commit()
                        state = 1
                        msg = Message.task_exist
                        Activity.name = task.name

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
    if bool(Client.active):
        try:
            name = request.args.get('name')

            if(bool(tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()) == False):
                state = 0
                msg = Message.task_out

            else:
                for x in tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all():
                    if (name == x.name):
                        state = 1
                        msg = Message.task_in
                        Activity.active = x._id
                        Activity.name = x.name
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

    content = {subtask.name:subtask.description for subtask in subtasks.query.filter_by(
                user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'subtasks':content})

def screate_logic():
    if bool(Activity.active):
        try:
            name = request.args.get('name')
            description = request.args.get('description')

            subtask = subtasks(name=name, user_id=Client.active,
                               task_id=Activity.active, description=description, to_do=True, 
                               in_progress=False, for_checking=False, done=False, archived=False)

            if (bool(subtasks.query.filter_by(user_id=Client.active,
                                              task_id=Activity.active).all()) == False):
                    db.session.add(subtask)
                    db.session.commit()
                    state = 1
                    msg = Message.subtask_exist
                    Todo.name = subtask.name
            else:
                for x in subtasks.query.filter_by(user_id=Client.active,
                                                  task_id=Activity.active).all():
                    if (name == x.name):
                        state = 0
                        msg = Message.subtask_out
                        break
                    else:
                        db.session.add(subtask)
                        db.session.commit()
                        state = 1
                        msg = Message.subtask_exist
                        Todo.name = subtask.name

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
    else:
        state = 0
        msg = Message.task_out
        Todo.name = ""
    
    content = {subtask.name:subtask.description for subtask in subtasks.query.filter_by(
               user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'created_subtask':Todo.name,
                    'subtasks':content})

def sopen_logic():
    if bool(Client.active):
        try:
            name = request.args.get('name')

            if(bool(subtasks.query.filter_by(user_id=Client.active,
                                             task_id=Activity.active).all()) == False):
                state = 0
                msg = Message.subtask_out

            else:
                for x in subtasks.query.filter_by(user_id=Client.active,
                                                  task_id=Activity.active).all():
                    if (name == x.name):
                        state = 1
                        msg = Message.subtask_in
                        Todo.name = x.name
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

    content = {item.name:item.description for item in subtasks.query.filter_by(
                user_id=Client.active, task_id=Activity.active).all()}

    return jsonify({'state':state,
                    'message':msg,
                    'username':Client.username,
                    'opened_project':Board.name,
                    'opened_task':Activity.name,
                    'opened_subtask':Todo.name,
                    'subtasks':content})