#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import pandas as pd


class TestPandasSeriesOperations(unittest.TestCase):
    def test_series_slicing(self):
        arr = np.random.randn(5)
        srs = pd.Series(arr)
        self.assertTrue(isinstance(srs[1], float))
        self.assertEqual(srs[1].size, 1)

        self.assertListEqual(srs[2:].index.tolist(), [2, 3, 4])
        self.assertEqual(srs[2:].size, 3)

        self.assertListEqual(srs[[3, 0, 4]].index.tolist(), [3, 0, 4])
        self.assertEqual(srs[[3, 0, 4]].size, 3)

    # TODO: Fix me!
    def test_series_operations(self):
        arr = np.random.randn(5)
        srs = pd.Series(arr)
        result = srs ** 2
        self.assertEqual(result.size, srs.size)


if __name__ == '__main__':
    unittest.main()