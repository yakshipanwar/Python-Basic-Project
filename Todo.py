check = True
name = input("Enter Your name : " )
print(f"Welcome {name}")
number = int(input("Enter Number of tasks : "))
initial = 0
todo_list = ["      "]*number
while check:
    operation = input("Enter the operations "" ADD , DELETE , UPDATE , DONE ,  SHOW"" : ")
    if operation == "ADD":
        if number != initial:
            task = input(f"Enter the {initial + 1} task ")
            todo_list[initial] = task
            initial = initial + 1
        else:
            print("You entered Your complete today task ...")
    elif operation == "UPDATE":
        if todo_list:
            n = int(input("Enter number of task you want to update : " ))
            if n > initial or n < 0:
                print("Enter valid input ")
            else:
                task = input("Enter the task with which you want to Upadte the Task : ")
                todo_list[n-1] = task
                print("Task Updated ...")
    elif operation == "DELETE":
        n = int(input("Enter number of task you want to Delete : " ))
        if todo_list:
            if n > initial or n < 0:
                print("Enter valid input ")
            else:
                todo_list.remove(todo_list[n-1])
                print("Task deleted")
                initial = initial - 1
    elif operation == "SHOW":
        for i in range(0 , initial):
            print(f"Task {i+1} :: {todo_list[i]} ")
        print("Choose Whatever you wanna do!!")
        
    elif operation == "DONE":
        print('You are saying you are done with work !!!  [ type "SURE" ]')
        sure = input()
        if sure == "SURE":
            check = False

"""
    A simple Todo List application.

    This application allows users to add, update, delete, and show tasks.
    It also allows users to mark tasks as done.

    Example:
    In terminal $ python Todo.py
    Enter Your name : Yakshi
    Welcome Yakshi
    Enter Number of tasks : 3
    Enter the operations " ADD , DELETE , UPDATE , DONE ,  SHOW" : ADD
    Enter the 1 task : Buy milk
    Enter the operations " ADD , DELETE , UPDATE , DONE ,  SHOW" : ADD
    Enter the 2 task : Walk the dog
    Enter the operations " ADD , DELETE , UPDATE , DONE ,  SHOW" : SHOW
    Task 1 :: Buy milk
    Task 2 :: Walk the dog
    Choose Whatever you wanna do!!
    Enter the operations " ADD , DELETE , UPDATE , DONE ,  SHOW" : UPDATE
    Enter number of task you want to update : 1
    Enter the task with which you want to Update the Task : Buy eggs
    Task Updated ...
    Enter the operations " ADD , DELETE , UPDATE , DONE ,  SHOW" : SHOW
    Task 1 :: Buy eggs
    Task 2 :: Walk the dog
    Choose Whatever you wanna do!!
    Enter the operations " ADD , DELETE , UPDATE , DONE ,  SHOW" : DONE
    You are saying you are done with work !!!  [ type "SURE" ]
    SURE
    """