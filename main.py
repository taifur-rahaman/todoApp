import functionalities as func

todos = []

try:
    with open("todos.txt", "r") as file:
        todos = file.readlines()
except FileNotFoundError:
        todos = []

while True:
    user_action = input("1. Add Todo\n2. Show Todos\n3. Edit Todos\n4. Delete Todos\n5. Exit\nChoose an Action: ")
    
    match user_action:
        case "1":
            new_todo = func.add_todo()
            todos.append(new_todo)
            
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
            for todo in todos:
                print(f"{todos.index(todo) + 1} - {todo}") 
            func.delete_todo(todos)
        case "5":
            print("Exiting the Application.")
            break
        case _:
            print("Invalid Input. Please Try again")