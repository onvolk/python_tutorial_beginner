#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import pandas as pd


class TestPandaSeriesMasking(unittest.TestCase):
    def test_series_masking_equal(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        result = s[s == 3]
        self.assertListEqual(result.to_list(), [3])
        self.assertEqual(result.index, 1)
        self.assertEqual(result.size, 1)

    def test_series_masking_compare(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        self.assertListEqual(s[s > 5].to_list(), [6, 8])
        self.assertListEqual(s[s > 5].index.tolist(), [4, 5])
        self.assertEqual(s[s > 5].size, 2)
        result = s[(s > 5) & (s < 7)]
        self.assertListEqual(result.to_list(), [6])
        self.assertEqual(result.index, 4)
        self.assertEqual(result.size, 1)

    def test_series_masking_null(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        self.assertEqual(s[pd.isnull(s)].size, 1)
        self.assertEqual(s[pd.isnull(s)].index, 3)
        self.assertListEqual(s[~pd.isnull(s)].to_list(), [1, 3, 5, 6, 8])
        self.assertEqual(s[~pd.isnull(s)].size, 5)
        self.assertEqual(s[~pd.isnull(s)].index.tolist(), [0, 1, 2, 4, 5])

if __name__ == '__main__':
    unittest.main()
