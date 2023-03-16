class Link:
    admin = '/admin'
    settings = '/settings'
    login = '/login'
    register = '/register'
    dashboard = '/dashboard'
    project = '/dashboard/<string:project_name>'
    task = '/dashboard/<string:project_name>/<string:task_name>'

class Message:
    not_logged_in = 'User not logged in.'
    
    #User
    access_granted = 'Access Granted.'
    access_not_granted = 'Access Denied.'
    email_exists = 'Email already exists. User not registered.'
    username_exists = 'Username already exists. User not registered.'
    user_registered = 'User registered.'
    user_not_registered = 'User not registered.'

    #Project
    project_exists = 'Project name already exists. Project not created.'
    project_created = 'Project created.'
    project_not_created = 'Project not created.'
    project_not_opened = 'Project not opened.'
    project_deleted = 'Project deleted.'
    project_not_deleted = 'Project not deleted.'

    #Task
    task_exists = 'Task name already exists. Task not created.'
    task_created = 'Task created.'
    task_not_created = 'Task not created.'
    task_not_opened = 'Task not opened.'

    #Subtask
    subtask_exists = 'Subtask name already exists. Subtask not created.'
    subtask_created = 'Subtask created.'
    subtask_not_created = 'Subtask not created.'