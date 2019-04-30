#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyArrayTransformation(unittest.TestCase):
    def test_array_shape(self):
        a = np.arange(28).reshape(4, 7)
        self.assertEqual(a.shape, (4, 7))  # the shape of the array

    def test_array_transpose(self):
        a = np.arange(28).reshape(4, 7)
        result = a.T
        self.assertEqual(result.shape, (7, 4))
        np.testing.assert_array_equal(result, [[0, 7, 14, 21],
                                                [1, 8, 15, 22],
                                                [2, 9, 16, 23],
                                                [3, 10, 17, 24],
                                                [4, 11, 18, 25],
                                                [5, 12, 19, 26],
                                                 [6, 13, 20, 27]])

    def test_array_ravel(self):
        a = np.arange(28).reshape(4, 7)
        result = a.ravel()  # makes one-dimension array
        self.assertEqual(result.size, 28)
        np.testing.assert_array_equal(result, [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
                                                17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_array_reshape(self):
        a = np.arange(28)
        np.testing.assert_array_equal(a.reshape(2, 2, 7), [[[0, 1, 2, 3, 4, 5, 6],
                                                            [7, 8, 9, 10, 11, 12, 13]],
                                                            [[14, 15, 16, 17, 18, 19, 20],
                                                             [21, 22, 23, 24, 25, 26, 27]]])

    def test_array_vertical_stack(self):
        a = np.array([[8, -1],
                      [4, 9]])
        b = np.array([[0.2, 0.9],
                      [-0.02, 0.04]])
        result = np.vstack((a,b))  # vertical stack, adds b below a
        self.assertEqual(result.shape, (4, 2))
        np.testing.assert_array_equal(result, [[8, -1],
                                                [4., 9],
                                                [0.2, 0.9],
                                                [-0.02, 0.04]])

    def test_array_horizontal_stack(self):
        a = np.array([[8, -1],
                      [4, 9]])
        b = np.array([[0.2, 0.9],
                      [-0.02, 0.04]])
        result = np.hstack((a, b))  # horizontal stack, adds b rights to a
        self.assertEqual(result.shape, (2, 4))
        np.testing.assert_array_equal(result, [[8, -1, 0.2, 0.9],
                                               [4., 9, -0.02, 0.04]])

    def test_array_horizontal_split(self):
        a = np.array([[8, -1],
                      [4, 9]])
        b = np.array([[0.2, 0.9],
                      [-0.02, 0.04]])
        h = np.hstack((a, b))  # horizontal stack, adds b rights to a
        np.hsplit(h, 2)  # makes 2 arrays from 1 horizontally
        np.testing.assert_array_equal(np.hsplit(h, 2), [([[8, -1],
                                                            [4, 9]]),
                                                        ([[0.2, 0.9],
                                                        [-0.02, 0.04]])])

    def test_array_vertical_split(self):
        a = np.array([[8, -1],
                      [4, 9]])
        b = np.array([[0.2, 0.9],
                      [-0.02, 0.04]])
        v = np.vstack((a, b))  # vertical stack, adds b below a
        np.vsplit(v, 2)  # makes 2 arrays from 1 vertically
        np.testing.assert_array_equal(np.vsplit(v, 2), [([[8, -1],
                                                          [4, 9]]),
                                                        ([[0.2, 0.9],
                                                          [-0.02, 0.04]])])



if __name__ == '__main__':
    unittest.main()
