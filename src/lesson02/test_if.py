#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestLoops(unittest.TestCase):
    def test_if(self):
        tomorrow_temp = 25
        my_cloth = 'jacket'
        warm_criterion = 20
        if tomorrow_temp > warm_criterion:
            my_cloth = 'T-shirt'
        result = 'Tomorrow I will wear a {}'.format(my_cloth)
        self.assertEqual(result, 'Tomorrow I will wear a T-shirt')


if __name__ == '__main__':
    unittest.main()
