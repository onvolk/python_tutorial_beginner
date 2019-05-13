#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import unittest
import os


class TestPlot(unittest.TestCase):

    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def test_plot(self):
        data = [['tom', 10], ['nick', 15], ['juli', 14]]
        df = pd.DataFrame(data, columns=['Name', 'Age'])
        figure = df['Age'].plot().get_figure()
        figure.savefig('{}\out\\first_graph.png'.format(self.CURRENT_FOLDER))


if __name__ == '__main__':
    unittest.main()

