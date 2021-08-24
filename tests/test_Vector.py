# Matthew Hilton
# July 6th, 2021
#
# Test Module: Vector.py
#
# Imports
import unittest

from CppStlPython import Vector
from random import randint


class test_vector(unittest.TestCase):

    def setUp(self):
        self.str_fill_vector = Vector(5, "foo")
        self.int_list = [1, 2, 3, 4, 5]

    # Test Init: 7 tests
    def test_init_empty(self):
        v = Vector()
        self.assertEqual(v.data(), [])

    def test_init_type(self):
        v = Vector(int)
        self.assertIsInstance(1, v._vector_type())
        self.assertEqual(v.data(), [])

    def test_init_fill(self):
        self.assertIsInstance("s", self.str_fill_vector._vector_type())
        self.assertEqual(len(self.str_fill_vector), 5)
        self.assertEqual(self.str_fill_vector.data(), ["foo"] * 5)

    def test_init_copy(self):
        v = Vector(self.str_fill_vector)
        self.assertIsInstance("s", v._vector_type())
        self.assertEqual(len(v), 5)
        self.assertEqual(v, self.str_fill_vector)

    def test_init_list(self):
        v = Vector(self.int_list)
        self.assertIsInstance(1, v._vector_type())
        self.assertEqual(len(v), 5)
        self.assertEqual(v.data(), self.int_list)

    def test_init_fail_list_type_mismatch(self):
        with self.assertRaises(TypeError):
            v = Vector([1, 2, 3, 4, 'five'])

    def test_init_fail_args(self):
        with self.assertRaises(Vector.ConstructorFailure):
            v = Vector(1, 2, 3, 4, 5, 6, 7, 8, 9)

    # Test Element Access: 14 tests
    # Vector[]: 6 tests
    def test_setitem(self):
        self.str_fill_vector[0] = "bar"
        self.assertEqual(self.str_fill_vector.data()[0], "bar")

    def test_setitem_fail_index(self):
        with self.assertRaises(IndexError):
            self.str_fill_vector[5] = "bar"

    def test_setitem_fail_type(self):
        with self.assertRaises(TypeError):
            self.str_fill_vector[0] = 1

    def test_setitem_loop(self):
        v = Vector(10, 0)
        rand_ints = []
        for i in range(len(v)):
            temp = randint(0, 100) % (i + 1)
            v[i] = temp
            rand_ints.append(temp)
        self.assertEqual(v.data(), rand_ints)

    def test_getitem(self):
        self.assertEqual(self.str_fill_vector[0], "foo")

    def test_getitem_fail_index(self):
        with self.assertRaises(IndexError):
            data = self.str_fill_vector[5]

    # At: 3 tests:
    def test_at_getitem(self):
        v = Vector(self.int_list)
        self.assertEqual(v.at(0), 1)

    def test_at_setitem(self):
        v = Vector(self.int_list)
        v.at(0, 0)
        self.assertEqual(v.at(0), 0)

    def test_at_getitem_fail_args(self):
        v = Vector(self.int_list)
        with self.assertRaises(Vector.ArgumentError):
            v.at(0, 0, "a", None)

    # Front: 2 Test
    def test_front(self):
        v = Vector(self.int_list)
        self.assertEqual(v[0], v.front())

    def test_front_fail(self):
        v = Vector(int)
        with self.assertRaises(Vector.OutOfRangeError):
            x = v.front()

    # Back: 2 Test
    def test_back(self):
        v = Vector(self.int_list)
        self.assertEqual(v[4], v.back())

    def test_back_fail(self):
        v = Vector(int)
        with self.assertRaises(Vector.OutOfRangeError):
            x = v.back()

    # Data: 1 Test
    def test_data(self):
        v = Vector(self.int_list)
        self.assertEqual(v.data(), self.int_list)