# Try to implement the practicals in Exercise 14 ( List) using tuple."""

############################# part 1 #############################


# this function checks if the argument passed is a number
def is_number(a):
    return type(a) in [int, float]


def addition(a, b):
    return a + b if is_number(a) and is_number(b) else None


def subtraction(a, b):
    return a - b if is_number(a) and is_number(b) else None


def division(a, b):
    return a / b if is_number(a) and is_number(b) and b != 0 else None


def multiplication(a, b):
    return a * b if is_number(a) and is_number(b) else None


############################# part 2 #############################
def filter_number(item=tuple()):
    res = tuple()
    for i in item:
        if is_number(i):
            res += (i,)
    return res


############################# part 3 #############################
def freq_counter(items=tuple()):
    types = tuple()
    count = tuple()
    res = tuple()

    for item in items:
        if type(item) not in types:
            types += (type(item),)

    size = len(types)

    count = size * [0]

    for item in items:
        if type(item) in types:
            count[types.index(type(item))] += 1

    for i in range(size):
        res += ((types[i], count[i]),)

    return res


############################# part 4 #############################
def index_parity(items=tuple()):
    if len(items) > 1:
        i = 1

        while i < len(items) - 1:

            if (i + 1) % 2 == items[i] % 2:
                items = list(items)
                items.remove(items[i])
                items = tuple(items)

            else:
                i += 1

    return items


############################# part 5 #############################
def same_parity(items=tuple()):
    first_item = items[0]
    pars = (first_item, )

    for i in range(1, len(items)):
        if first_item % 2 == items[i] % 2:
            pars += (items[i],)

    return pars
