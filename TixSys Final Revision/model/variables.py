progress_list = ['In Progress', 'Revisions', 'Testing', 'Deployment']

class Link:
    admin = '/admin'
    settings = '/dashboard/settings'
    login = '/login'
    dashboard = '/dashboard'
    project = '/dashboard/<string:project_name>'
    task = '/dashboard/<string:project_name>/<string:task_name>'
    
class Message:
    #System
    next_update = 'This feature will be in the next update.'

    #User
    not_logged_in = 'User not logged in.'
    access_granted = 'Access Granted.'
    access_not_granted = 'Access Denied.'
    email_exists = 'Email already exists. User not registered.'
    username_exists = 'Username already exists. User not registered.'
    user_registered = 'User registered.'
    user_not_registered = 'User not registered.'
    user_archived = 'User archived.'
    user_not_archived = 'User not archived.'

    #Project
    project_exists = 'Project name already exists. Project not created.'
    project_created = 'Project created.'
    project_not_created = 'Project not created.'
    project_not_opened = 'Project not opened.'
    project_archived = 'Project archived.'
    project_not_archived = 'Project not archived.'
    project_deleted = 'Project deleted.'
    project_not_deleted = 'Project not deleted.'

    #Task
    task_exists = 'Task name already exists. Task not created.'
    task_created = 'Task created.'
    task_not_created = 'Task not created.'
    task_not_opened = 'Task not opened.'
    task_archived = 'Task archived.'
    task_not_archived = 'Task not archived.'
    task_moved = 'Task moved.'
    task_not_moved = 'Task not moved.'

    #Subtask
    subtask_exists = 'Subtask name already exists. Subtask not created.'
    subtask_created = 'Subtask created.'
    subtask_not_created = 'Subtask not created.'
    subtask_archived = ' Subtask archived.'
    subtask_not_archived = 'Subtask archived.'