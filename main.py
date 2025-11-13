user_promt = "Enter a Todo: "

todos = []

while True:
    choice = input("Do you want to add a todo? (y/n): ")
    if choice.lower() != 'y':
        break
    else: 
        todo = input(user_promt)
        todos.append(todo)
        print(todos)
    
print(f"You have {len(todos)} todos in the list.")