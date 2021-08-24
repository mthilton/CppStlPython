# Matthew Hilton
# July 3st, 2021
#
# Test Module: array.py
#
# Imports
import unittest

from CppStlPython import Array
from random import randint


class test_array(unittest.TestCase):

    def setUp(self):
        self.empty_array = Array()
        self.copy_int_array_5 = Array()
        self.int_array_5 = Array(int, 5)
        self.int_array_10 = Array(int, 10)
        self.int_array_100 = Array(int, 100)
        self.fs_int_array_400 = Array(int, 400)
        self.snd_int_array_400 = Array(int, 400)
        self.str_array_100 = Array(str, 100)

    # Test Array Unit Test Helpers: 2 Tests
    def test_array_data_is_list(self):
        self.assertIsInstance(self.empty_array.data(), list)

    def test_array_type_is_proper_type(self):
        self.assertIsInstance(None, self.empty_array.array_type())

    # Test Init: 5 test
    def test_init_empty(self):
        self.assertIsInstance(None, self.empty_array.array_type())
        self.assertEqual(len(self.empty_array), 0)
        self.assertEqual(self.empty_array.data(), [])

    def test_init_int_len_5_(self):
        self.assertIsInstance(0, self.int_array_5.array_type())
        self.assertEqual(len(self.int_array_5), 5)
        self.assertEqual(self.int_array_5.data(),
                         [int for _ in range(5)])

    def test_init_str_len_100_(self):
        self.assertIsInstance('sa', self.str_array_100.array_type())
        self.assertEqual(len(self.str_array_100), 100)
        self.assertEqual(self.str_array_100.data(),
                         [str for _ in range(100)])

    def test_init_none_len_100_(self):
        a = Array(100)
        self.assertEqual(a.array_type(), type(None))
        self.assertEqual(len(a), 100)
        self.assertEqual(a.data(), [None for _ in range(100)])

    def test_copy_init(self):
        self.copy_int_array_5 = Array(self.int_array_5)
        self.assertEqual(self.int_array_5, self.copy_int_array_5)
        self.copy_int_array_5[0] = 100
        self.assertNotEqual(self.int_array_5, self.copy_int_array_5)

    # Test Capacity Methods: 3 Tests
    def test_size(self):
        self.assertEqual(len(self.int_array_5), self.int_array_5.size())

    def test_max_size(self):
        self.assertEqual(len(self.int_array_5), self.int_array_5.max_size())

    def test_empty(self):
        empty = True
        for i in range(len(self.int_array_5)):
            try:
                x = self.int_array_5[i]
            except self.int_array_5.UninitalizedValueError:
                continue
            empty = False

        self.assertTrue(empty)

    # Test Element Access: 10 Tests
    # Array[]: 8 Tests
    def test_setitem(self):
        self.int_array_5[0] = 5
        self.assertEqual(self.int_array_5.data()[0], 5)

    def test_setitem_fail_index(self):
        with self.assertRaises(IndexError):
            self.int_array_5[5] = 5

    def test_setitem_fail_type(self):
        with self.assertRaises(TypeError):
            self.int_array_5[0] = "x"

    def test_setitem_loop(self):
        rand_ints = []
        for i in range(len(self.int_array_10)):
            temp = randint(0, 100) % (i + 1)
            self.int_array_10[i] = temp
            rand_ints.append(temp)
        self.assertEqual(self.int_array_10.data()[i], rand_ints[i])

    def test_getitem(self):
        self.int_array_5[0] = 5
        self.assertEqual(self.int_array_5[0], 5)

    def test_getitem_loop(self):
        rand_ints = []
        for i in range(len(self.int_array_10)):
            temp = randint(0, 100) % (i + 1)
            self.int_array_10[i] = temp
            self.assertEqual(self.int_array_10[i], temp)

    def test_getetitem_fail_index(self):
        with self.assertRaises(IndexError):
            x = self.int_array_5[5]

    def test_getetitem_fail_unititalize(self):
        with self.assertRaises(Array.UninitalizedValueError):
            x = self.int_array_5[0]

    # At: 3 tests:
    def test_at_getitem(self):
        for x in range(5):
            self.int_array_5[x] = x + 5
        self.assertEqual(self.int_array_5.at(0), 5)

    def test_at_setitem(self):
        for x in range(5):
            self.int_array_5[x] = x + 5
        self.int_array_5.at(0, 0)
        self.assertEqual(self.int_array_5.at(0), 0)

    def test_at_setitem(self):
        with self.assertRaises(Array.ArgumentError):
            self.int_array_5.at(0, 0, "a", None)

    # Front: 2 Test
    def test_front(self):
        self.int_array_5[0] = 42
        self.assertEqual(self.int_array_5[0], self.int_array_5.front())

    def test_front_fail(self):
        with self.assertRaises(Array.UninitalizedValueError):
            x = self.int_array_5.front()

    # Back: 2 Test
    def test_back(self):
        self.int_array_5[4] = 42
        self.assertEqual(self.int_array_5[4], self.int_array_5.back())

    def test_back_fail(self):
        with self.assertRaises(Array.UninitalizedValueError):
            self.int_array_5.fill(None)
            x = self.int_array_5.back()

    # Test iterators: 1 Test
    def test_itr(self):
        self.int_array_5.fill(None)
        i = 0
        for j in range(len(self.int_array_5)):
            self.int_array_5[j] = j
        for elem in self.int_array_5:
            self.assertEqual(elem, self.int_array_5[i])
            i += 1

    # Test Modifiers: 6 Tests
    # Fill: 3 Test
    def test_fill_success(self):
        self.fs_int_array_400.fill(40)
        for i in range(len(self.snd_int_array_400)):
            self.snd_int_array_400[i] = 40
        self.assertEqual(self.fs_int_array_400, self.snd_int_array_400)

    def test_fill_succes_empty(self):
        self.int_array_5.fill(None)
        self.assertEqual(self.int_array_5, Array(int, 5))

    def test_fill_fail_type(self):
        with self.assertRaises(TypeError):
            self.int_array_5.fill('x')

    # Swap: 3 Tests
    def test_swap_success(self):
        self.fs_int_array_400.fill(40)
        self.snd_int_array_400.fill(50)
        self.fs_int_array_400.swap(self.snd_int_array_400)
        for i in range(len(self.fs_int_array_400)):
            self.assertEqual(self.fs_int_array_400[i], 50)
            self.assertEqual(self.snd_int_array_400[i], 40)

    def test_swap_fail_typing(self):
        with self.assertRaises(TypeError) as cm:
            self.int_array_100.fill(10)
            self.str_array_100.fill('x')
            self.int_array_100.swap(self.str_array_100)

    def test_swap_fail_size(self):
        with self.assertRaises(Array.SizeError):
            self.int_array_5.fill(5)
            self.int_array_10.fill(10)
            self.int_array_10.swap(self.int_array_5)


if __name__ == "__main__":
    unittest.main()
