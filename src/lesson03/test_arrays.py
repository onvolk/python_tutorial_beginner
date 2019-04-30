#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_first_actions(self):
        a = np.arange(15).reshape(3,5)
        np.testing.assert_array_equal(a, [[0,  1,  2,  3,  4],
                                            [5,  6,  7,  8,  9],
                                            [10, 11, 12, 13, 14]])
        self.assertEqual(a.ndim, 2)  # the number of dimensions
        self.assertEqual(a.shape, (3, 5))  # the shape of the array
        self.assertEqual(a.size, 15)  # the number the elements in the array


if __name__ == '__main__':
    unittest.main()
