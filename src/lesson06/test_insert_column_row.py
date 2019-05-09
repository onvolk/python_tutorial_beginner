#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import numpy as np
import os
import pandas as pd


class TestPandasInsertColumnsRows(unittest.TestCase):
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_insert_column(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        data.insert(0, 'New column', data.City)  # inplace, insert in data
        data.to_csv('{}\\out\\insert_column.csv'.format(self.CURRENT_FOLDER))

    def test_insert_row(self):
        data = pd.read_csv('{}\\fixtures\customers.csv'.format(self.CURRENT_FOLDER))
        info = {'CustomerID': 420, 'CustomerName': 'Apotheke', 'ContactName': 'Lena Mueller', 'Address': '154 Strasse', 'City': 'Frankfurt', 'PostalCode': '74350', 'Country': 'Germany'}  # a new row as a dict
        line = pd.DataFrame(info, index=[3])  # dict to Dataframe object with index 3
        result = pd.concat([data.iloc[:3], line, data.iloc[3:]]).reset_index(drop=True)  # not inplace, returns a new dataframe from the list of dataframe objects
        result.to_csv('{}\\out\\insert_row.csv'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()
