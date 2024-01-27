import mysql.connector as mysql

from AUTH_Admin import auth_admin


# connecting to databse
db = mysql.connect(host = "localhost", user = "root", password = "", database = "College")

"""
allow us to run different queries del, insert and so on
buffered = true means we can multi queries without errors
"""
command_handler = db.cursor(buffered=True)



def main(db,command_handler):
    while 1:
        print("Welcome to college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        
        
        user_option = input(str("option : "))
        if user_option == "1":
            print("Student Login")
        elif user_option == "2":
            print("teacher Login")
        elif user_option == "3":
            auth_admin(db,command_handler)
        else:
            print("no valid option was selected")
            
main(db, command_handler)
        
            