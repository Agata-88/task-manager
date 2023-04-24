# Imported libraries
from datetime import date

# Program opens user.txt file in read mode and reads lines.
# Variables are crated and information from user.txt file
# is stored in them. 'login' and 'password' variables store
# items from indexed posistion 0 and 1 respecitvely. Each of 
# lists is appended each for loop.
username = []
password = []
with open ("user.txt", "r") as f:
    for lines in f:
        lines = lines.strip("\n").split(", ")
        username_list = username.append(lines[0])
        password_list = password.append(lines[1])
        print(username)
        print(password)
# User is asked to enter login and password. index method is used
# to check position of username in 'username' list and corresponding 
# password in 'password' list based on their index in lists.
# If indexes are matching menu is displayed. If username is recognised
# and passowrd is not or if username is not recognised relevant 
# output is printed. User is continously asked to enter username
# and password.
username_input = input("Please enter your login: ").lower()
password_input = input ("Please enter your password: ").lower()

username_index = -1
password_index = -1
i=0

if username_input in username:
    if password_input in password:
        username_index = username.index(username_input)
        password_index = password.index(password_input)
        if username_index == password_index:
            print("Correct information entered")
    while password_input not in password:
        print ("Password not recognised, please try again: ")
        username_input = input("Please enter your login: ").lower()
        password_input = input ("Please enter your password: ").lower()
        i+=1
while username_input not in username:
    print ("Username not recognised, plase try again: ")
    username_input = input("Please enter your login: ").lower()
    password_input = input ("Please enter your password: ").lower()
    i+=1

# Special menu is displayed for admin only as code additionally
# looks for 'admin' user input. 'r' and 'ds' functions
# are only available to admin.

while username_index == password_index and username_input == "admin".lower():
    menu = input("Please select one of the following options: \n"
                "r - Register new user \n"
                "a - Add task\n"
                "va - View all tasks\n"
                "vm - View my tasks\n"
                "ds - Display statistics\n"
                "e - Exit\n").lower()
    if menu == "r":
            username = input("Please input new username: ")
            password = input("Please input new password: ")
            password_confirmation = input("Please confirm password: ")
            if password == password_confirmation:
                with open ("user.txt", "a") as f:
                    f.write ("\n" + username + ", " + password)
                    print("New user registered successfully")
           
            if password != password_confirmation:
                print("Passwords are not matching, new user not registered.")

# ds menu if only avaialble for admin and checks number of lines
# in user.txt and tasks.txt file as number of lines equals
# numer of users and tasks respecitvely.
    elif menu == "ds":
        with open ("user.txt", "r") as f:
                total_users = f.readlines()
                print("Total number of users: ", len(total_users))
        with open ("tasks.txt", "r") as f:
                total_tasks = f.readlines()
                print("Total number of tasks: ", len(total_tasks))
    elif menu == "a":
        username = input("Input username of the person whom the task will be assigned to: ")
        task = input("Please enter task name: \n")
        task_description = input ("Please enter task description: \n")
        due_date = input ("Please confirm due date for the task in dd mmm yyyy format: \n")
        today = date.today()
        today_str = today.strftime("%d %b %Y")
        task_completion_status = str("No")
        with open ("tasks.txt", "a") as f:
            f.write ("\n"+ username + ", " + task + ", "  + task_description + ", "  + today_str + ", " + due_date + ", " + task_completion_status)  #date assigned not reading
            print("Task added successfully")
        
    elif menu == "va":
        with open ("tasks.txt", "r") as f:
            for lines in f:
                    lines = lines.split(", ")
                    order = ["Assigned to: \t\t", "Task: \t\t\t", "Task description: \t", "Date assigned: \t\t", "Due date: \t\t", "Task complete? \t\t"]
                    for (a,b) in zip(lines,order):
                        print(b,a)
                    
# Below code allows user to view tasks assigned to currently logged in user.
    elif menu == "vm":
        with open ("tasks.txt", "r") as f:
            for lines in f:
                if username_input in username:
                    username = str(username)
                    if lines.startswith(username_input):
                        lines = lines.split(", ")
                        order = ["Assigned to: \t\t", "Task: \t\t\t", "Task description: \t", "Date assigned: \t\t", "Due date: \t\t", "Task complete? \t\t"]
                        for (a,b) in zip(lines,order):
                            print(b,a)  
    elif menu == "e":
        print('Goodbye!!!')
        exit()  

    else:
        print("You have made a wrong choice, Please Try again")

while username_index == password_index:
    menu = input("Please select one of the following options: \n"
                "a - Add task\n"
                "va - View all tasks\n"
                "vm - View my tasks\n"
                "e - Exit\n").lower()
    if menu == "a":
            username = input("Input username of the person whom the task will be assigned to: ")
            task = input("Please enter task name: \n")
            task_description = input ("Please enter task description: \n")
            due_date = input ("Please confirm due date for the task in dd mmm yyyy format: \n")
            today = date.today()
            today_str = today.strftime("%d %b %Y")
            task_completion_status = str("No")
            with open ("tasks.txt", "a") as f:
                f.write ("\n"+ username + ", " + task + ", "  + task_description + ", "  + today_str + ", " + due_date + ", " + task_completion_status)  #date assigned not reading
                print("Task added successfully")
        
    elif menu == "va":
        with open ("tasks.txt", "r") as f:
            for lines in f:
                    lines = lines.split(", ")
                    order = ["Assigned to: \t\t", "Task: \t\t\t", "Task description: \t", "Date assigned: \t\t", "Due date: \t\t", "Task complete? \t\t"]
                    for (a,b) in zip(lines,order):
                        print(b,a)
        
# Below code allows user to view tasks assigned to currently logged in user.
    elif menu == "vm":
        with open ("tasks.txt", "r") as f:
            for lines in f:
                if username_input not in username:
                    print("No tasks are currently assigned to this user: ")
                if username_input in username:
                    username = str(username)
                    if lines.startswith(username_input):
                        lines = lines.split(", ")
                        order = ["Assigned to: \t\t", "Task: \t\t\t", "Task description: \t", "Date assigned: \t\t", "Due date: \t\t", "Task complete? \t\t"]
                        for (a,b) in zip(lines,order):
                            print(b,a)
    elif menu == "e":
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")