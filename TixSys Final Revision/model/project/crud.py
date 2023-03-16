from flask import request, jsonify
from uuid import uuid4
from model.variables import Message
from model.init_db import db
from model.project.data import Project
from model.task.data import Task
from model.subtask.data import Subtask
from middleware.session import check_session

def create_project():
    user_id = check_session()

    if not user_id:
        return jsonify({'message':Message.not_logged_in})
    
    projects = Project.query.filter_by(user_id=user_id, archived=False).all()
    data = request.get_json()
    description = ''

    if 'name' in data:
        for project in projects:
            if data['name'] == project.name:
                return jsonify({'message':Message.project_exists})
        
        if 'description' in data:
            description = data['description']

        project = Project(public_id=str(uuid4()),
                          user_id=user_id,
                          name=data['name'],
                          description=description,
                          archived=False)
    
        db.session.add(project)
        db.session.commit()

        return jsonify({'message':Message.project_created})

    return jsonify({'message':Message.project_not_created})

def get_project_data(kwarg):
    user_id = check_session()

    if not user_id:
        return jsonify({'message':'User not logged in.'})
    
    project = Project.query.filter_by(user_id=user_id, name=kwarg['project_name'], archived=False).first()
    data = request.get_json()

    if ('project_id' in data) and project:
        project = Project.query.filter_by(public_id=data['project_id'], user_id=user_id, archived=False).first()
        tasks = Task.query.filter_by(project_id=project.public_id, archived=False).all()
        subtasks = Subtask.query.filter_by(archived=False)

        project_data = {'public_id':project.public_id,
                        'name':project.name,
                        'date_created':project.date_created,
                        'date_updated':project.date_updated,
                        'tasks':[{'public_id':task.public_id,
                                'name':task.name,
                                'description':task.description,
                                'progress':task.progress,
                                'date_created':task.date_created,
                                'date_due':task.date_due,
                                'subtasks':[{'public_id':subtask.public_id,
                                             'name':subtask.name,
                                             'done':subtask.done}
                                             for subtask in subtasks.filter_by(task_id=task.public_id)]}
                                             for task in tasks]}
        
        return jsonify({'project_data':project_data})
    
    return jsonify({'message':Message.project_not_opened})
    
def delete_project(kwarg):
    user_id = check_session()

    if not user_id:
        return jsonify({'message':Message.not_logged_in})
    
    projects = Project.query.filter_by(user_id=user_id, archived=False).all()
    data = request.get_json()

    if 'project_id' in data:
        for project in projects:
            if data['project_id'] == project.public_id:
                project.archived = True
                db.session.commit()
                break

        return jsonify({'message':Message.project_deleted})

    return jsonify({'message':Message.project_not_deleted})