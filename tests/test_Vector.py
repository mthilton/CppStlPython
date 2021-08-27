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
        self.assertEqual(len(v), 0)
        self.assertIsNone(v.type())
        self.assertEqual(list(v.data()), [])

    def test_init_type(self):
        v = Vector(int)
        self.assertIsInstance(1, v.type())
        self.assertEqual(list(v.data()), [])

    def test_init_fill(self):
        self.assertIsInstance("s", self.str_fill_vector.type())
        self.assertEqual(len(self.str_fill_vector), 5)
        self.assertEqual(list(self.str_fill_vector.data()), ["foo"] * 5)

    def test_init_copy(self):
        v = Vector(self.str_fill_vector)
        self.assertIsInstance("s", v.type())
        self.assertEqual(len(v), 5)
        self.assertEqual(v, self.str_fill_vector)
        self.assertNotEqual(id(v), id(self.str_fill_vector))

    def test_init_list(self):
        v = Vector(self.int_list)
        self.assertIsInstance(1, v.type())
        self.assertEqual(len(v), 5)
        self.assertEqual(list(v.data()), self.int_list)

    def test_init_fail_list_type_mismatch(self):
        with self.assertRaises(TypeError):
            v = Vector([1, 2, 3, 4, 'five'])

    def test_init_fail_args(self):
        with self.assertRaises(Vector.ConstructorFailure):
            v = Vector(1, 2, 3, 4, 5, 6, 7, 8, 9)

    # Test Capacity: 3 tests
    def test_size(self):
        v = Vector(self.int_list)
        self.assertEqual(v.size(), 5)

    def test_empty(self):
        v = Vector()
        self.assertTrue(v.empty())

    def test_empty_false(self):
        self.assertFalse(self.str_fill_vector.empty())

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
        self.assertEqual(list(v.data()), rand_ints)

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
        self.assertEqual(list(v.data()), self.int_list)

    # Test Modifier Methods: 14 tests

    # Push_back(): 2 tests
    def test_push_back(self):
        self.str_fill_vector.push_back('t')
        self.assertEqual(self.str_fill_vector.back(), 't')
        self.assertEqual(len(self.str_fill_vector), 6)

    def test_push_back_type_error(self):
        v = Vector(self.int_list)
        with self.assertRaises(TypeError):
            v.push_back('t')

    # pop_back(): 2 tests
    def test_pop_back(self):
        self.str_fill_vector.push_back('bar')
        self.str_fill_vector.pop_back()
        self.assertEqual(self.str_fill_vector.back(), 'foo')
        self.assertEqual(len(self.str_fill_vector), 5)

    def test_pop_back_fail(self):
        v = Vector()
        with self.assertRaises(Vector.OutOfRangeError):
            v.pop_back()

    # insert(): 3 tests
    def test_insert(self):
        v = Vector(self.int_list)
        v.insert(0, 0)
        self.assertEqual(v.front(), 0)

    def test_insert_fail_type(self):
        v = Vector(self.int_list)
        with self.assertRaises(TypeError):
            v.insert(4, 't')

    def test_insert_fail_range(self):
        v = Vector(self.int_list)
        with self.assertRaises(Vector.OutOfRangeError):
            v.insert(5, 6)

    # erase(): 3 tests
    def test_erase(self):
        v = Vector(self.int_list)
        v.erase(0)
        self.assertEqual(len(v), 4)
        self.assertEqual(v.front(), 2)

    def test_erase_OutOfRange(self):
        v = Vector(self.int_list)
        with self.assertRaises(Vector.OutOfRangeError):
            v.erase(5)

    def test_erase_range(self):
        v = Vector(self.int_list)
        v.erase(0, 5)
        self.assertEqual(len(v), 0)
        with self.assertRaises(Vector.OutOfRangeError):
            v.front()

    def test_erase_range_fail(self):
        v = Vector(self.int_list)
        with self.assertRaises(Vector.OutOfRangeError):
            v.erase(0, 6)

    # swap(): 1 test
    def test_swap(self):
        v = Vector(10, 1)
        u = Vector(self.int_list)
        v.swap(u)
        self.assertEqual(list(v.data()), self.int_list)

    # clear(): 1 test
    def test_clear(self):
        v = Vector(self.int_list)
        v.clear()
        self.assertTrue(v.empty())

    # emplace(): 1 test
    def test_emplace(self):
        self.str_fill_vector.emplace(0, 'bar')
        self.assertEqual(self.str_fill_vector.front(), 'bar')

    # emplace_back(): 1 test
    def test_emplace_back(self):
        self.str_fill_vector.emplace_back('bar')
        self.assertEqual(self.str_fill_vector.back(), 'bar')

    # Test Iterators: 6 Tests
    def test_iter_overload(self):
        l = [1, 2, 3, 4, 5]
        a = Vector(l)

        count = 0
        it = iter(a)
        for elem in l:
            self.assertEqual(next(it), elem)
            count += 1

    def test_rev_iter_(self):
        l = [5, 4, 3, 2, 1]
        a = Vector([1, 2, 3, 4, 5])

        count = 0
        it = a.rbegin()
        for elem in l:
            self.assertEqual(next(it), elem)
            count += 1

    def test_begin(self):
        a = Vector(int)
        for x in range(5):
            a.push_back(x + 1)

        it = a.begin()
        self.assertEqual(a[0], next(it))

    def test_end(self):
        a = Vector(int)
        for x in range(5):
            a.push_back(x + 1)

        it = a.end()
        with self.assertRaises(StopIteration):
            next(it)

    def test_rbegin(self):
        a = Vector(int)
        for x in range(5):
            a.push_back(x + 1)

        it = a.rbegin()
        self.assertEqual(a.back(), next(it))

    def test_rend(self):
        a = Vector(int)
        for x in range(5):
            a.push_back(x + 1)

        it = a.rend()
        with self.assertRaises(StopIteration):
            next(it)


if __name__ == "__main__":
    unittest.main()
