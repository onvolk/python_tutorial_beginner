#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class TestDictionaries(unittest.TestCase):
    def test_dictionary_lookup(self):
        drink = {'type': 'tea', 'quantity': 'two cups'}
        self.assertEqual(drink['quantity'], 'two cups')

    def test_dictionary_add_entry(self):
        drink = {'type': 'coffee', 'quantity':'a cup'}
        drink['brand'] = 'Starbucks'
        self.assertDictEqual(drink, {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'})

    def test_change_the_value(self):
        drink = {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'}
        drink['type'] = 'Late'
        self.assertDictEqual(drink, {'type': 'Late', 'quantity': 'a cup', 'brand': 'Starbucks'})

    def test_delete(self):
        drink = {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'}
        del drink['brand']
        self.assertDictEqual(drink, {'type': 'coffee', 'quantity': 'a cup'})

    def test_clear(self):
        drink = {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'}
        drink.clear()
        self.assertDictEqual(drink, {})
        self.assertDictEqual(drink, dict())

    def test_dict_functions_keys(self):
        drink = {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'}
        # https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
        keys_as_list = list(drink.keys())
        another_way = list(drink)
        self.assertListEqual(keys_as_list, ['type', 'quantity', 'brand'])
        self.assertListEqual(keys_as_list, another_way)

    def test_dict_functions_values(self):
        drink = {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'}
        values_as_list = list(drink.values())
        self.assertListEqual(values_as_list, ['coffee', 'a cup', 'Starbucks'])

    def test_dict_functions_items(self):
        drink = {'type': 'coffee', 'quantity': 'a cup', 'brand': 'Starbucks'}
        items_as_list = list(drink.items())
        self.assertListEqual(items_as_list, [('type', 'coffee'), ('quantity', 'a cup'), ('brand', 'Starbucks')])


if __name__ == '__main__':
    unittest.main()
