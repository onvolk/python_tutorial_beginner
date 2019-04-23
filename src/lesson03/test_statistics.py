#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyStatistics(unittest.TestCase):
    def test_statistics_sum(self):
        a = np.arange(9).reshape(3,3)
        np.testing.assert_array_equal(a, [[0,  1,  2],
                                            [3,  4,  5],
                                            [6, 7, 8]])
        self.assertEqual(a.sum(), 36) # sum of all the elements of the array
        np.testing.assert_array_equal(a.sum(axis=1), [3, 12, 21])  # sum by each row
        np.testing.assert_array_equal(a.sum(axis=0), [9, 12, 15])  # sum by each column

    def test_statistics_max(self):
        a = np.arange(9).reshape(3,3)
        np.testing.assert_array_equal(a, [[0,  1,  2],
                                            [3,  4,  5],
                                            [6, 7, 8]])
        self.assertEqual(a.max(), 8) # max of all the elements of the array
        np.testing.assert_array_equal(a.max(axis=1), [2, 5, 8])  # max by each row
        np.testing.assert_array_equal(a.max(axis=0), [6, 7, 8])  # max by each column

    def test_statistics_min(self):
        a = np.arange(9).reshape(3,3)
        np.testing.assert_array_equal(a, [[0,  1,  2],
                                            [3,  4,  5],
                                            [6, 7, 8]])
        self.assertEqual(a.min(), 0) # min of all the elements of the array
        np.testing.assert_array_equal(a.min(axis=1), [0, 3, 6])  # min by each row
        np.testing.assert_array_equal(a.min(axis=0), [0, 1, 2])  # min by each column

    def test_statistics_average(self):
        a = np.arange(9).reshape(3,3)
        np.testing.assert_array_equal(a, [[0,  1,  2],
                                            [3,  4,  5],
                                            [6, 7, 8]])
        self.assertEqual(np.average(a), 4) # average of all the elements of the array
        np.testing.assert_array_equal(np.average(a, axis=1), [1, 4, 7])  # average by each row
        np.testing.assert_array_equal(np.average(a, axis=0), [3, 4, 5])  # average by each column

    def test_statistics_std(self):
        a = np.arange(9).reshape(3,3)
        np.testing.assert_array_equal(a, [[0,  1,  2],
                                            [3,  4,  5],
                                            [6, 7, 8]])
        self.assertEqual(np.std(a), 2.581988897471611) # standard deviation of all the elements of the array
        #np.testing.assert_array_equal(np.std(a, axis=1), [0.816497, 0.816497, 0.816497])  # standard deviation by each row
        #np.testing.assert_array_equal(np.std(a, axis=0), [2.44949, 2.44949, 2.44949])  # standard deviation by each column

if __name__ == '__main__':
    unittest.main()
