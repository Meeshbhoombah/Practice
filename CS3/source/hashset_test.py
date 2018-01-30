# -*- encoding: utf-8 -*-

"""
set_test.py

Test the HashSet
"""

from hashset import HashSet
import unittest

class HashSetTest(unittest.TestCase):

    def test_init(self):
        hs = HashSet('A', 'B', 'C')
        assert hs.size == 4

    def test_contains(self):
        hs = HashSet()
        assert hs.contains('') == False
        hs = HashSet('A', 'B', 'C')
        assert hs.contains('A') == True
        

