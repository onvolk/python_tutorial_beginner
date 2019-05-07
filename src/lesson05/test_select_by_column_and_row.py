#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasSelectByColumnRow(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_select_by_column_and_row(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        self.assertEqual(data.iloc[0, 4], 'Berlin')
        self.assertEqual(data.loc[0, 'City'], 'Berlin')
        data.iloc[0:3, 4:7].to_csv('{}\\out\select_columns_and_rows.csv'.format(self.CURRENT_FOLDER))
        data.loc[0:3, 'CustomerName':'City'].to_csv('{}\\out\select_columns_and_rows_name.csv'.format(self.CURRENT_FOLDER))
        data.loc[:, 'CustomerName':'City'].head().to_csv(
            '{}\\out\select_columns_and_rows_name_number.csv'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()
