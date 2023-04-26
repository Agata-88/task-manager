# Imported libraries
from datetime import date
from datetime import datetime
import datetime

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
        # print(username)
        # print(password)
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

# Functions are created for relevant menu outputs. 
# reg_user function allows admin to create new user. 
# If username already exists relevant error message is displayed
# and user is asked for new username.
def reg_user ():
    global username
    reg_username = input("Please input new username: ")
    password = input("Please input new password: ")
    password_confirmation = input("Please confirm password: ")
    if password == password_confirmation:
        with open ("user.txt", "a") as f:
            f.write ("\n" + reg_username + ", " + password)
            print("\nNew user registered successfully.\n")      
    if password != password_confirmation:
        print("\nPasswords are not matching, new user not registered. Please try again.\n")
    return()

# add_task function allows user to add new task basen on series
# of questions held in variables. Program reads from tasks.txt 
# file and writes another task into the same file.
def add_task ():
    task_num=0
    username = input("Input username of the person whom the task will be assigned to: \n")
    task = input("Please enter task name: \n")
    task_description = input ("Please enter task description: \n")
    due_date = input ("Please confirm due date for the task in dd mmm yyyy format: \n")
    today = date.today()
    today_str = today.strftime("%d %b %Y")
    task_completion_status = str("No")
    with open ("tasks.txt", "r") as f:
        data = len(f.readlines())
        task_num = data+1
    with open ("tasks.txt", "a") as f:
        f.write ("\n"+ str(task_num) + ", " + username + ", " + task + ", "  + task_description + ", "  + today_str + ", " + due_date + ", " + task_completion_status)  #date assigned not reading
        print("\nTask added successfully\n")

# view_all function allows user to view all tasks from tasks.txt file.
# All tasks are displayed.
def view_all():
    with open ("tasks.txt", "r") as f:
            for lines in f:
                    lines = lines.split(", ")
                    order = ["Task number: \t\t", "Assigned to: \t\t", "Task: \t\t\t", "Task description: \t", "Date assigned: \t\t", "Due date: \t\t", "Task complete? \t\t"]
                    for (a,b) in zip(lines,order):
                        print(b,a)
                    print("-"*79) 
    return()

# view_mine function allows currenlty logged user to view their tasks. 
# User can also mark their task as complete or edit their tasks.
# Task can only be edited if it is not marked as completed. 
# Relevant outputs are printed. Outcome of all edits is written
# into the same tasks.txt file.
def view_mine():
    lines_zero = []
    long_string = []
    with open ("tasks.txt", "r") as f:
        print ("\nBelow tasks are currenlty assigned to", username_input, ":\n")
        for lines in f:
            global username
            if username_input in username:
                    username = str(username)
                    if username_input in lines:
                        lines = lines.split(", ")
                        order = ["Assignment number: \t", "Assigned to: \t\t", "Task: \t\t\t", "Task description: \t", "Date assigned: \t\t", "Due date: \t\t", "Task complete? \t\t"]
                        for (a,b) in zip(lines,order):
                            print(b,a)  
                        lines_zero.append(lines[0]) 
        task_choice = input("\nPlease choose task number to mark it as complete or edit; alternatively please enter '-1' to return to main menu: \n")
        if task_choice == "-1":
                print("\nYou have returned to main menu.\n")
        if task_choice in lines_zero:
            task_op = input("To mark task as complete please enter '1', to edit please enter '2': \n")
            if task_op == "1":
                long_string = []
                one_string = str(one_string)
                with open ("tasks.txt", "r") as f:
                    for lines in f:
                        if lines.startswith(task_choice):
                            lines = lines.split(", ")
                            lines[6] = "Yes\n"
                            lines = ", ".join(lines)
                        one_string = long_string.append(lines)
                        one_string = "".join(long_string)
                with open ("tasks.txt", "w") as f:
                    f.write(one_string)
                    print("Selected task has been marked as completed, well done!\n")
            if task_op == "2":
                with open ("tasks.txt", "r") as f:
                    for lines in f:
                        if lines.startswith(task_choice):
                            lines = lines.split(", ")
                            if lines[6] == "Yes\n":
                               print("\nThis task cannot be edited as it has already been completed.\n")                           
                            if lines[6] == "No\n":
                                new_user_assigned = input("Please enter username of new person assigned to this task: \n")
                                new_due_date = input("Please enter new due date for this task: \n")
                                lines[1] = new_user_assigned
                                lines[5] = new_due_date
                            lines = ", ".join(lines)
                        one_string = long_string.append(lines)
                        one_string = "".join(long_string)
                with open ("tasks.txt", "w") as f:
                    f.write(one_string)
                    #print("\nTask has been edited successfully\n")                        
    return()

# disp_stats function calls gen_reports function so files 
# 'task_overview.txt' and 'user_overview.txt' can be created 
# in the first instance if not previously created by admin.
# Program then reads from relevant .txt files and output 
# is displayed.
def disp_stats():
    gen_reports()
    print("Current task and user statistics: \n")
    with open("task_overview.txt", "r") as f:
        print(f.read())
    with open("user_overview.txt", "r") as f:
        print(f.read())

# gen_reports function creates "task_overview.txt" and "user_overview.txt" files.
# "task.txt" file is read and lines are counted to count total number of tasks.
# if statements are created to establish task status and if task is overdue.
# Relevant calucations are compelted to satify capstone project requirement.
# Result of these is written into "task_overview.txt" file. 
# Information from both "user.txt" and "tasks.txt" files is used to
# run neccessary calculations which are then witten into "user_overview.txt" file.

def gen_reports():
    with open ("tasks.txt", "r") as f:
        task_count=len(f.readlines())
        f.seek(0)
        yes_count = []
        no_count = []
        num_overdue = []
        no_and_overdue_count = []
        perc_incomplete = ()
        no_and_overdue = ()
        for lines in f:
            lines = lines.strip("\n").split(", ")
            today = date.today()
            x= datetime.datetime.strptime(lines[5], "%d %b %Y").date()
            y = x.strftime("%d %b %Y")
            due_date = datetime.datetime.strptime(y,"%d %b %Y").date()
            if lines[6] == "Yes":
                yes = lines.count("Yes")
                yes_count.append(yes)
            if lines[6] == "No":
                no = lines.count("No")
                no_count.append(no)
            if lines[6] == "No" and today>due_date:
                no_and_overdue = lines.count("No") and lines.count(today>due_date)
                no_and_overdue_count.append(no_and_overdue)
            perc_incomplete = (len(no_count)/task_count) * 100
            if today> due_date:
                overdue = lines.count(today>due_date)
                num_overdue.append(overdue)
                print(due_date)
        print("\nTask report has been generated and is available to view in 'task_overview.txt' file\n")
    with open ("task_overview.txt", "w") as task_overview:
        task_overview.write ("--------------------------------------------------------\n"
                "Total number of tasks generated: " + "\t" + str(task_count) + "\n" 
                "Total number of completed tasks: " + "\t" +  str(len(yes_count)) + "\n"
                "Total number of uncompleted tasks: " + "\t" + str(len(no_count))+ "\n"
                "Not completed and overdue tasks: "+ "\t" +  str(len(no_and_overdue_count))+ "\n"
                "Percentage of incomplete tasks: " + "\t" +  str(round(perc_incomplete,(2)))+ "\n"
                "Total number of overdue tasks: " + "\t\t" +  str(len(num_overdue)) + "\n"
                "--------------------------------------------------------\n")
    global username
    with open ("user.txt", "r") as user_file:
        user_count=len(user_file.readlines())
        user_file.seek(0)
    with open ("tasks.txt", "r") as task_file:
        task_count=len(task_file.readlines())
        task_file.seek(0)
        task_lines = task_file.readlines()
        task_file.seek(0)
    for name in username:
        user_task_count = 0
        comp_user_tasks = 0
        perc_comp_user_tasks = 0
        not_comp_user_tasks = 0
        overdue_user_tasks = 0
        perc_overdue_user_task = 0
        no_tasks = ""
        for lines in task_lines:  
            lines = lines.strip("\n").split(", ")
            today = date.today()
            x= datetime.datetime.strptime(lines[5], "%d %b %Y").date()
            y = x.strftime("%d %b %Y")
            due_date = datetime.datetime.strptime(y,"%d %b %Y").date()
            if name == lines[1]:
                user_task_count +=1                
                if lines[6] == "Yes":
                    comp_user_tasks +=1
                if lines[6] == "No":
                    not_comp_user_tasks +=1
                if lines[6] == "No" and today>due_date:
                    overdue_user_tasks +=1
        if user_task_count == 0:
            no_tasks = ("There are no tasks assigned to " + name)
            with open ("user_overview.txt", "a") as user_overview:  
                user_overview.write("--------------------------------------------------------\n" + no_tasks)
            if user_task_count == 0:
                break
        prc_user_tasks = (user_task_count/task_count *100)  
        perc_comp_user_tasks = (comp_user_tasks/user_task_count * 100)#
        perc_not_comp_user_task = ((not_comp_user_tasks/user_task_count) * 100)
        perc_overdue_user_task = ((overdue_user_tasks/user_task_count) *100)    
        
        with open ("user_overview.txt", "a") as user_overview:
            user_overview.write ("--------------------------------------------------------\n"
                                "Total number of users registered : " + "\t\t\t\t" + str(user_count) + "\n"
                                "Total number of tasks generated : " + "\t\t\t\t" + str(task_count) + "\n"
                                "Number of tasks assigned to " + name + " : \t\t\t" + str(user_task_count) + "\n"
                                "Percentage of tasks assigned to " + name + " : \t\t" + str(round(prc_user_tasks,2)) + "% \n"
                                "Percentage of tasks completed by " + name + " : \t\t" + str(round(perc_comp_user_tasks,2)) + "%\n"
                                "Percentage of tasks not completed by " + name + " : \t" + str(round(perc_not_comp_user_task,2)) + "%\n"
                                "Percentage of tasks which haven't been\ncompleted by " + name + " and are overdue : \t\t\t" + str(round(perc_overdue_user_task,2)) + "%\n")
                            
                                
    print("\nUser report has been generated and is available to view in 'user_overview.txt' file.\n")
    return ()

while username_index == password_index and username_input == "admin".lower():
    menu = input("\nPlease select one of the following options: \n"
                "r - Register new user \n"
                "a - Add task\n"
                "va - View all tasks\n"
                "vm - View my tasks\n"
                "ds - Display statistics\n"
                "gr - Generate Reports\n"
                "e - Exit\n").lower()
    print("-"*79)
    if menu == "r":
           reg_user()
    elif menu == "ds":
        disp_stats()
    elif menu == "gr":
        gen_reports()
    elif menu == "a":
        add_task()      
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()

    elif menu == "e":
        print('Goodbye!!!') 
        exit()  
    else:
        print("You have made a wrong choice, Please Try again")

while username_index == password_index:
    menu = input("\nPlease select one of the following options: \n"
                "a - Add task\n"
                "va - View all tasks\n"
                "vm - View my tasks\n"
                "e - Exit\n").lower()
    print("-"*79)
    if menu == "a":
        add_task()    
    elif menu == "va":
        view_all()
    elif menu == "vm":
        view_mine()
    elif menu == "e":
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
