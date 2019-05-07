#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasSelectByColumn(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_select_column_by_name(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        result = data[['City', 'CustomerName']]
        result.to_csv('{}\\out\select_by_name.csv'.format(self.CURRENT_FOLDER))

    def test_select_column_by_number(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        result = data[[1, 2]]
        result.to_csv('{}\\out\select_by_number.csv'.format(self.CURRENT_FOLDER))

    def test_select_column_by_attribute(self):
        data = pd.read_excel('{}\\fixtures\customers.xlsx'.format(self.CURRENT_FOLDER), sheet_name='Sheet1')
        result = data.CustomerName
        result.to_excel('{}\\out\select_by_attribute.xlsx'.format(self.CURRENT_FOLDER))



if __name__ == '__main__':
    unittest.main()
