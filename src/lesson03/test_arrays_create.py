#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyArrayCreate(unittest.TestCase):
    def test_array_create(self):
        a = np.arange(15).reshape(3, 5)
        np.testing.assert_array_equal(a, [[0,  1,  2,  3,  4],
                                            [5,  6,  7,  8,  9],
                                            [10, 11, 12, 13, 14]])

    def test_array_create_steps(self):
        b = np.arange(0, 10, 3)  # set the steps of iteration
        np.testing.assert_array_equal(b, [0, 3, 6, 9])

    def test_array_create_number_elements(self):
        c = np.linspace(0, 10, 5)  # fill the gap between 0 and 10, 5 - the number of elements
        np.testing.assert_array_equal(c, [0,  2.5, 5, 7.5, 10])

    def test_array_create_zeros(self):
        d = np.zeros((2, 2, 3))  # the array of zeros
        np.testing.assert_array_equal(d, [[[0, 0, 0],
                                            [0, 0, 0]],
                                          [[0, 0, 0],
                                           [0, 0, 0]]])

    def test_array_create_ones(self):
        e = np.ones((2, 2))
        np.testing.assert_array_equal(e, [[1, 1],
                                        [1, 1]])

    def test_array_create_empty(self):
        self.assertEqual(np.empty((3, 3)).shape, (3, 3))

    def test_array_create_from_list(self):
        np.testing.assert_array_equal(np.array([3, 7, 10]), [3, 7, 10])  # create an array from a list

    def test_array_create_from_tuple(self):
        np.testing.assert_array_equal(np.array((10, 7, 3)), [10, 7, 3])  # create an array from a tuple

    def test_array_create_multi(self):
        np.testing.assert_array_equal(np.array([[0, 0], [1, 1], [2, 2]]), [[0, 0], [1, 1], [2, 2]])


if __name__ == '__main__':
    unittest.main()
