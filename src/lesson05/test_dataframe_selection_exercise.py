#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os
import pandas as pd


class TestPandasDataFrameSelectionExercise(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    # TODO: assert dataframe from fixtures
    def test_select_by_column_names(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[:, ['CustomerName', 'City']].to_csv('{}\out\select_by_column_name.csv'.format(self.CURRENT_FOLDER))

    # TODO: assert dataframe from fixtures
    def test_select_by_column_number(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.iloc[:, [0, 1]].to_csv('{}\out\select_column_number.csv'.format(self.CURRENT_FOLDER))

    # TODO: assert dataframe from fixtures
    def test_select_records_by_row_name(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        result = data.loc[10:15, ['CustomerName', 'City']]
        result.to_csv('{}\out\select_records_by_row_name.csv'.format(self.CURRENT_FOLDER))
        self.assertEqual(len(result), 6)

    # TODO: assert something
    def test_select_first_last(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[[0, (len(data)-1)], 'CustomerName'].to_csv('{}\out\select_first_last.csv'.format(self.CURRENT_FOLDER))  # data.loc[[0, data.tail(1).index.tolist()[0]], 'CustomerName']


if __name__ == '__main__':
    unittest.main()
