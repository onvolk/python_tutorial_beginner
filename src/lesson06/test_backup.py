#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasBackup(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_select_by_row(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER)).head()
        backup = data.copy()
        backup.to_csv('{}\\out\\backup.csv'.format(self.CURRENT_FOLDER))
        self.assertEqual(len(backup), len(data))
        data = ''
        self.assertEqual(len(data), 0)
        data = backup.copy()
        self.assertEqual(len(data), 5)



if __name__ == '__main__':
    unittest.main()
