from model.project.crud import create_project, get_project_data

def new_project():
    response = create_project()

    return response

def open_project(**kwargs):
    response = get_project_data(kwargs)

    return response