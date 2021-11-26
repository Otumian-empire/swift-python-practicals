"""
Fix this code base on the error message generated:

try:
    numerator = input('Enter the numerator: ')
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator + rate

    print(f"The result is {result}")
except Exception as z:
    print(f'error: {z}')

"""


# Test the code to see the error generated
# Enter the numerator: 3
# Enter the denominator: 5
# error: unsupported operand type(s) for /: 'str' and 'int'

# this is actually adding a string to an int.
# Fix by casting the numerator to int

# After the type-cast-fix, there was another error
# Enter the numerator: 3
# Enter the denominator: 5
# error: name 'rate' is not defined

# either remove rate or assign a value to rate
# I will remove it, the code did not say what type of value rate will be
# of course, rate can be a number. Here, we are suppose to fix the code
# and that was it. If you choose to add rate, then assign it a value


try:
    numerator = int(input('Enter the numerator: '))
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator

    print(f"The result is {result}")
except Exception as e:
    print(f'error: {e}')
