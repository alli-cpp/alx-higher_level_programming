#!/usr/bin/python3

"""
Module that executes a function that appends a line
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file, after each
    line containing a specific string
    """
    with open(filename, encoding="utf8") as my_file:
        line_list = my_file.readlines()
        new_content = ""
        for line in line_list:
            new_content += line
            if search_string in line:
                new_content += new_string
    with open(filename, "w", encoding="utf8") as f:
        f.write(new_content)
