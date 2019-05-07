#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasSelectByRow(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_select_by_row(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data[0:4].to_csv('{}\\out\select_by_row_slice.csv'.format(self.CURRENT_FOLDER))
        data.iloc[2].to_csv('{}\\out\select_one_row.csv'.format(self.CURRENT_FOLDER))
        data.iloc[[1, 3]].to_csv('{}\\out\select_several_rows.csv'.format(self.CURRENT_FOLDER))
        data.iloc[3:10].to_csv('{}\\out\select_several_rows_slice.csv'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()
