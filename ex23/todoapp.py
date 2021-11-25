"""
    push all the softwares to github
    using git, create a todo app and push the final result to github
"""

import os
import sys

todos = []


def clear_screen():
    _ = os.system('cls' if os.name == 'nt' else 'clear')


def is_int_index(index):
    try:
        index = int(index)
    except ValueError:
        print("index must be an int")
        sys.exit()

    return index


def is_bounded_index(index):
    return index >= 0 and index < len(todos)


class TodoApp:

    def add(self, task=''):
        if task:
            todos.append(task)
            return True

        return False

    def readall(self):
        return todos

    def read(self, index):
        index = is_int_index(index)

        if is_bounded_index(index):
            return todos[index]

        return ''

    def update(self, index, task):
        index = is_int_index(index)

        if is_bounded_index(index):
            todos[index] = task
            return True

        return False

    def deleteall(self):
        todos.clear()

    def delete(self, index):
        index = is_int_index(index)

        if is_bounded_index(index):
            del todos[index]
            return True

        return False


message = """TODO app
1 - add item
2 - read all items
3 - read item at index
4 - update item at index with task
5 - delete all items
6 - delete item at index
7 - exit
"""

while True:
    clear_screen()

    print(message)
    command = input("command >>> ")

    if command == '1':
        task = input("task >>> ")

        if TodoApp().add(task):
            print("Task added")
        else:
            print("Task could not added, task is empty")

    elif command == '2':
        todos_ = TodoApp().readall()

        for i in range(len(todos_)):
            print(i, todos[i])

    elif command == '3':
        index = input("index >>> ")
        task = TodoApp().read(index)
        print(task)

    elif command == '4':
        index = input("index >>> ")
        print(f'Task: {todos[int(index)]}')
        task = input("task >>> ")

        if TodoApp().update(index, task):
            print("Task updated")
        else:
            print("Task could not be updated, maybe, index is out of bounds")

    elif command == '5':
        TodoApp().deleteall()
        print("Deleted all task")

    elif command == '6':
        index = input("index >>> ")
        if TodoApp().delete(index):
            print("Task deleted")
        else:
            print("Task could not be deleted, maybe, index is out of range")

    else:
        clear_screen()
        break

    input("Hit enter to continue... ")

sys.exit()
