""" Write a unit test - TestCases - for the programs written since exercise 12 """
import unittest

from ex12 import sort_nested_items


class TestEx12(unittest.TestCase):

    def test_empty_nested_list(self):
        self.assertEqual(sort_nested_items([[], []]), [[], []])

    def test_2_nested_list(self):
        self.assertEqual(sort_nested_items(
            [[2, 4, 1], [7, -2,  4, 1]]), [[1, 2, 4], [-2, 1, 4, 7]])

    # assuming that a nested item is also nested then `sort_nested_items` will fail


if __name__ == "__main__":
    unittest.main()
