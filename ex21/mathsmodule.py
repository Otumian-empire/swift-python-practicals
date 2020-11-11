class MathsModule:

    def add(self, *args):
        total = 0

        for arg in args:
            if not self.is_number(arg):
                break

            total += arg

        return total

    def subtr(self, a, b):
        diff = 0

        if self.is_number(a) and self.is_number(b):
            diff = a - b

        return diff

    def mult(self,  *args):
        total = 1

        for arg in args:
            if not self.is_number(arg):
                break

            total *= arg

        return total

    def div(self, a, b):
        if self.is_number(a) and self.is_number(b) and b != 0:
            return a / b
        return None

    def floor_div(self, *args):
        if not self.is_number(args[0]):
            return None

        total = args[0]

        for arg in args[1:]:
            if not self.is_number(arg) or arg == 0:
                return None

            total //= arg

        return total

    def pow(self, a, b):
        if self.is_number(a) and self.is_number(b) and a != 0:
            return a ** b
        return None

    def mod(self, a, b):
        if self.is_number(a) and self.is_number(b) and b != 0:
            return a % b
        return None

    @staticmethod
    def is_number(a):
        return type(a) in [int, float]
