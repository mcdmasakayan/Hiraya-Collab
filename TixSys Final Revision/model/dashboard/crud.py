from flask import jsonify
from model.user.data import User
from model.project.data import Project
from model.task.data import Task
from middleware.session import check_session

def open_dashboard():
    dashboard_data = []

    user_id = check_session()

    if not user_id:
        return jsonify({'message':'User not logged in.'})

    user = User.query.filter_by(public_id=user_id, archived=False).first()
    projects = Project.query.filter_by(user_id=user.public_id, archived=False).all()
    tasks = Task.query.join(Project.tasks).filter_by(archived=False)

    user_data = {'user':{'public_id':user.public_id,
                         'first_name':user.first_name,
                         'last_name':user.last_name}}
    project_data = {'projects':[{'public_id':project.public_id,
                                 'name':project.name,
                                 'description':project.description,
                                 'date_created':project.date_created,
                                 'date_updated':project.date_updated,
                                 'tasks':[{'public_id':task.public_id,
                                           'name':task.name,
                                           'progress':task.progress,
                                           'date_created':task.date_created,
                                           'date_due':task.date_due}
                                            for task in tasks.filter_by(project_id=project.public_id)]}
                                            for project in projects]}

    dashboard_data.append(user_data)
    dashboard_data.append(project_data)

    return jsonify({'dashboard_data':dashboard_data})