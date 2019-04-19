#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestLists(unittest.TestCase):
    def test_declaration(self):
        my_list = [180, 3.90, 'World']
        self.assertNotIn(2, my_list)
        self.assertIn(3.90, my_list)
        self.assertListEqual(my_list, [180, 3.90, 'World'])

    def test_comprehension(self):
        my_list = [4, 2, 1, 4, 5]
        result = [item * 2 for item in my_list if item > 2]
        self.assertListEqual(result, [8, 8, 10])

    def test_comprehension_with_strings(self):
        result = [item.upper() for item in 'Would you like a cup of coffee?'.split() if len(item) > 3]
        self.assertListEqual(result, ['WOULD', 'LIKE', 'COFFEE?'])


if __name__ == '__main__':
    unittest.main()
