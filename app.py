def task():
    task = [] #empty list
    print("----Welocome to the To_Do_List App---- ")

    tasd_numb = int(input("Enter the Task number's : ")) #total task number's
    for i in range(tasd_numb):
        task_name = input(f"Enter task {i+1} :")
        task.append(task_name)
    
    while True:
        action_input = int(input("Enter 1 for Add\nEnter 2 for Delete\nEnter 3 for Update\nEnter 4 for View\nEnter 5 for Exit/Stop:  "))

        if action_input == 1:
            new_task = input("Enter Task for Add: ")
            task.append(new_task)
            print(f"Task \"{new_task}\" added successfuly.")
        elif action_input == 2:
            del_task = input("Enter Task for Delete: ")
            if del_task in task:
                task.remove(del_task)
                print(f"Successfuly Task {del_task} deleted!")
            else: 
                print("Enter Valid Task!")
        elif action_input == 3:
            updated_task = input("Enter which Task to Update: ")
            if updated_task in task:
                new_task = input("Enter new Task: ")
                ind =  task.index(updated_task)
                task[ind] = new_task
            print("No Such Task Found!!")
        elif action_input == 4:
            print(task)
        elif action_input == 5:
            break
        else:
            print("Enter Valid Number")


task()