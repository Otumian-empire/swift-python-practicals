import unittest

from mathsmodule import MathsModule


class TestMathsModule(unittest.TestCase):

    def test_add(self):
        module = MathsModule()

        self.assertEqual(module.add(1, 2), 3)
        self.assertEqual(module.add(1, -2), -1)
        self.assertEqual(module.add(1, 2, 3, 4), 10)

    def test_subtr(self):
        module = MathsModule()

        self.assertEqual(module.subtr(1, 2), -1)
        self.assertEqual(module.subtr(1, -2), 3)

    def test_mult(self):
        module = MathsModule()

        self.assertEqual(module.mult(1, 2), 2)
        self.assertEqual(module.mult(1, -2), -2)
        self.assertEqual(module.mult(1, 2, 4), 8)

    def test_div(self):
        module = MathsModule()

        self.assertEqual(module.div(1, 2), 0.5)
        self.assertEqual(module.div(1, -2), -0.5)
        self.assertEqual(module.div(5, 0), None)

    def test_floor_div(self):
        module = MathsModule()

        self.assertEqual(module.floor_div(1, 2), 0)
        self.assertEqual(module.floor_div(1, -2), -1)
        self.assertEqual(module.floor_div(1, 2, 3, 4), 0)

    def test_pow(self):
        module = MathsModule()

        self.assertEqual(module.pow(1, 2), 1)
        self.assertEqual(module.pow(2, 3), 8)
        self.assertEqual(module.pow(2, -2), 0.25)

    def test_mod(self):
        module = MathsModule()
        self.assertEqual(module.mod(1, 2), 1)
        self.assertEqual(module.mod(22, 7), 1)


if __name__ == "__main__":
    unittest.main()
