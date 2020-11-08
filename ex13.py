# ex13.py
'''
* Implement a function known as all(iterable). This function returns True if all of
the elements of the iterable is True or the iterable is empty, else False.

* Implement a function known as any(iterable) . This function returns True if any of
 the elements of the iterable is True . If the iterable is empty, return False.

* Implement the abs(x) function where x , is a number.

* Implement a function that returns the minimum and maximum numbers in given list. 
Don't use the built-in function min and max.
'''


def all(iterable=[]):
    for i in iterable:
        if not i:
            return False

    return True


def any(iterable):
    for i in iterable:
        if i:
            return True

    return False


# since `abs` is a built-in function, I shall append `_` to mine as `abs_`
def abs_(n):
    result = 0

    try:
        if n < 0:
            result = n * -1
        else:
            result = n
    except Exception:
        print('Enter a number please')
    finally:
        return result


def sort_list(item=[]):
    item_length = len(item)
    
    if item_length > 1:
        for i in range(item_length):
            for j in range(item_length - 1):
                if item[j] > item[j + 1]:
                    item[j], item[j + 1] = item[j + 1], item[j]

    return item


def min_max(iterable=[]):
    result = 0

    try:
        sorted_iterable = sort_list(iterable)
        result = (sorted_iterable[0], sorted_iterable[len(iterable) - 1])
    except Exception:
        print('The iterable must not be empty')
    finally:
        return result
