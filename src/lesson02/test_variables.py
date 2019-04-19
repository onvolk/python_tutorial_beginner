#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestVariables(unittest.TestCase):
    def test_integer(self):
        height = 180
        self.assertEqual(height, 180)

    def test_float(self):
        GPA = 3.90
        self.assertEqual(GPA, 3.90)

    def test_boolean(self):
        flag = True
        self.assertTrue(flag)


if __name__ == '__main__':
    unittest.main()
