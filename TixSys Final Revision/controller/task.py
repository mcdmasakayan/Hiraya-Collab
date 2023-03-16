from model.task.crud import create_task, get_task_data, archive_task

def new_task(**kwargs):
    response = create_task(kwargs)

    return response

def open_task(**kwargs):
    response = get_task_data(kwargs)

    return response

def remove_task(**kwargs):
    response = archive_task(kwargs)

    return response