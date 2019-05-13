#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import unittest
import os



class TestDataCompositionPlot(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_pie_plot(self):
        df = pd.DataFrame(np.random.randint(100, size=(10, 4)), columns=['a', 'b', 'c', 'd'])
        df.to_csv('{}\\out\\abcd.csv'.format(self.CURRENT_FOLDER))
        fig_row = df.iloc[0].plot.pie(figsize=(5,5)).get_figure()  # pie plot by row, figsize parameter makes a circular plot
        fig_row.savefig('{}\out\\pie_plot.png'.format(self.CURRENT_FOLDER))
        fig_col = df.a.plot.pie().get_figure()  # pie plot by column
        fig_col.savefig('{}\out\\col_pie_plot.png'.format(self.CURRENT_FOLDER))

    def test_area_plot(self):
        df = pd.DataFrame(np.random.randint(100, size=(10, 4)), columns=['a', 'b', 'c', 'd'])
        df.to_csv('{}\\out\\abcd.csv'.format(self.CURRENT_FOLDER))
        fig = df.plot.area().get_figure()  # area plot
        fig.savefig('{}\out\\area_plot.png'.format(self.CURRENT_FOLDER))
        fig_col = df.c.plot.area().get_figure()  # area plot
        fig_col.savefig('{}\out\\col_area_plot.png'.format(self.CURRENT_FOLDER))

if __name__ == '__main__':
    unittest.main()

