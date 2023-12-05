def get_todo(filepath="todos.txt"):
    with open(filepath,'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local

def write_todo(p_todo,filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(p_todo)


if __name__ == "__main__":
    print("Hello")
    print(get_todo())