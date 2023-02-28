from flask import request, jsonify
from model.machine import db, Project as projects

def pcreate_logic():
    try:
        name = request.args.get('name')
        description = request.args.get('description')

        project = projects(name=name, description=description, to_do=True, in_progress=False,
                           for_checking=False, done=False, archived=False)

        if (bool(projects.query.all()) == False):
                db.session.add(project)
                db.session.commit()
                state = 1
                msg = "SYSTEM: Project inserted in database."
        else:
            for x in projects.query.all():
                if (name == x.name):
                    state = 0
                    msg = "SYSTEM: Project not inserted in database. (Project already existing)"
                    break 

    except (UnboundLocalError, AttributeError):
        state = 0
        msg = "SYSTEM: An error has occurred."

    return jsonify({'state':state,
                    'message':msg})

def popen_logic():
     try:
        name = request.args.get('name')

        if(bool(projects.query.all()) == False):
            state = 0
            msg = "SYSTEM: Project does not exist in database."
        else:
            for x in projects.query.all():
                if (name == x.name):
                    state = 1
                    msg = "SYSTEM: Project opened."
                    break
                else:
                    state = 0
                    msg = "SYSTEM: Project not opened. (Project does not exist)"

     except (UnboundLocalError, AttributeError):
        state = 0
        msg = "SYSTEM: An error has occurred."
     
     return jsonify({'state':state,
                     'message':msg})