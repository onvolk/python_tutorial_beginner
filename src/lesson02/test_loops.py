#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestLoops(unittest.TestCase):
    def test_loop_string(self):
        string = 'Hello World'
        result = []
        for letter in string:
            result.append(letter)
        self.assertEqual(result, ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd'])

    def test_loop_list(self):
        my_list = ['White', 'Yellow', 'Blue', 'Black']
        result = list()
        for item in my_list:
            result.append(item)
        self.assertListEqual(result, ['White', 'Yellow', 'Blue', 'Black'])

    def test_loop_dictionary(self):
        my_dict = {'color': 'white', 'shape': 'circle', 'size': 10}
        result = []
        for key, value in my_dict.items():
            result.append((key, value))
        self.assertListEqual(result, [('color', 'white'), ('shape', 'circle'), ('size', 10)])


if __name__ == '__main__':
    unittest.main()
