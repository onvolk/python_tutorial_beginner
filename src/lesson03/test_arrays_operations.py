#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyArrayOperations(unittest.TestCase):
    def test_array_operations_add(self):
        a = np.array([2, 3, 5, 7, 11])
        np.testing.assert_array_equal(a+10, [ 12,  13,  15,  17,  21])

    def test_array_operations_multiply(self):
        a = np.array([2, 3, 5, 7, 11])
        np.testing.assert_array_equal(a*10, [ 20,  30,  50,  70,  110])

    def test_array_operations_power(self):
        a = np.array([2, 3, 5, 7, 11])
        np.testing.assert_array_equal(a**2, [ 4,  9,  25,  49,  121])

    def test_array_operations_comparison(self):
        a = np.array([2, 3, 5, 7, 11])
        np.testing.assert_array_equal(a<6, [ True,  True,  True,  False,  False])

if __name__ == '__main__':
    unittest.main()
