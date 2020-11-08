""" 
    Create a function for each of the following, using any means possible without cutting corners.( no using of built-in function - we have to try our best)
        addition - this function takes two objects as argument, and returns their sum if they are numbers, that is a float or an int.
        subtraction - this function takes two objects as argument, returns the resut of subtracting the second from the first.
        division - this function takes two objects as argument, returns the result from dividing the first by the second. Remember that zero division is not allowed thus check if the second is zero.
        multplication - this function takes two objects as argument, returns the product of the two.

    Write a function, that takes a list of various objects as an argument, return a list of all the objects that are numbers ( that is integer and float).

    Write a function taking a list of various objects as argument, return the number of each object in the list. (This is also known as the frequency counter)

    Write a function that takes a list of integers as an argument, remove ( delete) any element that has the same parity as its index + 1 .( If the index + 1 is even and the element is even, remove the element. If element is odd and index + 1 is odd, remove element, except when the index is 0), looping n - 1 times, where n is the size of the list.

    s = [2, 6, 18, 11, 4]
    # 6 is removed - loop 1
    # index of 6, + 1 = 2

    s = [2, 18, 11, 4]
    # 18 is removed - loop 2
    # index of 18, + 1 = 2

    s = [2, 11, 4]
    # 11 is not removed - loop 3
    # index of 11, + 1 = 2

    s = [2, 11, 4]
    # 4 is not removed - loop 4
    # index of 4, + 1 = 3

    # final output
    s = [2, 11, 4]

    Write a function that takes a list of integers as input, then return a list with the same parity as the first element.
"""

############################# part 1 #############################
# this function checks if the argument passed is a number


def is_number(a):
    return type(a) in [int, float]


# the problem did not state what to return when either is not a number
# as such we'd return None


def addition(a, b):
    # if is_number(a) and is_number(b):
    #     return a + b
    # return None

    return a + b if is_number(a) and is_number(b) else None


def subtraction(a, b):
    return a - b if is_number(a) and is_number(b) else None


def division(a, b):
    return a / b if is_number(a) and is_number(b) and not b == 0 else None


def multiplication(a, b):
    return a * b if is_number(a) and is_number(b) else None


############################# part 2 #############################
# This function is supposed to return the number of different types of object
def filter_number(item=[]):
    return [i for i in item if type(i) in [int, float]]


############################# part 3 #############################

def freq_counter(items=[]):
    types = []
    count = []
    res = []

    for item in items:
        if type(item) not in types:
            types.append(type(item))

    size = len(types)

    count = size * [0]

    for item in items:
        if type(item) in types:
            count[types.index(type(item))] += 1

    for i in range(size):
        res.append((types[i], count[i]))

    return res


############################# part 4 #############################

def index_parity(items=[]):
    # i = 1
    # while True:
    #     size = len(items)
    #     if size > 2 and i < size:
    #         if (items[i] + 1) % 2 == items[i] % 2:
    #             del items[i]
    #         else:
    #             i += 1
    #     else:
    #         break

    # return items
    pass


# s = [2, 6, 18, 11, 4]
# print(index_parity(s))

# i = 1
# while True:
#     if len(s) > 2:
#         del s[i]
#     else:
#         break
# print(len(s))


############################# part 5 #############################

def same_parity(items=[]):
    first_item = items[0]
    pars = [first_item, ]

    for i in range(1, len(items)):
        if first_item % 2 == items[i] % 2:
            pars.append(items[i])

    return pars
