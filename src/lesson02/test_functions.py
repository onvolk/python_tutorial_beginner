#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestFuctions(unittest.TestCase):
    def test_functions_greet(self):
        def greet(name):
            return 'Hello {}!'.format(name)

        self.assertListEqual([greet(item) for item in ['John', 'Mike', 'Tony']], ['Hello John!', 'Hello Mike!', 'Hello Tony!'])

    def test_fuctions_cloth(self):
        def cloth(temp):
            hot = 30
            warm = 20
            cold = 10
            cloth = ''
            if temp > hot:
                cloth = 'T-shirt'
            elif temp > warm:
                cloth = 'shirt'
            else:
                cloth = 'jacket'
            return cloth
        temp = 28
        self.assertEqual('I will wear a {}'.format(cloth(temp)), 'I will wear a shirt')


if __name__ == '__main__':
    unittest.main()
