from model.subtask.crud import create_subtask

def new_subtask(**kwargs):
    response = create_subtask(kwargs)

    return response