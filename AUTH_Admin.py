from Admin_Session import admin_session


def auth_admin(db, command_handler):
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    
    if username == "admin" : 
        if password == "password":
            admin_session(db, command_handler)
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognized")