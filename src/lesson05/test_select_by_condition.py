#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasSelectByCondition(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_select_by_condition(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[data.CustomerID>20].to_csv('{}\\out\select_customer_id_from_20.csv'.format(self.CURRENT_FOLDER))
        data.loc[data.Country=='Germany'].to_csv('{}\\out\select_germany.csv'.format(self.CURRENT_FOLDER))
        data.loc[data.Country.isin(['Germany', 'Mexico'])].to_csv('{}\\out\select_germany_mexico.csv'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()