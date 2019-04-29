#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import pandas as pd


class TestPandasSeriesCreation(unittest.TestCase):
    def test_series_single_element(self):
        sr = pd.Series(3.14)
        self.assertListEqual(sr.to_list(), [3.14])
        self.assertDictEqual(sr.to_dict(), {0: 3.14})

    def test_series_with_indexes(self):
        sr = pd.Series(3.14, index=['a', 'b', 'c'])
        self.assertDictEqual(sr.to_dict(), {'a': 3.14, 'b': 3.14, 'c': 3.14})
        pd.testing.assert_series_equal(sr, pd.Series({'a': 3.14, 'b': 3.14, 'c': 3.14}))

    def test_series_with_non_numeric_values(self):
        couples_dict = {'John': 'Emma', 'Edward': 'Molly', 'Alex': 'Iris'}
        couples = pd.Series(couples_dict)
        self.assertDictEqual(couples.to_dict(), couples_dict)

    def test_series_creation_random(self):
        arr = np.random.randn(5)  # 0..N-1
        sr = pd.Series(arr, index=['h', 'e', 'l', 'l', 'o'])
        self.assertListEqual(sr.index.tolist(), ['h', 'e', 'l', 'l', 'o'])
        self.assertEqual(sr.size, 5)

        result = [item for item in sr.to_list() if -10 <= item <= 10]
        self.assertEqual(sr.size, len(result))

        # Option 2:
        self.assertTrue(all([-10 <= item <= 10 for item in sr.to_list()]))


if __name__ == '__main__':
    unittest.main()
