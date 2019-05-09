#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasDeleteColumnsRows(unittest.TestCase):
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_delete_columns(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        result = data.drop(['City', 'Country'], 1)  # 1 for column and 0 for row, a list of columns to delete or one colunm: drop('City', 1)
        result.to_csv('{}\\out\\delete_column.csv'.format(self.CURRENT_FOLDER))

    def test_delete_rows(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        result = data.drop([0, 2, 4, 7], 0)  # 1 for column and 0 for row, delete a list of rows or one row: drop(5, 1)
        result.to_csv('{}\\out\\delete_row.csv'.format(self.CURRENT_FOLDER))

    def test_delete_rows_by_condition(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data[data.Country != 'Germany'].to_csv('{}\\out\\delete_rows_by_condition.csv'.format(self.CURRENT_FOLDER)) # drop customer from Germany
        data[data.CustomerID>50].to_csv('{}\\out\\delete_rows_by_condition50.csv'.format(self.CURRENT_FOLDER)) # delete all till 50 row


if __name__ == '__main__':
    unittest.main()
