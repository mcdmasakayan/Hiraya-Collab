from flask import request, jsonify
from model.machine import db, Project as projects, Task as tasks
from view.login.service import Client

class Board:
    active = 0

class Message:
    login_not = "SYSTEM: Must login first."
    logout_in = "SYSTEM: Logout successful."
    logout_out = "SYSTEM: You are not logged in."
    project_exist = "SYSTEM: Project inserted in database."
    project_not = "SYSTEM: Project not inserted in database."
    project_in = "SYSTEM: Project opened."
    project_out = "SYSTEM: Project not opened."
    task_in = "SYSTEM: Task inserted in database."
    task_out = "SYSTEM: Task not inserted in database."
    subtask_in = ""
    subtask_out = ""

def logout_logic():
    if bool(Client.active):
        Client.active = 0
        auth = 0
        msg = Message.logout_in
    else:
        auth = 0
        msg = Message.logout_out
    
    return jsonify({'auth':auth,
                    'message':msg})

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

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
    else:
        state = 0
        msg = Message.login_not

    content = [y.name for y in projects.query.filter_by(user_id=Client.active).all()]

    return jsonify({'state':state,
                    'message':msg,
                    'project_data': content})

def popen_logic():
    if bool(Client.active):
        try:
            name = request.args.get('name')

            if(bool(projects.query.filter_by(user_id=Client.active).all()) == False):
                state = 0
                msg = Message.project_out
                Board.active = 0

            else:
                for x in projects.query.filter_by(user_id=Client.active).all():
                    if (name == x.name):
                        state = 1
                        msg = Message.project_in
                        Board.active = x._id
                        break
                    else:
                        state = 0
                        msg = Message.project_out
                        Board.active = 0

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
            Board.active = 0
 
    else:
        state = 0
        msg = Message.login_not
        Client.active = 0

    content = [y.name for y in tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all()]

    return jsonify({'state':state,
                    'message':msg,
                    'task_data':content})

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
                    msg = Message.task_in
            else:
                for x in tasks.query.filter_by(user_id=Client.active, project_id=Board.active).all():
                    if (name == x.name):
                        state = 0
                        msg = Message.task_out
                        break
                    else:
                        db.session.add(task)
                        db.session.commit()
                        state = 1
                        msg = Message.task_in

        except (UnboundLocalError, AttributeError):
            state = 0
            msg = Message.error
    else:
        state = 0
        msg = Message.project_out
        Board.active = 0
    
    return jsonify({'state':state,
                    'message':msg})

def topen_logic():
    pass