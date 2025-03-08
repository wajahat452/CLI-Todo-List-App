"""
CLI To do list
Made by: Wajahat Hussain

Things to note before running.
--Please use quotes around any argument that has more than one word
--for the updatestatus button please enter a space and the id# of the task you want to change
then write use the status button after and type the new status for the item
--for the list-name button please use a .json file
"""

from sys import argv
import sys
import argparse
import json


parser = argparse.ArgumentParser(description="TODO list")
make_old_list_not_run=False


#Add Arguments
parser.add_argument(
"--category",
required=False,
help="This is the category of the TODO list item"
)
parser.add_argument(
"--description",
required=False,
help="This is the description of the item your adding"
)
parser.add_argument(
"--status",
required=False,
choices=["in progress", "complete", "incomplete"],
help="This is the status of the item your adding"
)
parser.add_argument(
    "--view",
    action='store_true',
    help="This shows the TO DO list to the user"
)
parser.add_argument(
    "--updatestatus",
    required=False,
    type=int,
    help="type the id# of task you want to update then type --status after and what you want to change it to"
)
parser.add_argument(
    "--list-name",
    required=False,
    help="This is what you press to make a new list. Please enter the name youd like for the list after pressing this, then continue giving the arguments"
)

#Parse Arguments
args=parser.parse_args()
category = args.category
description = args.description
status=args.status
view=args.view
updatestatus=args.updatestatus
list_name=args.list_name


#Code for the parsers to do thier jobs
IDs=[]

if view and make_old_list_not_run==False:
    if list_name:
        make_old_list_not_run=True
    else:
        make_old_list_not_run=False
    with open("TODO.json", "r") as file:
        data_from_file= json.load(file)
    for data in data_from_file:
        print(f"|ID: {data['id']}| --- |Category: {data['category']}| --- |Description: {data['description']}| --- |Status: {data['status']}|\n") 

#This part allows for the user to change the status of an item on their todo list
status_update=False
if updatestatus:
    with open("TODO.json", "r")as file:
        data_from_file=json.load(file)
    for data in data_from_file:
        if updatestatus== data['id']:
            data['status']=status
            status_update=True
            break

if status_update==True:
    with open("TODO.json", "w")as file:
        json.dump(data_from_file, file, indent=4)


#This section makes another to do list with the users desired name
if list_name:
    make_old_list_not_run=True
    
    try:
        with open(list_name, "r")as file:
            tasks=json.load(file)
            for task in tasks:
                IDs.append(task['id'])
    except (FileNotFoundError, json.JSONDecodeError):
        tasks=[]


    if IDs:
        max_id=max(IDs)
        identification= max_id +1
    else:
        identification=1

    if category and description and status:
        new_todolist= {
        "id": identification,
        "category": category,
        "description": description,
        "status": status
    }
        tasks.append(new_todolist)
   
    with open(list_name, "w")as file:
        json.dump(tasks, file, indent=4)

    if view and make_old_list_not_run==True:
        with open(list_name, "r") as file:
            data_from_file= json.load(file)
        print(f"The --{list_name}-- list:\n\n")
        for data in data_from_file:
            print(f"|ID: {data['id']}| --- |Category: {data['category']}| --- |Description: {data['description']}| --- |Status: {data['status']}|\n") 




#Reading JSON file b4 writing for the ORIGINAL todo list
if make_old_list_not_run==False:
    try:
        with open("TODO.json", "r") as file:
            tasks= json.load(file)
            for task in tasks:
                IDs.append(task['id'])
    except (json.JSONDecodeError):
        tasks=[]

    if IDs:
        max_id=max(IDs)
        identification= max_id +1
    else:
        identification=1


    #Appends the list when needed arguments are given (ORIGINAL LIST)
    if category and description and status:
    
        todolist= {
        "id": identification,
        "category": category,
        "description": description,
        "status": status
        }
        tasks.append(todolist)
    

    #Sending to the JSON file (ORIGINAL LIST)
    with open("TODO.json", "w") as file:
        json.dump(tasks, file, indent=4)

    







    