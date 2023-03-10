from flask import jsonify
from model.data import db, User, Project, Task, Subtask
from model.session import add_to_session
from datetime import datetime

class Progress:
    in_progress = 'In Progress'
    testing = 'Testing'
    revisions = 'Revisions'
    deployment = 'Deployment'

error_response = '<h1>Error 404 Page.</h1>'

def send_login_status(credentials):
    users = User.query.filter_by(archived=False).all()
    access = True
    active_user = User.query.filter_by(active=True, archived=False).first()
    
    if credentials == error_response:
        access = False

    if bool(active_user) == False:
        for user in users:
            if ((credentials['username'] == user.username or credentials['email'] == user.email)
                and (credentials['password'] == user.password)):
                user.active = True
                access = True
                db.session.commit()
                add_to_session(user._id)
                break
 
    data = {'access':access}

    return jsonify(data)

def send_registration_status(user_info):
    users = User.query.filter_by(archived=False).all()
    saved = True

    if user_info == error_response:
        saved = False
    
    if saved == True:
        entity = User(email=user_info['email'], username=user_info['username'],
                    password=user_info['password'], first_name=user_info['first_name'],
                    last_name=user_info['last_name'], verified=False, archived=False, active=False)
        
        for user in users:
            if user_info['username'] == user.username:
                saved = False
                break
        
        if (saved == True) or (bool(users) == False):
            saved = True
            db.session.add(entity)
            db.session.commit()

    data = {'saved':saved}
    
    return jsonify(data)

def send_dashboard_data():
    date_today = datetime.now()
    active_user = User.query.filter_by(active=True, archived=False).first()
    user_projects = Project.query.filter_by(user_id=active_user._id, archived=False).all()
    task_today = Task.query.join(Project.tasks).filter(date_today >= Task.date_due).filter_by(archived=False).all()
    tasks = Task.query.filter_by(archived=False)
    completions = {}

    for task in tasks:
        if task.active == True:
            task.active = False
            
    for project in user_projects:
        if project.active == True:
            project.active = False

    for project in user_projects:
        if bool(Task.query.join(Project.tasks)
           .filter_by(project_id=project._id, archived=False).count()) == False:
            completions[str(project)] = 100
        else:
            completions[str(project)] = (Task.query.join(Project.tasks)
                         .filter_by(project_id=project._id, progress=Progress.deployment, archived=False).count()/
                         Task.query.join(Project.tasks).filter_by(project_id=project._id, archived=False).count()) * 100

    project_info = {project.name:{'date_created':project.date_created,
                                   'date_due':project.date_due,
                                   'total_tasks':Task.query.filter_by(project_id=project._id, archived=False).count(),
                                   'completion':f'{completions[str(project)]}%'} for project in user_projects}
    task_info = {task.name:{'project_name':task.project.name,
                            'time_remaining':task.date_due, 
                            'assigned_users':''} for task in task_today}

    data = {'first_name':active_user.first_name,
            'last_name':active_user.last_name,
            'date_today':date_today,
            'projects':project_info,
            'tasks_today':task_info}

    return jsonify(data)

def send_logout_status():
    active_user = User.query.filter_by(active=True, archived=False).first()
    access = True

    if active_user.active:
        active_user.active = False
        access = False
        db.session.commit()

    elif bool(active_user) == False:
        access = False

    data = {'access':access}

    return jsonify(data)

def send_project_content(project_name):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    user_projects = Project.query.filter_by(user_id=active_user._id, archived=False).all()
    tasks = Task.query.filter_by(project_id=active_project._id, archived=False)
    
    for task in tasks:
        if task.active == True:
            task.active = False

    for project in user_projects:
        if project.active == True:
            project.active = False

    active_project.active = True
    db.session.commit()

    in_progress_tasks = Task.query.filter_by(project_id=active_project._id, progress=Progress.in_progress, archived=False)
    testing_tasks = Task.query.filter_by(project_id=active_project._id, progress=Progress.testing, archived=False)
    revision_tasks = Task.query.filter_by(project_id=active_project._id, progress=Progress.revisions, archived=False)
    deployment_tasks = Task.query.filter_by(project_id=active_project._id, progress=Progress.deployment, archived=False)

    tickets = [in_progress_tasks, testing_tasks, revision_tasks, deployment_tasks]
    completions = {}

    if tasks.count() == 0:
        completion = 100
    else:
        completion = (deployment_tasks.count()/tasks.count()) * 100

    for ticket in tickets:
        for task in ticket:
            if bool(Subtask.query.join(Task.subtasks)
            .filter_by(task_id=task._id, archived=False).count()) == False:
                completions[str(task)] = 100
            else:
                completions[str(task)] = (Subtask.query.join(Task.subtasks)
                                            .filter_by(task_id=task._id, done=True, archived=False).count()/
                                            Subtask.query.join(Task.subtasks)
                                            .filter_by(task_id=task._id, archived=False).count()) * 100
            
    data = {'project_name':active_project.name,
            'completion':f"{completion}%",
            'in_progress_tasks':{task.name:{'description':task.description,
                                            'completion':f'{completions[str(task)]}%',
                                            'date_due':task.date_due,
                                            'subtasks':{subtask.name:{'done':subtask.done,
                                                                      'description':subtask.description}
                                                        for subtask in Subtask.query.join(Task.subtasks)
                                                        .filter_by(task_id=task._id, archived=False)}}
                                                        for task in in_progress_tasks},
            'testing_tasks':{task.name:{'description':task.description,
                                        'completion':f'{completions[str(task)]}%',
                                        'date_due':task.date_due,
                                        'subtasks':{subtask.name:{'done':subtask.done,
                                                                  'description':subtask.description}
                                                        for subtask in Subtask.query.join(Task.subtasks)
                                                        .filter_by(task_id=task._id, archived=False)}}
                                                        for task in testing_tasks},
            'revision_tasks':{task.name:{'description':task.description,
                                         'completion':f'{completions[str(task)]}%',
                                         'date_due':task.date_due,
                                         'subtasks':{subtask.name:{'done':subtask.done,
                                                                   'description':subtask.description}
                                                        for subtask in Subtask.query.join(Task.subtasks)
                                                        .filter_by(task_id=task._id, archived=False)}}
                                                        for task in revision_tasks},
            'deployment_tasks':{task.name:{'description':task.description,
                                           'completion':f'{completions[str(task)]}%',
                                           'date_due':task.date_due,
                                           'subtasks':{subtask.name:{'done':subtask.done,
                                                                     'description':subtask.description}
                                                        for subtask in Subtask.query.join(Task.subtasks)
                                                        .filter_by(task_id=task._id, archived=False)}}
                                                        for task in deployment_tasks}
            }

    return jsonify(data)

def save_project(project_info):
    active_user = User.query.filter_by(active=True, archived=False).first()
    projects = Project.query.filter_by(user_id=active_user._id, archived=False).all()
    saved = True
    entity = Project(user_id=active_user._id, name=project_info['name'], description=project_info['description'],
                     priority_level=0, archived=False, active=False)
    
    for project in projects:
        if project_info['name'] == project.name:
            saved = False
            break
    
    if (saved == True) or (bool(projects) == False):
        saved = True
        db.session.add(entity)
        db.session.commit()

    data = {'saved':saved}

    return jsonify(data)

def remove_project(project_name):
    active_user = User.query.filter_by(active=True, archived=False).first()
    selected_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    projects = Project.query.filter_by(user_id=active_user._id, archived=False).all()
    deleted = False

    for project in projects:
        if selected_project.name == project.name:
            db.session.delete(selected_project)
            db.session.commit()
            deleted = True
    
    data = {'deleted':deleted}

    return jsonify(data)

def send_task_content(project_name, task_name):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    active_task = Task.query.filter_by(project_id=active_project._id, name=task_name, archived=False).first()
    user_tasks = Task.query.filter_by(project_id=active_project._id, archived=False).all()

    for task in user_tasks:
        if task.active == True:
            task.active = False
    
    active_task.active = True
    db.session.commit()

    subtasks = {subtask.name:{'done':subtask.done,
                              'description':subtask.description} for subtask in
                              Subtask.query.join(Task.subtasks).filter_by(task_id=active_task._id, archived=False)}

    data = {active_task.name:{'description':active_task.description,
                         'date_due':active_task.date_due,
                         'participants':'',
                         'subtasks':subtasks}}
    
    return jsonify(data)

def save_task(task_info):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, active=True, archived=False).first()
    saved = True

    if not bool(active_project):
        saved = False

    if saved == True:
        tasks = Task.query.filter_by(project_id=active_project._id, archived=False).all()
        
        entity = Task(project_id=active_project._id, name=task_info['name'], description=task_info['description'],
                        priority_level=0, progress=Progress.in_progress, archived=False, active=False)
        
        for task in tasks:
            if task_info['name'] == task.name:
                saved = False
                break
        
        if (saved == True) or (bool(tasks) == False):
            saved = True
            db.session.add(entity)
            db.session.commit()

            data = {'saved':saved,
                    'project_name':active_project.name}
    else:
        data = {'saved':saved}
        
    return jsonify(data)

def transfer_task(project_name, transfer_info):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    selected_task = Task.query.filter_by(project_id=active_project._id, name=transfer_info['name'], archived=False).first()
    moved = False

    if (selected_task.progress != transfer_info['progress']) and (transfer_info['progress'] in vars(Progress).values()):
        selected_task.progress = transfer_info['progress']
        db.session.commit()
        moved = True

    data = {'moved':moved}

    return jsonify(data)

def remove_task(project_name, task_name):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    selected_task = Task.query.filter_by(project_id=active_project._id, name=task_name, archived=False).first()
    tasks = Task.query.filter_by(project_id=active_project._id, archived=False).all()
    deleted = False

    for task in tasks:
        if selected_task.name == task.name:
            db.session.delete(selected_task)
            db.session.commit()
            deleted = True
    
    data = {'deleted':deleted}

    return jsonify(data)
    
def save_subtask(subtask_info):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, active=True, archived=False).first()
    active_task = Task.query.filter_by(project_id=active_project._id, active=True, archived=False).first()
    saved = True

    if not bool(active_task):
        saved = False

    if saved == True: 
        subtasks = Subtask.query.filter_by(task_id=active_task._id, archived=False).all()
        entity = Subtask(task_id=active_task._id, name=subtask_info['name'], description=subtask_info['description'],
                        done=False, priority_level=0, archived=False)
        
        for subtask in subtasks:
            if subtask_info['name'] == subtask.name:
                saved = False
                break
        
        if (saved == True) or (bool(subtasks) == False):
            saved = True
            db.session.add(entity)
            db.session.commit()

            data = {'saved':saved,
                    'task_name':active_task.name}
    else:
        data = {'saved':saved}
        
    return jsonify(data)

def remove_subtask(project_name, task_name, subtask_name):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    active_task = Task.query.filter_by(project_id=active_project._id, name=task_name, archived=False).first()
    selected_subtask = Subtask.query.filter_by(project_id=active_project._id, name=subtask_name, archived=False).first()
    subtasks = Subtask.query.filter_by(project_id=active_task._id, archived=False).all()
    deleted = False

    for subtask in subtasks:
        if selected_subtask.name == subtask.name:
            db.session.delete(selected_subtask)
            db.session.commit()
            deleted = True
    
    data = {'deleted':deleted}

    return jsonify(data)

def check_subtask(project_name, task_name, check_info):
    active_user = User.query.filter_by(active=True, archived=False).first()
    active_project = Project.query.filter_by(user_id=active_user._id, name=project_name, archived=False).first()
    active_task = Task.query.filter_by(project_id=active_project._id, name=task_name, archived=False).first()
    selected_subtask = Subtask.query.filter_by(task_id=active_task._id, name=check_info['name'], archived=False).first()
    subtasks = Subtask.query.filter_by(task_id=active_task._id, archived=False).all()
    completed = False

    for subtask in subtasks:
        if selected_subtask.name == subtask.name:
            selected_subtask.done = bool(check_info['check'])
            db.session.commit()
            completed = bool(check_info['name'])
    
    data = {'completed':completed}

    return jsonify(data)