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
        greater_than_5 = s[s > 5]
        self.assertListEqual(greater_than_5.to_list(), [6, 8])
        self.assertListEqual(greater_than_5.index.tolist(), [4, 5])
        self.assertEqual(greater_than_5.size, 2)

        greater_than_5_less_than_7 = s[(s > 5) & (s < 7)]
        self.assertListEqual(greater_than_5_less_than_7.to_list(), [6])
        self.assertEqual(greater_than_5_less_than_7.index, 4)
        self.assertEqual(greater_than_5_less_than_7.size, 1)

    def test_series_masking_null(self):
        s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 0 .. N-1
        all_nan = s[pd.isnull(s)]
        self.assertEqual(all_nan.size, 1)
        self.assertEqual(all_nan.index, 3)

        non_nan = s[~pd.isnull(s)]
        self.assertListEqual(non_nan.to_list(), [1, 3, 5, 6, 8])
        self.assertEqual(non_nan.size, 5)
        self.assertEqual(non_nan.index.tolist(), [0, 1, 2, 4, 5])

        # Option 2
        pd.testing.assert_series_equal(non_nan, pd.Series({0: 1., 1: 3, 2: 5, 4: 6, 5: 8}))


if __name__ == '__main__':
    unittest.main()
