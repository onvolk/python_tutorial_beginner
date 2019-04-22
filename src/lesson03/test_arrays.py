#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np


class TestNumpyArray(unittest.TestCase):
    def test_first_actions(self):
        a = np.arange(10)
        np.testing.assert_array_equal(a, np.array(range(0,10)))


if __name__ == '__main__':
    unittest.main()
