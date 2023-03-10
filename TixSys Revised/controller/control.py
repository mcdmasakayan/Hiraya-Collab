from flask import redirect, url_for
from model.fetch import get_credentials, get_user_info
from model.fetch import get_project_info, get_task_info, get_subtask_info
from model.fetch import get_transfer_info
from model.dispatch import send_login_status, send_registration_status
from model.dispatch import send_logout_status, send_dashboard_data
from model.dispatch import send_project_content, send_task_content
from model.dispatch import save_project, save_task, save_subtask
from model.dispatch import transfer_task, remove_task, remove_subtask, remove_project
from view.user_service import login_page, registration_page
from view.user_service import dashboard_page, project_page, task_page

class Link:
    dashboard = 'main_bp.show_dashboard'
    project = 'main_bp.show_project'
    task = 'main_bp.show_task'

def index():
    response = '<h1>This is the index page.</h1>'

    return response

def show_login_system():
    credentials = get_credentials()
    status = send_login_status(credentials)
    response = login_page(status)

    return response

def show_registration_system():
    user_info = get_user_info()
    status = send_registration_status(user_info)
    response = registration_page(status)

    return response

def show_dashboard():
    dashboard_data = send_dashboard_data()
    response = dashboard_page(dashboard_data)

    return response

def logout_account():
    response = send_logout_status()

    return response

def create_project():
    project_info = get_project_info()
    save_project(project_info)
    
    return redirect(url_for(Link.dashboard))

def open_project():
    name = get_project_info()['name']

    return redirect(url_for(Link.project, project_name=name))

def show_project(project_name):
    project_content = send_project_content(project_name)
    response = project_page(project_content)

    return response

def delete_project():
    name = get_project_info()['name']
    remove_project(name)

    return redirect(url_for(Link.dashboard))

def create_task(project_name):
    task_info = get_task_info()
    save_task(task_info)

    return redirect(url_for(Link.project, project_name=project_name))

def open_task(project_name):
    name = get_task_info()['name']

    return redirect(url_for(Link.task, project_name=project_name, task_name=name))

def show_task(project_name, task_name):
    task_content = send_task_content(project_name, task_name)
    response = task_page(task_content)

    return response

def move_task(project_name):
    transfer_info = get_transfer_info()
    transfer_task(project_name, transfer_info)

    return redirect(url_for(Link.project, project_name=project_name))

def delete_task(project_name):
    name = get_task_info()['name']
    remove_task(project_name, name)

    return redirect(url_for(Link.project, project_name=project_name))

def create_subtask(project_name, task_name):
    subtask_info = get_subtask_info()
    save_subtask(subtask_info)

    return redirect(url_for(Link.task, project_name=project_name, task_name=task_name))

def complete_subtask(project_name, task_name):

    return redirect(url_for(Link.task, project_name=project_name, task_name=task_name))

def delete_subtask(project_name, task_name):
    name = get_subtask_info()['name']
    remove_subtask(project_name, task_name, name)

    return redirect(url_for(Link.task, project_name=project_name, task_name=task_name))