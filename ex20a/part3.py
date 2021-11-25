""" 
Write a class for a document statistics. Refer to the exercise 19 to read about document statistics.
"""


class DocStat:

    def __init__(self, filename):
        self.filename = filename
        self.len_filename = len(filename)
        self.file_content = []

        self.read_file_content()

    def read_file_content(self):
        with open(self.filename, 'r') as file_obj:
            self.file_content = file_obj.readlines()

    def get_num_lines(self):
        return len(self.file_content)

    def get_num_words(self):
        num_words = 0

        for line in self.file_content:
            num_words += len(line.split(" "))

        return num_words

    def get_num_char_with_space(self):
        num_chars_space = 0

        for line in self.file_content:
            num_chars_space += len(line)

        return num_chars_space

    def get_num_char_with_no_space(self):
        num_chars_no_space = 0

        for line in self.file_content:
            for word in line.split(" "):
                num_chars_no_space += len(word)

        return num_chars_no_space

    def print_doc_stat(self):
        doc_stat_info = f"""
            {self.filename}
            {'_'* self.len_filename}
            Lines      - {self.get_num_lines()}
            Words      - {self.get_num_words()}
            Char (ws)  - {self.get_num_char_with_space()}
            Char (wos) - {self.get_num_char_with_no_space()}
            """

        return doc_stat_info
