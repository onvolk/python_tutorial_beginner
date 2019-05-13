#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasImportExportData(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_import_from_csv(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))

    def test_import_xls(self):
        data = pd.read_excel('{}\\fixtures\customers.xlsx'.format(self.CURRENT_FOLDER), sheet_name='Sheet2')

    def test_import_export_csv(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.to_csv('{}\\out\customers.csv'.format(self.CURRENT_FOLDER))
        data.to_csv('{}\\out\customers_no_index.csv'.format(self.CURRENT_FOLDER), index=False)

    def test_import_export_xls(self):
        data = pd.read_excel('{}\\fixtures\customers.xlsx'.format(self.CURRENT_FOLDER), sheet_name='Sheet2')
        data.to_excel('{}\\out\customers.xlsx'.format(self.CURRENT_FOLDER))
        data.to_excel('{}\\out\customers_no_index.xlsx'.format(self.CURRENT_FOLDER), index=False)


if __name__ == '__main__':
    unittest.main()
