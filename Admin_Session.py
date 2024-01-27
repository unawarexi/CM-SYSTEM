
def admin_session(db,command_handler):
   while 1:
       print("")
       print("Admin Menu")
       
       print("1. Register new Student ")
       
       print("2. Register new Teacher ")
       
       print("3. Delete Existing  Student")
       
       print("4. Delete Exisitng Teacher ")
       
       print("5. Logout")
       
       user_option = input(str("option : "))
       if user_option == "1":
           print("")
           print("register new student")
           username = input(str("student username : "))
           password = input(str("student password : "))
           query_vals = (username, password)
           
           command_handler.execute("INSERT INTO users(username, password, privilege) VALUES (%s,%s, 'student')",query_vals)
           db.commit()
           print(username + "has been registered as a student")
           
       elif user_option == "2":
           print("")
           print("register new teacher")
           username = input(str("teacher username : "))
           password = input(str("teacher password : "))
           query_vals = (username, password)
           
           command_handler.execute("INSERT INTO users(username, password, privilege) VALUES (%s,%s, 'teacher')",query_vals)
           db.commit()
           print(username + "has been registered as a teacher")
           
       elif user_option == "3":
           print("")
           print("delete Existing Student Account")
           username = input(str("student username : "))
           query_vals = (username, "student")
           command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
           db.commit()
           
           if command_handler.rowcount <  1:
               print("User not found")
           else:
               print(username + "has been deleted")
               
       elif user_option == "4":
           print("")
           print("delete Existing teacher Account")
           username = input(str("teacher username : "))
           query_vals = (username, "teacher")
           command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
           db.commit()
           
           if command_handler.rowcount <  1:
               print("User not found")
           else:
               print(username + "has been deleted")
               
       elif user_option == "5":
            print("Logging out...")
            break
        
       else:
            print("Invalid option. Please choose again.")
          