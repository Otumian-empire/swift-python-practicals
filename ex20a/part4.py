""" 
Write a program that allows creating, reading and updating of the content of a file using OOP.  """

import os

ERROR_MESSAGE = "There was an error, please check the file path "
ERROR_MESSAGE += "or pass the absolute path"


class CRUDFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, 'r') as read_file_object:
                return read_file_object.read()

        except (Exception, FileNotFoundError) as e:
            print(ERROR_MESSAGE)
            return None

    def reads(self, size):
        try:
            with open(self.filename, 'r') as read_file_object:
                return read_file_object.read(size)

        except (Exception, FileNotFoundError) as e:
            print(ERROR_MESSAGE)
            return None

    def readlines(self):
        try:
            with open(self.filename, 'r') as read_file_object:
                return read_file_object.readlines()

        except (Exception, FileNotFoundError) as e:
            print(ERROR_MESSAGE)
            return None

    def update(self, content):
        try:
            with open(self.filename, 'a+') as update_file_object:
                return update_file_object.write(content)

        except (Exception, FileNotFoundError) as e:
            print(ERROR_MESSAGE)
            return None

    def create(self, content):
        try:
            with open(self.filename, 'w+') as create_file_object:
                return create_file_object.write(content)

        except (Exception, FileNotFoundError) as e:
            print(ERROR_MESSAGE)
            return None

    def delete(self):
        try:
            return os.remove(self.filename)
        except (Exception, FileNotFoundError) as e:
            print(ERROR_MESSAGE)
            return None
