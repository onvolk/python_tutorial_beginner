#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestSets(unittest.TestCase):
    def test_set_creation(self):
        set_a = {1, 2, 3, 4, 5, 6, 7}
        set_b = set([1, 2, 3, 4])
        difference = set_a.difference(set_b)
        self.assertSetEqual(difference, {5, 6, 7})

    def test_remove_duplicates(self):
        nums = [1, 2, 1, 1, 1, 3, 4]
        self.assertListEqual(list(set(nums)), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()

