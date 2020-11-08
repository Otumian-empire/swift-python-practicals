""" Given a list, whose elements are also list ( talking about nested list), write a function that sorts this list and it list elements if possible
 """


# We will use this function to sort the content of the nested list
def sort_inner_list(item=[]):
    item_length = len(item)

    if item_length > 1:
        for i in range(item_length):
            for j in range(item_length - 1):
                if item[j] > item[j + 1]:
                    # simple way to swap - instead of creating a temp var
                    item[j], item[j + 1] = item[j + 1], item[j]

    return item


# the question is how not clear, how are the nested list going to be sorted
# by the first elements, by the size of the list, by the sum of the content
# of the nested list?
# Basically, I am to choose how to sort it by the size of elements in the
# nested list


def sort_outer_list_by_size(item=[]):
    item_length = len(item)

    if item_length > 1:
        for i in range(item_length):
            for j in range(item_length - 1):
                if len(item[j]) > len(item[j + 1]):
                    # swap items
                    item[j], item[j + 1] = item[j + 1], item[j]

    return item


def sort_nested_items(items=[]):
    sorted_inner_list = [sort_inner_list(i) for i in items]
    sorted_outer_list = sort_outer_list_by_size(sorted_inner_list)

    return sorted_outer_list
