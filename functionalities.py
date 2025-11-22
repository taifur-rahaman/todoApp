def add_todo():
    todo = input("Enter a Todo: ") + "\n"
    
    with open("todos.txt", "a") as file:
        file.write(todo)
        print("Todo has been added.")
    
    return todo

def edit_todo(todos):
    todo_number = int(input("Enter the number which you want to edit: "))
    new_todo = input("Enter the new Todo: ")
    todos[todo_number - 1] = new_todo
    print("Todo has been updated.")

def delete_todo(todos):
    todo_number = int(input("Enter the number which todo you want to delete: "))
    todos.pop(todo_number - 1)
    print("Todo has been deleted.")
    
    with open("todos.txt", "w") as file:
        file.writelines(todos)





