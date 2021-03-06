# Matthew Hilton
# July 6th, 2021
'''
Module: Vector.py

This is the port of the Vector module in the C++ Standard
Template Library. Anything involving pointers or move semantics
Are either modified or removed. Const iterators are also removed.
However vector.data() has been implemented
'''
from typing import Any, List, Tuple


class Vector():

    '''
    This is the main Vector class. It is statically typed but dynamically sized. The type of the
    items in this vector are guarenteed to all be the same. For more information visit:

    https://www.cplusplus.com/reference/vector/vector/
    '''

    __type: type = None
    __data: List = []
    __size: int = 0

    class ConstructorFailure(Exception):
        '''
        Rasied if the constructor does not receive the proper arguments
        '''

    class OutOfRangeError(Exception):
        '''
        Rasied if the user attempts to access not in range of the Vector
        '''

    class ArgumentError(Exception):
        '''
        Rasied if a memeber function does not receive thee proper arguments
        '''

    class VectorIterator:
        '''
        An iterator class for vector
        '''

        def __init__(self, vector: 'Vector', index: int = -1) -> None:
            self.__vector: 'Vector' = vector
            self.__size: int = len(vector)
            self.__index: int = index

        def __next__(self) -> None:
            self.__size: int = len(self.__vector)
            self.__index += 1
            if self.__index < self.__size:
                return self.__vector[self.__index]
            raise StopIteration

    class VectorReverseIterator:
        '''
        An iterator class for vector that will iterate backwards
        '''

        def __init__(self, vector: 'Vector', end: bool = False) -> None:
            self.__vector: 'Vector' = vector
            self.__size: int = len(vector)
            self.__index: int = self.__size if end is False else 0

        def __next__(self) -> None:
            self.__size: int = len(self.__vector)
            self.__index -= 1
            if self.__index > -1:
                return self.__vector[self.__index]
            raise StopIteration

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
            self.__type = None
            self.__data = []
            self.__size = 0
            return

        # Copy ctor
        if len(args) == 1 and isinstance(args[0], Vector):
            self.__type = args[0].__type
            self.__size = len(args[0])
            self.__data = args[0].__data
            return

        # Type instantiation ctor
        if len(args) == 1 and isinstance(args[0], type):
            self.__type = args[0]
            self.__data = []
            self.__size = 0
            return

        # List obj Ctor
        if len(args) == 1 and isinstance(args[0], list):
            self.__type = type(args[0][0])
            self.__size = len(args[0])
            self.__data = []
            for val in args[0]:
                if not isinstance(val, self.__type):
                    raise TypeError(
                        f"Vector Error (init): Value '{val}' is of type '{type(val)}' and is not \
                            of type '{self.__type}'")
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

    def type(self) -> type:
        '''Hidden Helper that returns the type of the vector'''
        return self.__type

    # Iterator Methods
    # rbegin, rend, cbegin, cend, crbegin, crend = delete

    def __iter__(self) -> Any:
        '''Magic Python Method that allows for iter(vector)
           Useful for foreach type for loops (ie: for elem in vector)'''
        return self.VectorIterator(self)

    def begin(self) -> Any:
        '''Returns the iterator to the first element in the vector'''
        return self.VectorIterator(self)

    def end(self) -> Any:
        '''Returns the iterator to the last element in the vector'''
        return self.VectorIterator(self, self.__size - 1)

    def rbegin(self) -> 'VectorReverseIterator':
        '''
        Returns the iterator to the last element in the vector.

        When next is called, you will go to the previous element
        in the vector.
        '''
        return self.VectorReverseIterator(self)

    def rend(self) -> 'VectorReverseIterator':
        '''
        Returns the iterator to the last element in the vector

        When next is called, you will go to the previous element
        in the vector.
        '''
        return self.VectorReverseIterator(self, end=True)

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
    def __getitem__(self, i: int) -> Any:
        if i >= self.__size:
            raise IndexError(
                f"VectorError (Operator[]): Index '{i}' is not in the bounds of the Vector. \
                    (Max index: {self.__size - 1})")
        return self.__data[i]

    # Magic Python Method that overloads operator[] assign
    #
    # Sets the value in the vector to the passed value at the passed index
    def __setitem__(self, i: int, value: Any) -> None:
        if isinstance(None, self.__type):
            self.__type = type(value)
        if i >= self.__size:
            raise IndexError(
                f"VectorError (Operator[]): Index '{i}' is not in the bounds of the Vector. \
                    (Max index: {self.__size - 1})")
        if not isinstance(value, self.__type):
            raise TypeError(
                f"VectorError (Operator[]): Value '{value}' is of type '{type(value)}' when type \
                    '{self.__type}' was expected.")
        self.__data[i] = value

    # Simialar to the previous Dunder methods; please just use the [] operator
    def at(self, i: int, *value: Any) -> Any:
        '''Returns the element at the given location. Will not accept assignments
           (ie: vector.at() = value) however if you want to set the value at
           that location add the value as an argument (ie: vector.at(index, value))'''
        if len(value) == 0:
            return self.__getitem__(i)

        if len(value) == 1:
            self.__setitem__(i, value[0])
            return None

        raise self.ArgumentError(
            f"Vector Error (at): Invalid Arguments. Expected Either an index or an index and a \
                value. (args: {i}, {value})")

    def front(self) -> Any:
        '''Returns the first element in the vector'''
        if self.__size < 1:
            raise self.OutOfRangeError("Vector Error (front): Vector is empty")
        return self.__data[0]

    def back(self) -> Any:
        '''Returns the last element in the vector'''
        if self.__size < 1:
            raise self.OutOfRangeError("Vector Error (back): Vector is empty")
        return self.__data[-1]

    def data(self) -> Tuple[Any]:
        '''
        Returns the underlying list as a tuple to maintain the state of the vector when this
        method is called.

        Order of elements is preserved.
        '''
        return tuple(self.__data)

    # Modifiers
    # These functions are not implemented becuase
    # assign(): Relates to iterables. Iterables are
    #           fundamentally different in python than c++

    def push_back(self, val: Any) -> None:
        '''
        Adds an element to the end of the vector.

        Raises a type error if passed value is not of the same type as the Vector
        '''
        if not isinstance(val, self.__type):
            raise TypeError(
                f"Vector Error (push_back): Value '{val}' is of type '{type(val)}' and is not of \
                    type '{self.__type}'")
        self.__data.append(val)
        self.__size += 1

    def pop_back(self) -> None:
        '''
        Pops of (removes) the last element in the vector

        If the vector is empty, raises Vector.EmptyError
        '''
        if self.__size < 1:
            raise self.OutOfRangeError(
                "Vector Error (pop_back): Unable to pop back the last element, Vector is empty!")
        self.__data.pop()
        self.__size -= 1

    def insert(self, i: int, val: Any) -> None:
        '''
        Inserts the value (val) at the location (i)

        i must be 0 <= i < Vector.size()
        val must be of the same type as the other elements in the vector
        '''

        if i < 0 or i >= self.__size:
            raise self.OutOfRangeError(
                f"Vector Error (insert): Invalid Index (Value: {i} is not 0 <= i < {self.__size})")

        if not isinstance(val, self.__type):
            raise TypeError(
                f"Vector Error (insert): Value '{val}' is of type '{type(val)}' and is not of \
                    type '{self.__type}'")

        self.__data.insert(i, val)
        self.__size += 1

    def erase(self, i: int, r: int = 1) -> None:
        '''
        Deletes the value at the location (i)

        i must be 0 <= i < Vector.size()
        '''
        if i < 0 or i >= self.__size:
            raise self.OutOfRangeError(
                f"Vector Error (insert): Invalid Index (Value: {i} is not 0 <= i < {self.__size})")

        if i + r > self.__size:
            raise self.OutOfRangeError(
                f"Vector Error (insert): Invalid Range, index + range must not exceed \
                    vector.size! ({i} + {r} > {self.__size})")

        for _ in range(r):
            self.__data.pop(i)
            self.__size -= 1

    def swap(self, v: 'Vector') -> None:
        '''Swaps the LHS elements with the RHS elements'''
        # This version has excpetions due to the fact that there are no compile
        # time errors for type checking and bounds checking.
        if self.__type is not v.__type:
            raise TypeError(
                f"ArrayError (swap): LHS vector is of type '{self.__type}' and RHS vector is of \
                    type '{v.__type}.'")

        # Generate temp list
        temp_li = self.__data

        # Clear values in lists, then -replace them with the items in the other list
        self.__data.clear()
        for item in v.__data:
            self.__data.append(item)

        v.__data.clear()
        for item in temp_li:
            v.__data.append(item)

        # Setting the sizes of the respective vectors.
        temp = self.__size
        self.__size = v.__size
        v.__size = temp

    def clear(self) -> None:
        '''
        Clears the vector of any items
        '''
        self.__size = 0
        self.__data.clear()

    def emplace(self, i: int, *args) -> None:
        '''
        Creates a new obj based on Vector.type and inserts it into the Vector at
        index (i).

        If i is not in range, this function will raise an OutOfRangeError
        '''
        if i < 0 or i >= self.__size:
            raise self.OutOfRangeError(
                f"Vector Error (emplace): Invalid Index (Value: {i} is not 0 <= i < {self.__size})")

        self.__data.insert(i, self.__type(*args))
        self.__size += 1

    def emplace_back(self, *args) -> None:
        '''
        Creates a new obj based on Vector.type and appends it to the end of the vector
        '''
        self.__data.append(self.__type(*args))
        self.__size += 1
