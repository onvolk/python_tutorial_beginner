#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os
import pandas as pd


class TestPandasDataFrameSelectionExercise(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


    def test_select_by_column_names(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        # data.loc[:, ['CustomerName', 'City']].to_csv('{}\\fixtures\select_by_column_name.csv'.format(self.CURRENT_FOLDER), index=False)
        result = pd.read_csv('{}\\fixtures\select_by_column_name.csv'.format(self.CURRENT_FOLDER))
        pd.testing.assert_frame_equal(data.loc[:, ['CustomerName', 'City']], result)


    def test_select_by_column_number(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        # data.iloc[:, [0, 1]].to_csv('{}\\fixtures\select_column_number.csv'.format(self.CURRENT_FOLDER), index=False)
        result = pd.read_csv('{}\\fixtures\select_column_number.csv'.format(self.CURRENT_FOLDER))
        pd.testing.assert_frame_equal(data.iloc[:, [0, 1]], result)

    # TODO: assert dataframe from fixtures
    def test_select_records_by_row_name(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[10:15, ['CustomerName', 'City']].to_csv('{}\\fixtures\select_records_by_row_name.csv'.format(self.CURRENT_FOLDER), index=False)
        result = pd.read_csv('{}\\fixtures\select_records_by_row_name.csv'.format(self.CURRENT_FOLDER))
        pd.testing.assert_frame_equal(data.loc[10:15, ['CustomerName', 'City']], result)
        self.assertEqual(len(result), 6)

    # TODO: assert something
    def test_select_first_last(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.loc[[0, (len(data)-1)], 'CustomerName'].to_csv('{}\\fixtures\select_first_last.csv'.format(self.CURRENT_FOLDER))  # data.loc[[0, data.tail(1).index.tolist()[0]], 'CustomerName']
        result = pd.read_csv('{}\\fixtures\select_first_last.csv'.format(self.CURRENT_FOLDER)))
        pd.testing.assert_frame_equal(data.loc[[0, (len(data)-1)], 'CustomerName'], result)


if __name__ == '__main__':
    unittest.main()
