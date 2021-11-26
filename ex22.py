""" Write a unit test - TestCases - for the programs written in exercise 12 """
import unittest

from ex12 import sort_nested_items


class TestEx12(unittest.TestCase):

    def test_empty_nested_list(self):
        self.assertEqual(sort_nested_items([[], []]), [[], []])

    def test_2_nested_list(self):
        self.assertEqual(sort_nested_items(
            [[2, 4, 1], [7, -2,  4, 1]]), [[1, 2, 4], [-2, 1, 4, 7]])

    # assuming that a nested item is also nested then `sort_nested_items` will fail


""" 
Complete the program below. This is an implementation of a function that returns the factorial of a given integer value.
"""


def factorial(n: int) -> int:
    return 1 if n < 1 else n * factorial(n - 1)


class TestFactorial(unittest.TestCase):

    def test_zero_factorial_is_one(self):
        self.assertEqual(factorial(0), 1)

    def test_one_factorial_is_one(self):
        self.assertEqual(factorial(1), 1)

    def test_five_factorial_is_120(self):
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
