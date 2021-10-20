# Matthew Hilton
# October 20th, 2021
#
# Test Module: RedBlackTree.py
#
# Imports
import unittest

from CppStlPython import RedBlackTree
# from random import randint


class test_RBNode(unittest.TestCase):

    def setUp(self) -> None:
        self.default = RedBlackTree.RBNode()
        self.m = RedBlackTree.RBNode(6)
        self.n = RedBlackTree.RBNode(5, RedBlackTree.Color.Black, None, self.m)

    def test_RBNode(self):
        self.assertEqual(None, self.default.get_val())
        self.assertEqual(5, self.n.get_val())
        self.assertEqual(6, self.m.get_val())
        self.assertEqual(None, self.default.get_left())
        self.assertEqual(None, self.n.get_left())
        self.assertEqual(None, self.m.get_left())
        self.assertEqual(None, self.default.get_right())
        self.assertEqual(self.m, self.n.get_right())
        self.assertEqual(None, self.m.get_right())
        self.assertEqual(RedBlackTree.Color.Red, self.default.get_color())
        self.assertEqual(RedBlackTree.Color.Black, self.n.get_color())
        self.assertEqual(RedBlackTree.Color.Red, self.m.get_color())
