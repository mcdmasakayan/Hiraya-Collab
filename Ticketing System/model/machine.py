import mysql.connector as mysql

db = mysql.connect(host='localhost', port=3306, username='root', password='root')
crsr = db.cursor()
crsr.execute("CREATE DATABASE IF NOT EXISTS tixsys")

class User:
        email = ""
        username = ""
        password = ""
        first_name = ""
        last_name = ""
        verified = False
        archived = False
        
user = User()

def initiate_database():
    db = mysql.connect(host='localhost', port=3306, username='root', password='root', database="tixsys")
    crsr = db.cursor()

    crsr.execute("""CREATE TABLE IF NOT EXISTS tixsys_accounts VALUES (email VARCHAR(255),
                 username VARCHAR(255), password VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255),
                 verified BOOLEAN, archived BOOLEAN)""")
    
    print("SYSTEM: Database connection sucessful.")

def login_user():
    #logic here

def register_user():        
    crsr.execute(
                    """INSERT INTO tixsys_accounts (email, username, password, first_name,
                    last_name, verified, archived) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (user.email, user.username, user.password, user.first_name, user.last_name,
                    user.verified, user.archived))
    print("SYSTEM: Database update sucessful.")
    
