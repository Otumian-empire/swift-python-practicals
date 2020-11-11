"""
    Re-write the Rectangle class, and check for execptions.

    ```
    # create a file, with name rectangle.py

    # this is a simple is class to model a rectangle
    # a rectangle has length and breadth, so we pass
    #  the length and breadth to the constructor
    # it has a 2 methods that would return the area and perimeter.

    class Rectangle:

        def __init__(self, length, breadth):
            self.length = length
            self.breadth = breadth

        def area(self):
            ''' returns the area as, length * breadth '''
            return self.length * self.breadth

        def perimeter(self):
            ''' returns the perimeter as, 2 * (length + breadth) '''
            return 2 * (self.length + self.breadth)

    # instance of the rectangle class
    rect_inst = Rectangle(2, 3)  # l = 2, b = 3

    # get the area
    area = rect_inst.area()

    # get the perimeter
    perrmeter = rect_inst.perimeter()

    print(
        f"The area and perimeter of the rectangle are, {area} and {perrmeter} respectively")
```
"""


def is_number(a):
    return type(a) in [int, float]


class Rectangle:
    def __init__(self, length, breadth):
        try:
            if not is_number(length) or not is_number(breadth):
                raise Exception("int or float required as args")

            self.length = length
            self.breadth = breadth
        except Exception as e:
            print("int or float args required")
            return None

    def area(self):
        """ returns the area as, length * breadth """
        try:
            return self.length * self.breadth
        except Exception as e:
            print("int or float args required")
            return None

    def perimeter(self):
        """ returns the perimeter as, 2 * (length + breadth) """
        try:
            return 2 * (self.length + self.breadth)
        except Exception as e:
            print("int or float args required")
            return None
