from flask import session
    
def check_session():
    public_id = session.get('public_id')

    return public_id

def add_to_session(public_id):
    current_session_id = session.get('public_id')

    if current_session_id:

        if current_session_id != public_id:
            session['public_id'] = public_id

    else:
        session['public_id'] = public_id
    
    print(session.get('public_id'))