# Create a database (file_db) and a table (file_stat)
# table has id, file_name, num_chars, num_lines and created_at
# id is primary key, file_name and created_at are text
# num_chars and num_lines are integer. No field is unique
# to allow multiple rows of the same file
# refer to file_db.sql for more.
# To run this app, import FileStatApp

import sqlite3

DATABASENAME = "file_db"


class FileStat:
    """ A script that collects a file's name, the number of characters in the entire file and the number of lines in the file to be saved in a database. """

    def __init__(self, filename):
        self.filename = filename

    @property
    def num_chars(self):
        """ returns the number of characters in the entire file """
        _num_chars = 0

        with open(self.filename, 'r') as file_obj:
            _num_chars = len(file_obj.read())

        return _num_chars

    @property
    def num_lines(self):
        """ returns the number of characters in the entire file """
        _num_lines = 0

        with open(self.filename, 'r') as file_obj:
            _num_lines = len(file_obj.readlines())

        return _num_lines


class FileStatDB:
    """ A script the saves a file's name, number of characters and lines in the entire file """

    def __init__(self):
        try:
            self.conn = sqlite3.connect(DATABASENAME)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            self.cur = None
            print(e)

    def create_file_stat_tb(self):
        sql_query = """CREATE TABLE IF NOT EXISTS "file_stat" (
                        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        "file_name"	TEXT NOT NULL,
                        "num_chars"	INTEGER NOT NULL,
                        "num_lines"	INTEGER NOT NULL,
                        "created_at"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                    );"""

        if self.cur != None:
            self.cur.execute(sql_query)

        if self.cur != None:
            self.conn.commit()
            return True

        return False

    def read_file_stats(self):
        sql_query = "SELECT id, file_name, num_chars, num_lines FROM file_stat;"
        rows = []

        self.cur.execute(sql_query)

        if self.cur != None:
            rows = self.cur.fetchall()

        return rows

    def save_file_stat(self, filename, num_chars, num_lines):
        sql_query = "INSERT INTO file_stat(file_name, num_chars, num_lines) VALUES(?, ?, ?)"
        values = (filename, num_chars, num_lines)

        if self.cur != None:
            self.cur.execute(sql_query, values)

        if self.cur != None:
            self.conn.commit()

            return True

        return False


class FileStatApp:
    """ Driver code  """

    def __init__(self):
        self.fs_db = FileStatDB()

    def read_stats(self):
        if self.fs_db.create_file_stat_tb:
            rows = self.fs_db.read_file_stats()

            for row in rows:
                print(row)
        else:
            print("Could not read file stats, probably \
                because the table was not created before hand.\
                    Try create a stat first, which will create\
                         the table if it was not created initially.")

    def create_stat(self, filename=""):
        if filename:
            self.fs = FileStat(filename)

            if self.fs_db.save_file_stat(self.fs.filename,
                                         self.fs.num_chars,
                                         self.fs.num_lines):
                print("File stat created")
            else:
                print("File stat no created")
        else:
            print("File name is required")
