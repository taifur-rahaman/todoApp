import functionalities as func

print("Welcome to the Todo App!")

todos = [] # Initializing an empty list to store todos

try:
    with open("todos.txt", "r") as file:
        todos = file.readlines()
except FileNotFoundError:
    open("todos.txt", "w").close()


while True:
    user_action = input("Choices:\n1. Add Todo\n2. Show Todos\n3. Edit Todo\n4. Delete Todo\n5. Exit\nChoose an action: ")
    
    match user_action:
        case "1":
            new_todo = func.add_todo()
            todos.append(new_todo)
        case "2":
            func.show_todos(todos)
        case "3":
            func.edit_todo(todos)
        case "4":
            func.delete_todo(todos)
        case "5":
            print("Exiting the Todo Application. Goodbye!")
            break
        case _:
            print("Invalid Choice. Please Try Again")