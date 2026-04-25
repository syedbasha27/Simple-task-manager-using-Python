import json


#loading from json file
def load_tasks():

    global tasks
    try:
      with open("/content/drive/MyDrive/tasks.json","r") as file:
        tasks=json.load(file)

    except:
      tasks=[]

#saving into the json file
def save_tasks():
  with open("/content/drive/MyDrive/tasks.json","w") as file:
    json.dump(tasks,file)



#adding the task
def add_task():

  task=input("Enter the task name:").lower()
  priority=input(f"Enter the priority of task {task} (high/low/medium):").lower()
  task_id=len(tasks)+1
  new={"id":task_id,
       "task":task,
       "priority":priority}
  tasks.append(new)
  save_tasks()
while True:

  add_task()
  choice=input("want to add more tasks(yes/no):").lower()

  if choice!="yess":
    break
#print(tasks)



#shows the saved tasks
def show_tasks():
  for i in range(len(tasks)):
    print(tasks[i])
show_tasks()


#removes the tasks
def remove_task():
  idr=int(input("enter the id of the task to remove:"))
  for task in tasks:
    if task["id"]==idr:
      tasks.remove(task)
      print("task removed")
      return
  print(f"no task with id:{idr}")  
remove_task()     

#sorting of tasks  based on priority
priority_order={"high":"1","medium":"2","low":"3"}

def sort_tasks():
  tasks.sort(key=lambda x:priority_order[x["priority"]])
sort_tasks()  


#recommending tasks based on user keyword

def recommend_task():
  keyword=input("enter the keyword:")

  for task in tasks:
    if keyword.lower() in task["task"]:
      print("Recommended",task["task"])
      return
  print("try with another keyword")  
recommend_task()





#menu with which user interacts

def menu():
  while True:
    print("1. ADD Task")
    print("2. REMOVE Task")
    print("3. SHOW Task")
    print("4. SORT Task")                
    print("5. RECOMMEND Task")

    choice=int(input("Enter what to do:"))
    match choice:
       case 1:
         add_task()
       case 2:
          remove_task()
       case 3:
          show_tasks()
       case 4:
          sort_tasks()
       case 5:
           recommend_task()
       case _:
           print("enter a valid number(1 to 5):")

menu()      








#output

1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:1
Enter the task name:hiking
Enter the priority of task hiking (high/low/medium):high
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:1
Enter the task name:scrolling
Enter the priority of task scrolling (high/low/medium):low
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 9, 'task': 'coding', 'priority': 'high'}
{'id': 11, 'task': 'coding', 'priority': 'high'}
{'id': 13, 'task': 'playing', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 15, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 12, 'task': 'hiking', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:4
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 9, 'task': 'coding', 'priority': 'high'}
{'id': 11, 'task': 'coding', 'priority': 'high'}
{'id': 13, 'task': 'playing', 'priority': 'high'}
{'id': 12, 'task': 'hiking', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 15, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:15
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 9, 'task': 'coding', 'priority': 'high'}
{'id': 11, 'task': 'coding', 'priority': 'high'}
{'id': 13, 'task': 'playing', 'priority': 'high'}
{'id': 12, 'task': 'hiking', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:5
enter the keyword:oo
Recommended cooking
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:13
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 9, 'task': 'coding', 'priority': 'high'}
{'id': 11, 'task': 'coding', 'priority': 'high'}
{'id': 12, 'task': 'hiking', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:5
enter the keyword:c
Recommended coding
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:9
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 11, 'task': 'coding', 'priority': 'high'}
{'id': 12, 'task': 'hiking', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:11
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 12, 'task': 'hiking', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:12
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 14, 'task': 'reading', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:14
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 16, 'task': 'scrolling', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:2
enter the id of the task to remove:16
task removed
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
Enter what to do:3
{'id': 4, 'task': 'coding', 'priority': 'high'}
{'id': 13, 'task': 'hiking', 'priority': 'high'}
{'id': 2, 'task': 'reading', 'priority': 'medium'}
{'id': 3, 'task': 'writing', 'priority': 'medium'}
{'id': 12, 'task': 'study', 'priority': 'medium'}
{'id': 8, 'task': 'cooking', 'priority': 'low'}
{'id': 14, 'task': 'scrolling', 'priority': 'low'}
1. ADD Task
2. REMOVE Task
3. SHOW Task
4. SORT Task
5. RECOMMEND Task
