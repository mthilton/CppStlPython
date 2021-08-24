# Matthew Hilton
# July 6th, 2021
#
# Module: Vector.py
#
# This is the port of the Vector module in the C++ Standard
# Template Library. Anything involving pointers or move semantics
# Are either modified or removed. Reverse iterators and const iterators
# are also removed. However vector.data() has been implemented

from typing import Any, List


class Vector():

    __type: type = None
    __data: List = []
    __index = -1
    __size: int = 0

    class ConstructorFailure(Exception):
        pass

    class OutOfRangeError(Exception):
        pass

    class ArgumentError(Exception):
        pass

    def __init__(self, *args) -> None:
        '''
        Written to work similar to C++11's std::vector.

        Parameters:
            * Type:    Sets the type of vector. Must be supplied with 
                       no other arguments
            * Vector:  Must be specified with no other arguments. If
                       a vector is passed, then the it will copy the 
                       contents of the passed vector to the new vector.
            * List of
              values:  A list obj of values that are to be added to the 
                       vector. All items in the list must match the 
                       type of the first element of the list.
            * Size:    Ammount to fill vector. Must be in the first 
                       position
            * Value:   Value to fill vector. Must be the last argument
                       requires a size
        '''
        # Empty Ctor
        if len(args) == 0:
            return

        # Copy ctor
        if len(args) == 1 and isinstance(args[0], Vector):
            self.__type = args[0].__type
            self.__size = len(args[0])
            self.__data = [val for val in args[0].__data]
            return

        # Type instantiation ctor
        if len(args) == 1 and isinstance(args[0], type):
            self.__type = args[0]
            return

        # List obj Ctor
        if len(args) == 1 and isinstance(args[0], list):
            self.__type = type(args[0][0])
            self.__size = len(args[0])
            self.__data = []
            for val in args[0]:
                if not isinstance(val, self.__type):
                    raise TypeError(
                        f"Value '{val}' is of type '{type(val)}' and is not of type '{self.__type}'")
                self.__data.append(val)
            return

        # Fill ctor
        if len(args) == 2 and isinstance(args[0], int):
            self.__type = type(args[1])
            self.__size = args[0]
            self.__data = [args[1] for _ in range(self.__size)]
            return

        # Fallthrough Error
        raise self.ConstructorFailure(
            f"Vector Error (init): Invalid Argument(s). ({args})")

    # Python Magic Methods
    # Magic Python Method to allow for len(vector)
    #
    # Returns the length of the vector
    def __len__(self) -> int:
        return self.__size

    # Magic Python Method that customizes the representation of print(vector)
    def __str__(self) -> str:
        return self.__data.__str__()

    # Magic Python Method that overloads the == method
    def __eq__(self, other: 'Vector') -> bool:
        if self.__size == other.__size and self.__type is other.__type:
            return self.__data == other.__data
        return False

    def _vector_type(self) -> type:
        '''Hidden Helper that returns the type of the vector'''
        return self.__type

    # Iterator Methods
    # rbegin, rend, cbegin, cend, crbegin, crend = delete

    def __iter__(self) -> 'Vector.__type':
        '''Magic Python Method that allows for iter(array)
           Useful for foreach type for loops (ie: for elem in array)'''
        return iter(self.__data)

    def __next__(self) -> 'Vector.__type':
        '''Magic Python Method that allows iter(array) to find the next element'''
        self.__index += 1
        if self.__index < self.__size:
            result = self.__array[self.__index]
            return result
        raise StopIteration

    def begin(self) -> 'Vector.__type':
        '''Returns the iterator to the first element in the array'''
        self.__index = -1
        return self.__next__()

    def end(self) -> 'Vector.__type':
        '''Returns the iterator to the last element in the array'''
        self.__index = self.__size
        return self.__iter__()

    # Capacity Methods

    # The following methods have not been implemented because the underlying
    # data structure is a list, not a statically sized array:
    #
    # max_size()
    # resize()
    # capacity()
    # reserve()
    # shrink_to_fit()

    def size(self) -> int:
        '''Returns the number of elements in the vector'''
        return self.__size

    def empty(self) -> bool:
        '''Checks to see if the vector is empty or not'''
        return self.__size == 0

    # Element Access
    # The following two dunder methods effectivly overload the [] operator

    # Magic Python Method that overloads operator[] access
    #
    # Returns the value at the given index
    def __getitem__(self, i: int) -> 'Vector.__type':
        if i >= self.__size:
            raise IndexError(
                f"VectorError (Operator[]): Index '{i}' is not in the bounds of the Vector. (Max index: {self.__size - 1})")
        return self.__data[i]

    # Magic Python Method that overloads operator[] assign
    #
    # Sets the array to the passed value at the passed index
    def __setitem__(self, i: int, value: 'Vector.__type') -> None:
        if isinstance(None, self.__type):
            self.__type = type(value)
        if i >= self.__size:
            raise IndexError(
                f"VectorError (Operator[]): Index '{i}' is not in the bounds of the Vector. (Max index: {self.__size - 1})")
        if not isinstance(value, self.__type):
            raise TypeError(
                f"VectorError (Operator[]): Value '{value}' is of type '{type(value)}' when type '{self.__type}' was expected.")
        self.__data[i] = value

    # Simialar to the previous Dunder methods; please just use the [] operator
    def at(self, i: int, *value: Any) -> Any:
        '''Returns the element at the given location. Will not accept assignments
           (ie: vector.at() = value) however if you want to set the value at
           that location add the value as an argument (ie: array.at(index, value))'''
        if len(value) == 0:
            return self.__getitem__(i)

        if len(value) == 1:
            self.__setitem__(i, value[0])
            return

        raise self.ArgumentError(
            f"Invalid Arguments. Expected Either an index or an index and a value. (args: {i}, {value})")

    def front(self) -> 'Vector.__type':
        '''Returns the first element in the array'''
        if self.__size < 1:
            raise self.OutOfRangeError(
                f"Vector Error (front): Vector is empty")
        return self.__data[0]

    def back(self) -> 'Vector.__type':
        '''Returns the last element in the array'''
        if self.__size < 1:
            raise self.OutOfRangeError(
                f"Vector Error (front): Vector is empty")
        return self.__data[-1]

    def data(self) -> List['Vector.__type']:
        '''Returns a list containing the curent vector'''
        return self.__data

    # Modifiers
    # These functions are not implemented becuase
    # assign(): Relates to iterables. Iterables are
    #           fundamentally different in python than c++

    def push_back(self, val: 'Vector.__type') -> None:
        pass

    def pop_back(self):
        pass

    def insert(self):
        pass

    def erase(self):
        pass

    def swap(self):
        pass

    def clear(self):
        pass

    def emplace(self):
        pass

    def emplace_back(self):
        pass
