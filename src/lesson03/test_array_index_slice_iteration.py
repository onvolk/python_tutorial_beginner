#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyArrayIndexingSlicingIteration(unittest.TestCase):
    def test_array_indexing(self):
        a = np.arange(10) * 2
        np.testing.assert_array_equal(a, [0,  2,  4,  6,  8,  10,  12,  14,  16,  18])
        self.assertEqual(a[3], 6)  # start from 0, index - 1, 3-1=2

    def test_array_slicing(self):
        a = np.arange(10) * 2
        np.testing.assert_array_equal(a[3:7], [6, 8, 10, 12])  # start from 0, 7 not incl., elements 3 to 6
        np.testing.assert_array_equal(a[:7], [0, 2, 4, 6, 8, 10, 12])  # elements 0 to 6
        np.testing.assert_array_equal(a[7:], [14, 16, 18])  # start from 0, elements 6 to the end


    def test_array_iteration(self):
        a = np.arange(10) ** 2
        np.testing.assert_array_equal(a, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
        result = list()
        for i in a:
            result.append(np.sqrt(i))
        self.assertListEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_array_multi_indexing(self):
        a = np.arange(20).reshape(4,5)
        np.testing.assert_array_equal(a, [[0,  1,  2,  3,  4],
                                            [5,  6,  7,  8,  9],
                                            [10, 11, 12, 13, 14],
                                            [15, 16, 17, 18, 19]])
        self.assertEqual(a[2,3], 13)

    def test_array_multi_slicing(self):
        a = np.arange(20).reshape(4, 5)
        np.testing.assert_array_equal(a[1:3,2:4], [[7, 8],
                                                    [12, 13]])  # 2nd and 3th rows, 3th and 4th columns


if __name__ == '__main__':
    unittest.main()
