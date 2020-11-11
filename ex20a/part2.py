"""
Write a class for basic mathematical operations, such as addition, subtraction, multiplication, division, floordivision ( aka integer division), modulo ( aka remainder), power, etc """


class MyMath:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subt(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        return None

    def int_dive(self):
        if self.b != 0:
            return self.a // self.b
        return None

    def pow(self):
        return self.a ** self.b

    def modulo(self):
        return self.a % self.b

    def int_dive(self):
        if self.b != 0:
            return self.a // self.b
        return None
