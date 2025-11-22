todos = []

while True:
    user_action = int(input("1. Add Todo\n2. Show Todos\n3. Exit\nChoose an Action: "))
    
    match user_action:
        case 1:
            todo = input("Enter a Todo: ")
            todos.append(todo)
            print(f"{todo} has been added to your list")
        case 2: 
            for item in todos:
                print(item)
        case 3:
            print("Exiting the Application.")
            break
        case _:
            print("Invalid Input. Please Try again")
            
            