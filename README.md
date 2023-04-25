# Task Manager

## What is this program?

Task manager is a program created for small business that can help to manage tasks assigned to each member of the team. This program works with two text files, user.txt and tasks.txt. User.txt file stores username and password for each user that has permission to use this program. tasks.txt file stores list of all tasks that the team is working on. Program allows to register user, add task, view all tasks and view task assigned to currently registered user or exit.

## Table of Contents

- [Are there any prerequisites?](#are-there-any-prerequisites?)
- [How can this program be run?](#how-can-this-program-be-run?)
- [What does this program do specifically?](#what-does-this-program-do-specifically?)

## Are there any prerequisites?

This program uses Python verion 3.7.

## How can this program be run?

All you need to do is to download the files and open the task_manager.py in code editor of your choice.

## What does this program do specifically?

1. It opens the "user.txt" file in read mode and reads each line, storing the information in two lists: username and password.
2. The user is prompted to enter their login and password. The program checks if the login and password entered match the ones in the username and password lists, respectively.
3. If the login and password match, a special menu is displayed for admin users. Admin users are identified by the username "admin".

![menu](https://user-images.githubusercontent.com/118485184/234401328-ec8839c1-efc2-41d8-9d1a-bf6792a57548.gif)

If the user selects the "r" option from the menu, they are prompted to enter a new username and password. If the passwords match, the new user is registered by appending their information to the "user.txt" file.

![r](https://user-images.githubusercontent.com/118485184/234402541-f5921056-e670-45a0-bfd5-fffae4db81ff.gif)

If the user selects the "ds" option from the menu, the program counts the number of users and tasks in both the "user.txt" and "tasks.txt" files and prints the results.

![ds](https://user-images.githubusercontent.com/118485184/234403597-5862cf36-a61e-4c04-92ce-d10245ce4e38.gif)


If the user selects the "a" option from the menu, they are prompted to enter information about a new task, which is then appended to the "tasks.txt" file.

![a](https://user-images.githubusercontent.com/118485184/234404606-07be204c-3921-4500-a05a-6b43617605d8.gif)

If the user selects the "va" option from the menu, the program reads the "tasks.txt" file and prints information about all tasks.

![va](https://user-images.githubusercontent.com/118485184/234405108-e7c5964c-c43b-42e8-84c4-dfb544ddc398.gif)

If the user selects the "vm" option from the menu, the program reads the "tasks.txt" file and prints information about tasks assigned to the currently logged in user.
If the user selects the "e" option from the menu, the program terminates.
