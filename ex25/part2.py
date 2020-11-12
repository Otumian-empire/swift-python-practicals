""" Write a script that returns the document statistics of a give file. The document statistics are number of lines, number of words number of characters with space and witout space.

file name
---------
Lines      - 8
Words      - 71
Char (ws)  - 403
Char (wos) - 337

Write these into a database """


import sqlite3

DATABASENAME = "file_db"


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
        sql_query = """CREATE TABLE IF NOT EXISTS "file_stat2" (
                            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            "file_name" TEXT NOT NULL,
                            "num_lines" INTEGER NOT NULL,
                            "num_words" INTEGER NOT NULL,
                            "chars_ws" INTEGER NOT NULL,
                            "chars_wos" INTEGER NOT NULL,
                            "created_at" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
                    """

        if self.cur != None:
            self.cur.execute(sql_query)

        if self.cur != None:
            self.conn.commit()
            return True

        return False

    def read_file_stats(self):
        sql_query = """
            SELECT 
                id, file_name, num_lines, num_words, chars_ws, chars_wos, created_at 
            FROM file_stat2;
        """

        rows = []

        self.cur.execute(sql_query)

        if self.cur != None:
            rows = self.cur.fetchall()

        return rows

    def save_file_stat(self, file_name, num_lines, num_words, chars_ws, chars_wos):
        sql_query = """
            INSERT INTO 
                file_stat2(file_name, num_lines, num_words, chars_ws, chars_wos)
            VALUES (?, ?, ?, ?, ?)
        """

        values = (file_name, num_lines, num_words, chars_ws, chars_wos)

        if self.cur != None:
            self.cur.execute(sql_query, values)

        if self.cur != None:
            self.conn.commit()

            return True

        return False


def doc_stats(filename=""):
    if filename:
        try:
            with open(filename, 'r') as file_obj:
                len_file_name = len(filename)
                content_lines = file_obj.readlines()

                num_lines = len(content_lines)

                num_words = 0
                for line in content_lines:
                    num_words += len(line.split(" "))

                num_chars_space = 0
                for line in content_lines:
                    num_chars_space += len(line)

                num_chars_no_space = 0
                for line in content_lines:
                    for word in line.split(" "):
                        num_chars_no_space += len(word)
                DB = FileStatDB()

                if DB.create_file_stat_tb():
                    if DB.save_file_stat(
                            filename, num_lines, num_words,
                            num_chars_space, num_chars_no_space):

                        rows = DB.read_file_stats()

                        for row in rows:
                            print(row)

                    else:
                        print("File stat not saved")
        except FileNotFoundError:
            print("Please provide an existing file path")
        except UnicodeDecodeError:
            print("Please a file other than a binary")

    else:
        print("File name is required")

# call doc_stats and pass the file path
# this will print an error message if there was an error
# else print the content of the database table file_stat2
