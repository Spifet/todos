def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file_get:
        todos_local = file_get.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)


if __name__ == "__main__":
    print(__name__)