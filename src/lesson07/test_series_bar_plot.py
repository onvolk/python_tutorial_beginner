#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import unittest
import os


class TestSeriesBarPlot(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_series_plot(self):
        aapl = pd.read_csv('{}\\fixtures\\aapl.csv'.format(self.CURRENT_FOLDER))
        aapl = aapl[::-1]  # reverse, from old to new data
        fig = aapl['Adj Close'].plot().get_figure()
        fig.savefig('{}\out\\adj_close_plot.png'.format(self.CURRENT_FOLDER))

    def test_bar_plot(self):
        df = pd.DataFrame(np.random.randint(100, size=(5, 2)), columns=['male', 'female'])
        df.to_csv('{}\\out\\male_female.csv'.format(self.CURRENT_FOLDER))
        figv = df.plot.bar().get_figure()  # vertical bar
        figv.savefig('{}\out\\bar_plot.png'.format(self.CURRENT_FOLDER))
        figh = df.plot.barh().get_figure()  # horizontal bar
        figh.savefig('{}\out\\barh_plot.png'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()

