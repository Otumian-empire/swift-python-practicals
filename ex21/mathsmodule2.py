"""
For a second version of this program, let a method take 3 args, operator, first_operand, second_operand. Instead of calling any of the methods such as add, just call, evaluate with arguments such as evaluate('+', 2, 5) to return 7. This should work even if the second and third arguments are in a form of strings such as evaluate('+', '2', '5') .
"""


class MathsModule2:
    OPERATORS = ["+", "-", "*", "/", "//", "**", "%"]

    def evaluate(self, op, a, b):
        self.op = op
        self.a = a
        self.b = b
        self.opearations = [self.add, self.subtr, self.mult,
                            self.div, self.floor_div, self.pow, self.mod]
        try:
            if self.is_number(self.a) and self.is_number(self.b):
                if self.op in self.OPERATORS:
                    index = self.OPERATORS.index(self.op)
                    return self.opearations[index]()

        except Exception as e:
            print(
                "pass an int or float value with a valid stringed operator")
            print(" such as +, -, /, //, *, ** or %")

        return None

    def add(self):
        return self.a + self.b

    def subtr(self, a, b):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def floor_div(self):
        return self.a // self.b

    def pow(self):
        return self.a ** self.b

    def mod(self):
        return self.a % self.b

    @staticmethod
    def is_number(a):
        return type(a) in [int, float]
