def add_todo(todos):
    todo = input("Enter a Todo: ")
    todos.append(todo)
    print(f"{todo} has been added to your list")

def edit_todo(todos):
    todo_number = int(input("Enter the number which you want to edit: "))
    new_todo = input("Enter the new Todo: ")
    todos[todo_number - 1] = new_todo
    print("Todo has been updated.")