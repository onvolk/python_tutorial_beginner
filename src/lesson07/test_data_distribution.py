#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import unittest
import os



class TestDataDistributionPlot(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_histogram_box_plot(self):
        df = pd.DataFrame(np.random.randint(100, size=(100, 2)), columns=['male', 'female'])
        df.to_csv('{}\\out\\male_female100.csv'.format(self.CURRENT_FOLDER))
        hist1 = df.plot.hist().get_figure()  # histogram male and female
        hist1.savefig('{}\out\\histogram_male_female.png'.format(self.CURRENT_FOLDER))
        hist2 = df.male.plot.hist().get_figure()  # histogram only male
        hist2.savefig('{}\out\\histogram_male.png'.format(self.CURRENT_FOLDER))
        hist3 = df.plot.hist(alpha=0.5).get_figure()  # histogram transparent
        hist3.savefig('{}\out\\histogram_transparent.png'.format(self.CURRENT_FOLDER))
        hist4 = df.plot.hist(stacked=True).get_figure()  # histogram the sum of male and female
        hist4.savefig('{}\out\\histogram_sum.png'.format(self.CURRENT_FOLDER))
        box = df.plot.box().get_figure()  # box plot
        box.savefig('{}\out\\box_plot.png'.format(self.CURRENT_FOLDER))



if __name__ == '__main__':
    unittest.main()

