from flask import request, jsonify
from uuid import uuid4
from model.init_db import db
from model.project.data import Project
from model.task.data import Task
from model.subtask.data import Subtask
from middleware.session import check_session

def create_subtask(kwarg):
    user_id = check_session()

    if not user_id:
        return jsonify({'message':'User not logged in.'})
    
    project = Project.query.filter_by(user_id=user_id, name=kwarg['project_name'], archived=False).first()
    task = Task.query.filter_by(project_id=project.public_id, name=kwarg['task_name'], archived=False).first()

    data = request.get_json()
    
    if 'project_id' in data and project and task:
        task = Task.query.filter_by(public_id=data['task_id'], project_id=project.public_id, archived=False).first()
        subtasks = Subtask.query.filter_by(task_id=task.public_id, archived=False).all()
        
        description = ''

        if 'name' in data:
            for subtask in subtasks:
                if data['name'] == subtask.name:
                    return jsonify({'message':'Subtask name already exists. Subtask not created.'})
            
            if 'description' in data:
                description = data['description']

            subtask = Subtask(public_id=str(uuid4()),
                        task_id=task.public_id,
                        name=data['name'],
                        description=description,
                        priority_level=0,
                        done=False,
                        archived=False)
        
            db.session.add(subtask)
            db.session.commit()

            return jsonify({'message':'Subtask created.'})

    return jsonify({'message':'Subtask not created.'})