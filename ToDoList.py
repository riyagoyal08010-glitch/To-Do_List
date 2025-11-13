tasks = []
while True:
   print("Welcome! to To-Do list ")
   print("1. Show to-do list")
   print("2. Add tasks in list")
   print("3. Remove tasks from the list")
   print("4. Exit")
   a = int(input("\n Enter your choice(1,2,3,4): "))
   if a == 1:
      print(f"\nYour to-do list: \n{tasks}")
      if tasks == []:
        print("\nNo task added yet!")
   elif a ==2:
     b = input("\nEnter the task you want to achieve: ")
    
     tasks.append(b)
   
     print(f"\nYour desired task : {b} has been added in list successfully")
     print(f"\n the updated to-do list:{tasks}")
   elif a == 3:
      c = input("\nEnter the task you want to remove: ")
      if c in tasks:
        tasks.remove(c)
        print(f"\nYour updated list is ; {tasks}")
      else:
        print("Task not found")
   else:
    print("\nYou have been exited out from the to do list")
    break





