from flask import session
    
def check_session():
    public_id = 'ff01d9f1-46fe-4df1-a54c-dff62787d4b3'

    return public_id

def add_to_session(public_id):
    current_session_id = session.get('public_id')

    if current_session_id:

        if current_session_id != public_id:
            session['public_id'] = public_id

    else:
        session['public_id'] = public_id
    
    print(session.get('public_id'))