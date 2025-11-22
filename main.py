import functionalities as func

todos = []

while True:
    user_action = input("1. Add Todo\n2. Show Todos\n3. Edit Todos\n4. Exit\nChoose an Action: ")
    
    match user_action:
        case "1":
            func.add_todo(todos)
        case "2":
            print("Your Todos:")
            for item in todos:
                print(f"{todos.index(item) + 1} - {item}")
            print("\n")
        case "3":
            for todo in todos:
                print(f"{todos.index(todo) + 1} - {todo}") 
            func.edit_todo(todos)
        case "4":
            print("Exiting the Application.")
            break
        case _:
            print("Invalid Input. Please Try again")