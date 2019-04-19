#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestStrings(unittest.TestCase):
    def test_replace(self):
        drinks = 'Would you like a cup of coffee?'
        self.assertEqual(drinks.replace('o', '0'), 'W0uld y0u like a cup 0f c0ffee?')

    def test_split(self):
        drinks = 'Would you like a cup of coffee?'
        self.assertListEqual(drinks.split(' '), ['Would', 'you', 'like', 'a', 'cup', 'of', 'coffee?'])

    def test_join(self):
        drinks = 'Would you like a cup of coffee?'
        words = drinks.split()
        self.assertEqual(' '.join(words), drinks)

    def test_startswith(self):
        drinks = 'Would you like a cup of coffee?'
        self.assertTrue(drinks.startswith('Would'))
        self.assertFalse(drinks.startswith('Do'))

    def test_endswith(self):
        drinks = 'Would you like a cup of coffee?'
        self.assertTrue(drinks.endswith('?'))
        self.assertFalse(drinks.endswith('!'))

    def test_string_format_without_names(self):
        greeting = 'Hello, {} {}'.format('Olha', 'Volk')
        self.assertEqual(greeting, 'Hello, Olha Volk')

    def test_string_format_with_names(self):
        greeting = 'Hello, {first_name} {last_name}'.format(first_name='Olha', last_name='Volk')
        self.assertEqual(greeting, 'Hello, Olha Volk')


if __name__ == '__main__':
    unittest.main()
