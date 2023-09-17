# Start here. Once you have good test, move on to hw2.py

import unittest
from hw2 import Card, Deck, is_group

import random

class TestCard(unittest.TestCase):
    def test_init(self):
        """Tests that we can initialize cards w/ number/color/shading/shaper"""
        c1 = Card(2, "green", "striped", "diamond")

        self.assertEqual(c1.number, 2)
        self.assertEqual(c1.color, "green")
        self.assertEqual(c1.shading, "striped")
        self.assertEqual(c1.shape, "diamond")

    def test_str(self):
        """test that we can get a good string representation of GroupCard instances"""

        c1 = Card(2, "green", "striped", "diamond")
        self.assertEqual(str(c1), "Card(2, green, striped, diamond)")

    def test_eq(self):
        """Tests that two cards are equal iff all attributes (number, color, shading, shape) are equal"""
        c1 = Card(2, "green", "striped", "diamond")
        c2 = Card(2, "green", "striped", "diamond")
        c3 = Card(3, "green", "striped", "diamond")

        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)

           
# Write your own docstrings for the tests below
class TestDeck(unittest.TestCase):
    def test_init(self):

        x = Deck([1, 2, 3], ["green", "blue", "purple"], ["empty", "striped", "solid"], ["diamond", "squiggle", "oval"])
        self.assertEqual(len(x), 81)
        self.assertEqual(x.my_nums, [1, 2, 3])
        self.assertEqual(x.my_cols, ["green", "blue", "purple"])
        self.assertEqual(x.my_shadings, ["empty", "striped", "solid"])
        self.assertEqual(x.my_shapes, ["diamond", "squiggle", "oval"])
        

    def test_draw_top(self): 
        x = Deck([1, 2, 3], ["green", "blue", "purple"], ["empty", "striped", "solid"], ["diamond", "squiggle", "oval"])
        self.assertEqual(str(x.cards[-1]), "Card(3, purple, solid, oval)")

    def test_shuffle(self): 
        
        x = Deck([1, 2, 3], ["green", "blue", "purple"], ["empty", "striped", "solid"], ["diamond", "squiggle", "oval"])
        random.seed(1)
        random.shuffle(x.cards)
        self.assertEqual(str(x.cards[-1]), "Card(1, blue, solid, oval)")
        
# After Card and Deck are working, write and test the alg below.
# Include a docstring.
class TestSimulator(unittest.TestCase):
    def test_is_group(self):
        c1 = Card(1, "blue", "striped", "squiggle")
        c2 = Card(1, "purple", "striped", "diamond")
        c3 = Card(1, "green", "striped", "oval")
        c4 = Card(3, "purple", "empty", "diamond")

        self.assertTrue(is_group(c1, c2, c3))
        self.assertFalse(is_group(c1, c2, c4))


unittest.main() # runs all unittests above