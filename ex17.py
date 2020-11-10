""" 
    Write a program that creates a dynamic user profile. Make use of the input(). Make use of setdefault.
    Write a function that removes items with duplicate values
    Write a function that reverses a dictionary
    Write a function that sorts a dictionary by Key then value ( 2 functions)
    Write a function that takes a dictionary as an argument, return another dictionary that has the frequencey of the length of the value, if value is int or float, frequencey is number of digits. Keep the keys of the old as the new.
"""


# dynamic user profile
def dynamic_profile():
    fullname = input("Enter fullname: ")
    age = input("Enter age: ")
    job = input("Enter job: ")

    print(f"Full Name: {fullname}")
    print(f"Age: {age}")
    print(f"Job: {job}")


# remove duplicates from dict
def remove_duplicates(dict_item=dict()):
    new_dict = {}

    for key, val in dict_item.items():
        dict_values = list(dict_item.values())

        if dict_values.count(val) > 1:
            dict_item[key] = None

    for key, val in dict_item.items():
        if val != None:
            new_dict[key] = val

    return new_dict


# reverse dictionary
def reverse_dict(dict_item=dict()):
    new_dict = {}
    keys = list(dict_item.keys())

    for key in range(len(keys) - 1, -1, -1):
        new_dict[keys[key]] = dict_item[keys[key]]

    return new_dict


# sort dictionary by key
def sort_dict_key(dict_item=dict()):
    new_dict = {}
    keys = list(dict_item.keys())

    item_length = len(keys)

    if item_length > 0:
        for i in range(item_length):
            for j in range(item_length - 1):
                if keys[j] > keys[j + 1]:
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]

        for i in range(item_length):
            new_dict[keys[i]] = dict_item[keys[i]]

    return new_dict


# sort dictionary by value
def sort_dict_val(dict_item=dict()):
    new_dict = {}
    keys = list(dict_item.keys())

    item_length = len(keys)

    if item_length > 0:
        for i in range(item_length):
            for j in range(item_length - 1):
                if dict_item[keys[j]] > dict_item[keys[j + 1]]:
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]

        for i in range(item_length):
            new_dict[keys[i]] = dict_item[keys[i]]

    return new_dict


# return a dictionary of the number of digits in the value of a dictionary
def dict_freq(dict_item=dict()):
    new_dict = {}

    for key, val in dict_item.items():
        num_digits = len(str(val))

        if type(val) == float:
            num_digits -= 1

        new_dict[key] = num_digits

    return new_dict
