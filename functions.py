FILEPATH = "todos.txt"   #THIS IS A CONSTANT AS IS IN CAPITAL LETTERS


def get_todos(filepath=FILEPATH):   #here we are using parameters to pass the files path
    """ this is how create docs string for functions, this can help to explain parts of the code"""  # this is called docs string which helps to identify what the fucntion does
    with open(filepath, 'r') as file_local:  # a function that will return todos as readlines will will read the file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):   #here we are using args default, which means that by default the filepath will be todos.txt, this can be change as well
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)  # no return is used as this only completes a function to overwirte the file