#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os
import pandas as pd


class TestPandasSelectByCondition(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    # TODO: Split to multiple tests and compare dataframes with loaded from fixtures
    def test_select_by_id_from_20(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[data.CustomerID > 20].to_csv('{}\\fixtures\select_customer_id_from_20.csv'.format(self.CURRENT_FOLDER), index=False)
        result = pd.read_csv('{}\\fixtures\select_customer_id_from_20.csv'.format(self.CURRENT_FOLDER))
        pd.testing.assert_frame_equal(data.loc[data.CustomerID > 20], result)

    def test_select_by_germany(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[data.Country == 'Germany'].to_csv('{}\\out\select_germany.csv'.format(self.CURRENT_FOLDER))

    def test_select_by_germany_mexico(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[data.Country.isin(['Germany', 'Mexico'])].to_csv('{}\out\select_germany_mexico.csv'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()
