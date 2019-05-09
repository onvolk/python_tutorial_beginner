#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasColumnRenameRearrange(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_column_rename(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER)).head()
        result = data.rename(columns={'ContactName': 'Salesman', 'CustomerID': 'Bla Bla Bla!'})
        self.assertEqual(data.loc[2, 'Country'], result.loc[2, 'Country'])
        result.to_csv('{}\\out\\rename_column.csv'.format(self.CURRENT_FOLDER))

    def test_column_rearrange(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER)).head()
        cols = data.columns.tolist()  # makes a list of columns names
        cols = cols[::-1]  # reverse the list
        result = data[cols]
        result.to_csv('{}\\out\\rearrange_columns.csv'.format(self.CURRENT_FOLDER))
        self.assertListEqual(cols, result.columns.tolist())
        result_new = data.loc[:, cols]
        result_new.to_csv('{}\\out\\rearrange_columns_new.csv'.format(self.CURRENT_FOLDER))
        self.assertListEqual(cols, result_new.columns.tolist())



if __name__ == '__main__':
    unittest.main()
