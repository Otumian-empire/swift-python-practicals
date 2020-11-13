""" Write a scripts that backs the content of a file up. Save the back up in the database.
"""

import sqlite3
import sys

DATABASENAME = "file_db"


class FileBackUp:

    def __init__(self):
        try:
            self.conn = sqlite3.connect(DATABASENAME)
        except:
            self.conn = None

    def _create_tb(self):
        sql_query = """
            CREATE TABLE IF NOT EXISTS "bkpfile" (
                "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                "file_name" TEXT NOT NULL UNIQUE,
                "file_content" Text NOT NULL,
                "created_at" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """

        try:
            cur = self.conn.cursor()
            cur.execute(sql_query)

            if cur == None:
                print("Table not available, please create it manually")
            else:
                self.conn.commit()

        except Exception as e:
            print("Error")

    def _insert(self, file_name=""):
        try:
            if file_name:
                self._create_tb()

                with open(file_name, "r") as file_obj:
                    file_content = file_obj.read()

                    sql_query = "INSERT INTO bkpfile(file_name, file_content) VALUES(?, ?)"
                    values = (file_name, file_content)

                    cur = self.conn.cursor()
                    cur.execute(sql_query, values)

                    if cur != None:
                        self.conn.commit()
                        print("File backup created")
                    else:
                        print("File backup unsuccessful")

            else:
                print("File name is required for backup")

        except FileNotFoundError:
            print("Please provide an existing file path")
        except UnicodeDecodeError:
            print("Please a file other than a binary")
        except sqlite3.IntegrityError:
            # update rather
            # print("update rather")
            self._update(file_name)

    def _recover_file(self, file_name=""):
        try:
            if file_name:
                sql_query = "SELECT file_content FROM bkpfile WHERE file_name =?"
                values = (file_name, )

                cur = self.conn.cursor()
                cur.execute(sql_query, values)

                if cur == None:
                    print("Could not read file")
                else:

                    # create this recovery file as recovery_<file_name>
                    file_content = cur.fetchone()[0]

                    with open(f"recovery_{file_name}", "w+") as recovery_file_obj:
                        print(file_content, file=recovery_file_obj)
                        print("File recovery successful")

            else:
                print("File name is required for recovery")
        except FileNotFoundError:
            print("Please provide an existing file path")
        except UnicodeDecodeError:
            print("Please a file other than a binary")

    def _read_all_bkpfile(self):
        try:
            sql_query = "SELECT id, file_name, created_at FROM bkpfile"

            cur = self.conn.cursor()
            cur.execute(sql_query)

            if cur != None:
                rows = cur.fetchall()

                if len(rows) > 0:
                    for row in rows:
                        print(row)
                else:
                    print("There are no backedup files")

            else:
                print("File backup unsuccessful")

        except sqlite3.Error as e:
            print(e)

    def _update(self, file_name=""):
        try:
            if file_name:
                with open(file_name, "r") as file_obj:
                    file_content = file_obj.read()

                    sql_query = """
                        UPDATE
                            bkpfile
                        SET
                            file_content = ?,
                            created_at = CURRENT_TIMESTAMP
                        WHERE
                            file_name = ?;"""

                    values = (file_content, file_name)

                    cur = self.conn.cursor()
                    cur.execute(sql_query, values)

                    if cur != None:
                        self.conn.commit()
                        print("File backup updated")
                    else:
                        print("File backup update unsuccessful")

            else:
                print("File name is required for backup")

        except FileNotFoundError:
            print("Please provide an existing file path")
        except UnicodeDecodeError:
            print("Please a file other than a binary")


if __name__ == "__main__":
    # backup, -b
    # recover, -r
    # no flag passed: read the save backups

    # TODO: Add deleting of backup
    # TODO: Find a better to save the file content in the database,
    # think security and efficiency

    fbkp = FileBackUp()

    if len(sys.argv) > 1:
        try:
            flag = sys.argv[1].lower()

            if flag in ["backup", "-b", "recover", "-r"]:
                file_name = sys.argv[2]

                if flag in ["backup", "-b"]:
                    fbkp._insert(file_name)
                elif flag in ["recover", "-r"]:
                    fbkp._recover_file(file_name)

            else:
                print(
                    f"Unknown flag, {flag}. Pass: backup, -b for \
                        backup/update and recover, -r for recovery")

        except:
            print("flag and filename required")

    else:
        fbkp._read_all_bkpfile()
