#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestSets(unittest.TestCase):
    def test_set(self):
        nums = [1, 2, 1, 1, 1, 3, 4]
        self.assertListEqual(list(set(nums)), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
