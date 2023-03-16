from flask import request, jsonify
from uuid import uuid4
from model.variables import Message
from model.init_db import db
from model.project.data import Project
from model.task.data import Task
from model.subtask.data import Subtask
from middleware.session import check_session

def create_task(kwarg):
    user_id = check_session()

    if not user_id:
        return jsonify({'message':Message.not_logged_in})
    
    project = Project.query.filter_by(user_id=user_id, name=kwarg['project_name'], archived=False).first()

    data = request.get_json()
    
    if 'project_id' in data and project:
        project = Project.query.filter_by(public_id=data['project_id'], user_id=user_id, archived=False).first()
        tasks = Task.query.filter_by(project_id=project.public_id, archived=False).all()
        
        description = ''

        if 'name' in data:
            for task in tasks:
                if data['name'] == task.name:
                    return jsonify({'message':Message.task_exists})
            
            if 'description' in data:
                description = data['description']

            task = Task(public_id=str(uuid4()),
                        project_id=project.public_id,
                        name=data['name'],
                        description=description,
                        priority_level=0,
                        progress='In Progress',
                        archived=False)
        
            db.session.add(task)
            db.session.commit()

            return jsonify({'message':Message.task_created})

    return jsonify({'message':Message.task_not_created})

def get_task_data(kwarg):
    user_id = check_session()

    if not user_id:
        return jsonify({'message':Message.not_logged_in})
    
    project = Project.query.filter_by(user_id=user_id, name=kwarg['project_name'], archived=False).first()
    task = Task.query.filter_by(project_id=project.public_id, name=kwarg['task_name'], archived=False).first()
    data = request.get_json()

    if 'project_id' in data and project and task:
        subtasks = Subtask.query.filter_by(task_id=data['task_id'], archived=False).all()

        task_data = {'public_id':task.public_id,
                     'name':task.name,
                     'description':task.description,
                     'subtasks':[{'public_id':subtask.public_id,
                                  'name':subtask.name,
                                  'description':subtask.description,
                                  'done':subtask.done} for subtask in subtasks]}
        
        return jsonify({'task_data':task_data})
    
    return jsonify({'message':Message.task_not_opened})