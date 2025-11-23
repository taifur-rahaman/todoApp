def add_todo():
    todo = input("Enter a new todo: ") + "\n"
    
    with open("todos.txt", "a") as file:
        file.writelines(todo)
    
    return todo

def show_todos(todos):
    print("Your Todos:\n")
    for todo in todos:
        print(f"{todos.index(todo) + 1} - {todo.strip('\n')}")
    print("\n")

def edit_todo(todos):
    show_todos(todos)
    todo_number = int(input("Enter the number of the todo to edit: "))
    
    with open("todos.txt", "r") as file:
        todos = file.readlines()
    
    new_todo = input("Enter the new todo: ") + "\n"
    todos[todo_number - 1] = new_todo
    
    with open("todos.txt", "w") as file:
        file.writelines(todos)

def delete_todo(todos):
    show_todos(todos)
    
    with open("todos.txt", "r") as file:
        todos = file.readlines()
        
    todo_number = int(input("Enter the number of the todo to delete: "))
    todos.pop(todo_number - 1)
    
    with open("todos.txt", "w") as file:
        file.writelines(todos)


