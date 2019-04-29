#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import pandas as pd


class TestPandasSeriesIndexing(unittest.TestCase):
    def test_series_indexing_head(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        result = s.head(3)  # the first 3 elements
        self.assertListEqual(result.to_list(), [1, 3, 5])
       # pd.testing.assert_series_equal(s.head(3), pd.Series([1, 3, 5]))

    def test_series_indexing_tail(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        result = s.tail(2)  # the last 2 elements
        self.assertListEqual(result.to_list(), [6, 8])
        # pd.testing.assert_series_equal(s.tail(2), pd.Series([6, 8]))

    def test_series_indexing_sample(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        result = s.sample(3)  # the random 3 elements
        self.assertEqual(result.size, 3)

    def test_series_indexing_frac(self):
        s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 0 .. N-1
        result = s.sample(frac=0.6)  # 20% of elements
        self.assertEqual(result.size, 6)

if __name__ == '__main__':
    unittest.main()
