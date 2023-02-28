from flask import request, jsonify
from model.machine import db, Project as projects
from view.login.service import session

def pcreate_logic():
    if 'active_user' in session:
        active_user = session['active_user']
        try:
            name = request.args.get('name')
            description = request.args.get('description')

            project = projects(name=name, user_id=active_user, description=description, to_do=True, in_progress=False,
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
    else:
        state = 0
        msg = "SYSTEM: Must login first."

    return jsonify({'state':state,
                    'message':msg})

def popen_logic():
    if 'active_user' in session:
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
    else:
        state = 0
        msg = "SYSTEM: Must login first."

    return jsonify({'state':state,
                        'message':msg})

def logout_logic():
    if 'active_user' in session:
        active_user = session['active_user']
        session.pop(active_user, None)
        auth = 0
        msg = "SYSTEM: Logout successful."
    else:
        auth = 0
        msg = "SYSTEM: You are not logged in."
    
    return jsonify({'auth':auth,
                    'message':msg})