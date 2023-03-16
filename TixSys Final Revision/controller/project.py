from model.project.crud import create_project, get_project_data, delete_project

def new_project():
    response = create_project()

    return response

def open_project(**kwargs):
    response = get_project_data(kwargs)

    return response

def remove_project(**kwargs):
    response = delete_project(kwargs)
    return response