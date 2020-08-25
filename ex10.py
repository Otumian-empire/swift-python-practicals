# ex10.py
'''
Write a program that checks if a given integer input is a multiple 
of 2, 3 or both 2 and 3 and then print what multiple it is with the input.

# the code should behave this way

# input = 4
# output = 4 is a multitple of 2

# input = 6
# output = 6 is a multitple of 2 and 3

# input = 9
# output = 9 is a multitple of 3

# input = 18
# output = 18 is a multitple of 2 and 3
'''

try:
    user_number = int(input("Enter a number: "))

    if user_number % 2 == 0 and user_number % 3 == 0:
        print(f'{user_number} is a multitple of 2 and 3')
    elif user_number % 2 == 0:
        print(f'{user_number} is a multitple of 2')
    elif user_number % 3 == 0:
        print(f'{user_number} is a multitple of 3')

except ValueError as e:
    print(f"Please enter a number: {str(e)}")
