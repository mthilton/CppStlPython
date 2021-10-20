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

    '''
    Enum for the colors of the tree.
    '''
    Black = 0
    Red = 1


class RBNode:

    '''
    Node Class for each node in the tree. Contians the value, color, and children of the node.
    '''

    def __init__(self, _v: Any = None, _c: Color = Color.Red, _l: 'RBNode' = None, _r: 'RBNode' = None) -> None:
        '''
        Node Constrcutor. By default, this constructor will generate an empty node colored red with nil children.

        Parameters:

            _v: Value of the node, can take any type. Type checking is done at the tree level. By default, val is
                None
            _c: Color of the node. By default, color is red.
            _l: Left child of the node. By default, the left child is None
            _r: Right child of the node. By default, the right child is None
        '''
        self.__val = _v
        self.__color = _c
        self.__left = _l
        self.__right = _r

    def __str__(self) -> str:
        '''
        overloads the str(RBNode) function. Will return a string representation of RBNode
        '''
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
        '''
        Value getter method for RBNode. Returns the value of the node.
        '''
        return self.__val

    def get_color(self) -> Color:
        '''
        Color getter method for RBNode. Returns the color of the node.
        '''
        return self.__color

    def get_left(self) -> 'RBNode':
        '''
        Left getter method for RBNode. Returns the left child of Node, can be None.
        '''
        return self.__left

    def get_right(self) -> 'RBNode':
        '''
        Right getter method for RBNode. Returns the right child of Node, can be None.
        '''
        return self.__right

    def set_val(self, _v: Any) -> None:
        '''
        Value setter method for RBNode. Modifies the value of the node.
        '''
        self.__val = _v

    def set_color(self, _c: Color) -> None:
        '''
        Color setter method for RBNode. Modifies the color of the node.
        '''
        self.__color = _c

    def set_left(self, _l: 'RBNode') -> None:
        '''
        Left setter method for RBNode. Modifies the left child of Node, can be None.
        '''
        self.__left = _l

    def set_right(self, _r: 'RBNode') -> None:
        '''
        Right setter method for RBNode. Modifies the right child of Node, can be None.
        '''
        self.__right = _r


class RedBlackTree:

    def init(self, _r: RBNode = None) -> None:
        pass
