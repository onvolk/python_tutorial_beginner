#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import unittest
import os
import statsmodels.api as sm


class TestLinearRegressionPart1(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_regression(self):
        df = pd.read_excel('{}\\fixtures\\commercial rent.xlsx'.format(self.CURRENT_FOLDER))
        df.describe().to_excel('{}\out\describe.xlsx'.format(self.CURRENT_FOLDER))
        # Y = a + bX
        Y = df.rental_rates
        X = df.iloc[:, 1:]  # multiple regression, X are all columns except the first
        X = sm.add_constant(X)
        X.to_excel('{}\out\X.xlsx'.format(self.CURRENT_FOLDER))
        est = sm.OLS(Y, X) # makes the function - OlS model
        est = est.fit()
        est.summary()
        est.predict()




if __name__ == '__main__':
    unittest.main()

