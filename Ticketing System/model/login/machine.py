from model.database.machine import User, db
import hashlib

def hash_string(str):
    hash_str = hashlib.md5(str.encode()).hexdigest()

    return hash_str

def login_user(username, password):
    status = "Login Failed."
    system_msg = "SYSTEM: Account not found in database."
    pw_hash = hash_string(password)

    for x in User.query.all():
        if x.username == username and x.password == pw_hash:
            system_msg = "SYSTEM: Account found in database."
            status = f"Login Successful. Welcome {x.first_name} {x.last_name}!"
            break
    print(system_msg)
    
    return status
 
def register_user(email, username, password, first_name, last_name, verified, archived):
    status = "Registration Successful."
    add_user = False
    pw_hash = hash_string(password)
   
    user = User(email=email, username=username, password=pw_hash, first_name=first_name,
                           last_name=last_name, verified=verified, archived=archived)

    for x in User.query.all():
        if email == x.email or username == x.username:
            add_user = False
            status = "Registration Failed."
            print("SYSTEM: Account already existing in database.")
            break
        else:
            add_user = True

    if add_user == True or bool(User.query.all()) == False:
        db.session.add(user)
        db.session.commit()
        print("SYSTEM: Account inserted in database.")
        print(User().get_users())

    return status