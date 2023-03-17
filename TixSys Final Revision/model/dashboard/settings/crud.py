from flask import request, jsonify
from middleware.session import check_session
from model.variables import Message
from model.init_db import db
from model.user.data import User
from model.project.data import Project
from model.task.data import Task
from model.subtask.data import Subtask

def archive_user():
    user_id = check_session()

    if not user_id:
        return jsonify({'message':Message.not_logged_in})
    
    data = request.get_json()

    if 'user_id' in data:
        user = User.query.filter_by(public_id=data['user_id'], archived=False).first()

        if user:
            projects = Project.query.filter_by(user_id=user.public_id, archived=False).all()
            
            for project in projects:
                tasks = Task.query.filter_by(project_id=project.public_id, archived=False).all()

                for task in tasks:
                    subtasks = Subtask.query.filter_by(task_id=task.public_id, archived=False).all()

                    for subtask in subtasks:
                        subtask.archived = True
                        
                    task.archived = True


                project.archived = True

            user.archived = True
            db.session.commit()

        return jsonify({'message':Message.user_archived})

    return jsonify({'message':Message.user_not_archived})