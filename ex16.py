""" Implement your own version of

- Intersection
- Union
- difference
- symmetric_difference
- delete like discard or remove ( ignore the KeyError thing)
- update
- isset - it checks if a sequence has no duplicate ( remember `count` )
 """


def intersection(set_a, set_b):
    # return [element for element in set_a if element in set_b]

    intersected_elements = []

    for element in set_a:
        if element in set_b:
            intersected_elements.append(element)

    return intersected_elements


def union(set_a, set_b):
    union_elements = set_a[:]

    for element in set_b:
        if element not in set_a:
            union_elements.append(element)

    return union_elements


def difference(set_a, set_b):
    difference_elements = []

    for element in set_a:
        if element not in set_b:
            difference_elements.append(element)

    return difference_elements


def symmetric_difference(set_a, set_b):
    # # union - intersection = difference(union, intersection)
    # union_elements = union(set_a, set_b)
    # intersection_elements = intersection(set_a, set_b)

    # symmetric_difference_elements = difference(
    #     union_elements, intersection_elements)

    # return symmetric_difference_elements

    # differenceAB + differenceBA = union(differenceA_B, differenceB_A)
    differenceA_B = difference(set_a, set_b)
    differenceB_A = difference(set_b, set_a)

    symmetric_difference_elements = union(
        differenceA_B, differenceB_A)

    return symmetric_difference_elements


def delete(set_item=[], element=0):
    if element in set_item:
        set_item.remove(element)

    return set_item


def isset(set_item=[]):
    for element in set_item:
        if set_item.count(element) > 1:
            return False

    return True
