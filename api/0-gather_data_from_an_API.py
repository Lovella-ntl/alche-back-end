#!/usr/bin/python3
import requests
import sys
 
 
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
 
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    employee_name = user.get("name")
 
    todos = requests.get("{}/todos".format(base_url)).json()
    employee_todos = [
        task for task in todos if task.get("userId") == employee_id
    ]
 
    total_tasks = len(employee_todos)
    done_tasks = [
        task for task in employee_todos if task.get("completed") is True
    ]
    number_of_done_tasks = len(done_tasks)
 
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
 
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
