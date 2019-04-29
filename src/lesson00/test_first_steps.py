#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestFirstThingsInPythonMethods(unittest.TestCase):
    def test_addition(self):
        # prepare
        a = 2
        b = 3

        # act
        result = a + b

        # assert
        self.assertEqual(result, 5)

    def test_multiply(self):
        # prepare
        a = 2
        b = 3

        # act
        result = a * b

        # assert
        self.assertEqual(result, 6)

    def test_assignment(self):
        a = 3
        b = a
        self.assertEqual(b, a)
        self.assertEqual(a, 3)
        self.assertEqual(b, 3)

    def test_string(self):
        a = "Olechka"
        self.assertEqual(a.lower(), "olechka")

if __name__ == '__main__':
    unittest.main()
