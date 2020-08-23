""" 
* Write a program to take input from the user, print the input, 
    seperated by a short-dash, `-` , and the length of the string. 
    `Eg: input='Doe', output=Doe - 3` 

* Write a program that reads data from the user and converts the data to lower case, upper case, title and capitalize.
"""

"""
Problem Summary:
    a program that takes input from the user,
    prints the input, seperated by a short-dash, `-` ,
    and the length of the input. 
    `Eg: input='Doe', output=Doe - 3` 
Analysis:
    input: input from user, user_input 
    output: user input - length of user input, user_input - size of user_input
    process: size of user_input = number of character in user input
Design:
    user_input: Enter your first name
    user_input_size: size of user_input

    display: {user_input} - user_input_size
"""

user_input = input('Enter your first name: ') or ''
user_input_size = len(user_input)

print(f'{user_input} - {user_input_size}')

