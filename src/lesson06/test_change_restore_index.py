#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasIndexChangeRestore(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_index_change_restore(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.set_index('CustomerName', verify_integrity=True).to_csv('{}\\out\\change_index.csv'.format(self.CURRENT_FOLDER))  # change index to 'CustomerName', if it is unique
        temp = data.set_index('City')
        temp.loc['London'].to_csv('{}\\out\\change_index_city.csv'.format(self.CURRENT_FOLDER))
        result = data.reset_index(drop=True)
        result.to_csv('{}\\out\\restore_index.csv'.format(self.CURRENT_FOLDER))  # index reset without adding a new column 'index'
        pd.testing.assert_frame_equal(data, result)
        

if __name__ == '__main__':
    unittest.main()
