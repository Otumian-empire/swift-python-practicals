"""
Write a function that returns the number of lines and characters on each line in the entire file.

Write a function that returns the document statistics of a give file. The document statistics are number of lines, number of words, number of characters with space and witout space. Lines are separated by newlines, words are separated by spaces.

    file name
    ---------
    Lines      - 8
    Words      - 71
    Char (ws)  - 403
    Char (wos) - 337

Write a program that allows creating, reading and updating of the content of a file.
"""


def num_line_char(filename):
    with open(filename, 'r') as file_obj:
        content_lines = file_obj.readlines()

        num_lines = len(content_lines)
        num_chars = 0

        for line in content_lines:
            num_chars += len(line)

        return num_lines, num_chars


def doc_stats(filename):
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

        doc_stat_info = f"""
        {filename}
        {'_'*len_file_name}
        Lines      - {num_lines}
        Words      - {num_words}
        Char (ws)  - {num_chars_space}
        Char (wos) - {num_chars_no_space}
        """

        return doc_stat_info


# pass create, read and update to do respectively
def cru_file(filename, mode, content=""):
    try:
        if mode == "create":
            with open(filename, 'w+') as create_file_obj:
                print(content, file=create_file_obj)
        elif mode == "update":
            with open(filename, 'a+') as update_file_obj:
                print(content, file=update_file_obj)
        elif mode == "read":
            with open(filename, 'r') as read_file_obj:
                print(read_file_obj.read())
        else:
            print("Unknown mode")
    except Exception as e:
        print(e)
