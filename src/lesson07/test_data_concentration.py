#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import unittest
import os



class TestDataConcentrationPlot(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_scatter_plot(self):
        df = pd.DataFrame(np.random.randint(100, size=(100, 2)), columns=['male', 'female'])
        df['score'] = df.male*0.3+df.female*0.7
        df.to_csv('{}\\out\\male_female100.csv'.format(self.CURRENT_FOLDER))
        scat = df.plot.scatter(x='male', y='female', s=df.score).get_figure()  # scatter plot
        scat.savefig('{}\out\\scatter_plot.png'.format(self.CURRENT_FOLDER))

    def test_heat_map(self):
        df = pd.DataFrame(np.random.randint(100, size=(100, 2)), columns=['male', 'female'])
        df.to_csv('{}\\out\\male_female100.csv'.format(self.CURRENT_FOLDER))
        scat = df.plot.hexbin(x='male', y='female', gridsize=10).get_figure()  # scatter plot
        scat.savefig('{}\out\\heat_map.png'.format(self.CURRENT_FOLDER))

if __name__ == '__main__':
    unittest.main()

