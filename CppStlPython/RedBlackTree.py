# Matthew Hilton
# October 20th, 2021

'''
Helper Module: RedBlackTree.py

This module implements red black trees for some of the ordered 
containers like map and set. A Red-Black tree is a Balanced Binary
Search Tree that colors the nodes either red or black in order 
to maintain a Balanced tree. Red-Black Trees satisfy 4 properties.

   1. Every node is colored either black or red
   2. Ever leaf node (nodes that Nil/Null/None) is black
   3. A red node has no red children and its parent is black
   4. Every path from a given node to any decended has the same number of black nodes
'''

from enum import Enum
from typing import Any


class Color(Enum):
    Black = 0
    Red = 1


class RBNode:

    def __init__(self, _v: Any = None, _c: Color = Color.Red, _l: 'RBNode' = None, _r: 'RBNode' = None) -> None:
        self.__val = _v
        self.__color = _c
        self.__left = _l
        self.__right = _r

    def __str__(self) -> str:
        str_repr = "Value: "
        str_repr += str(self.__val) if self.__val is not None else "None"
        str_repr += "\nColor: "
        str_repr += self.__color.name
        str_repr += "\nLeft: "
        str_repr += str(self.__left.get_val()
                        ) if self.__left is not None else "None"
        str_repr += "\nRight: "
        str_repr += str(self.__right.get_val()
                        ) if self.__right is not None else "None"
        return str_repr

    def get_val(self) -> Any:
        return self.__val

    def get_color(self) -> Color:
        return self.__color

    def get_left(self) -> 'RBNode':
        return self.__left

    def get_right(self) -> 'RBNode':
        return self.__right

    def set_val(self, _v: Any) -> None:
        self.__val = _v

    def set_color(self, _c: Color) -> None:
        self.__color = _c

    def set_left(self, _l: 'RBNode') -> None:
        self.__left = _l

    def set_right(self, _r: 'RBNode') -> None:
        self.__right = _r
