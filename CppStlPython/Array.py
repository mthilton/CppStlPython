# Matthew Hilton
# July 1st, 2021
#
# Module: array.py
#
# This is the port of the array module in the C++ Standard
# Template Library. Anything involving pointers or move semantics
# Are either modified or removed. Reverse iterators and const iterators
# are also removed. However array.data() has been implemented.

# Imports
from typing import Any, List


class Array():

    __size: int = 0
    __type: type = None
    __data: List[type] = []
    __defined: List[bool] = []
    __index: int = -1

    class UninitalizedValueError(Exception):
        pass

    class SizeError(Exception):
        pass

    class ArgumentError(Exception):
        pass

    class ConstructorFailure(Exception):

        def __init__(self, errno: int, *keys):
            errors = [
                f"Args '{keys[0]}' and '{keys[1]}' cannot be used together",
                "Arg 'type' cannot be used without 'size'",
                f"Two arg constructor expected a 'type' then a 'size' but recieved: ({type(keys[0])}, {type(keys[1])})",
                f"Single arg constructor expected an int or an Array but got {type(keys[0])}"
                f"Invalid Args: {keys}"
            ]
            self.message = "Array error (init): " + errors[errno]
            super.__init__(self.message)

    def __init__(self, *args) -> None:
        '''
        Written to work similar to C++11's std::array.

        Parameters:
            * Type:  Sets the type of array. Must be supplied with 
                     a size and 'type' must be in the first position
            * Size:  Sets the size of the array. Can be supplied
                     by itself or with type. If specified with type 
                     this must be the second argument. Otherwise
                     it must be the first and only argument. If it
                     is the only argument, the array will be an array
                     of None. The first item you add will set its type
            * Array: Must be specified with no other arguments. If
                     an array is passed, then the it will copy the 
                     contents of the passed array to the new array.
        '''
        invalid_args = []
        errno = -1

        # Empty array ctor
        if len(args) == 0:
            self.__size = 0
            self.__data = []
            self.__type = type(None)
            self.__defined = []
            return

        # Type checking of values
        if len(args) > 0 and not (isinstance(args[0], type) or
                                  isinstance(args[0], int) or
                                  isinstance(args[0], Array)):
            invalid_args.append(args[0])
            errno = 4

        if len(args) > 1 and not isinstance(args[1], int):
            invalid_args.append(args[1])
            errno = 4

        if len(args) > 2:
            invalid_args += list(args[2:])
            errno = 4

        if errno < 0:

            # Ctor Arg Mismatch
            if len(args) == 2 and isinstance(args[1], Array):
                if isinstance(args[0], int):
                    errno = 0
                    invalid_args = ['size', 'Array']

                if isinstance(args[0], type):
                    errno = 0
                    invalid_args = ['type', 'Array']

            # Type only Ctor Failure
            if len(args) == 1 and isinstance(args[0], type):
                errno = 1

            # Type and size Ctor
            if len(args) == 2:
                if isinstance(args[0], type) and isinstance(args[1], int):
                    self.__size = args[1]
                    self.__data = [args[0]] * args[1]
                    self.__type = args[0] if args[0] is not None else type(
                        None)
                    self.__defined = [False] * args[1]
                    return
                errno = 2
                invalid_args = list(args)

            if len(args) == 1:
                # Size Ctor
                if isinstance(args[0], int):
                    self.__size = args[0]
                    self.__data = [None] * args[0]
                    self.__type = type(None)
                    self.__defined = [False] * args[0]
                    return
                # Copy Ctor
                if isinstance(args[0], Array):
                    self.__size = args[0].__size
                    self.__type = args[0].__type
                    for i in range(len(args[0])):
                        self.__data.append(args[0].__data[i])
                        self.__defined.append(args[0].__defined[i])
                    return
                errno = 3
                invalid_args = list(args)

        raise self.ConstructorFailure(errno, *invalid_args)

    def __len__(self) -> int:
        '''Returns the length of the array'''
        return self.__size

    def __str__(self) -> str:
        '''Generates a string representation of the array. If a value shows '/U/',
           the value at that index is uninitialized'''

        s = "["
        for i in range(self.__size):
            s += str(self.__data[i]) if self.__defined[i] else "/U/"
            if i != self.__size - 1:
                s += ", "
        s += "]"
        return s

    def __eq__(self, other) -> bool:
        '''Magic Python Method that overloads the == method'''

        if self.__size == len(other) and self.__type is other.__type:
            for i in range(self.__size):
                if self.__data[i] != other.__data[i]:
                    return False
            return True
        return False

    def array_type(self) -> Any:
        '''Returns the type that is allowed in the current array'''
        return self.__type

    # Iterator Methods
    # rbegin, rend, cbegin, cend, crbegin, crend = delete

    def __iter__(self) -> Any:
        '''Magic Python Method that allows for iter(array)
           Useful for foreach type for loops (ie: for elem in array)'''
        return iter(self.__data)

    def __next__(self) -> Any:
        '''Magic Python Method that allows iter(array) to find the next element'''
        self.__index += 1
        if self.__index < self.__size:
            result = self.__array[self.__index]
            return result
        raise StopIteration

    def begin(self) -> Any:
        '''Returns the iterator to the first element in the array'''
        self.__index = -1
        return self.__next__()

    def end(self) -> Any:
        '''Returns the iterator to the last element in the array'''
        self.__index = self.__size
        return self.__iter__()

    # Capacity Methods

    def size(self) -> int:
        '''Returns the size of the array
           You really should use len(array) but, is included to match C++ STL'''
        return self.__size

    def max_size(self) -> int:
        '''Returns the size of the array
           You really should use len(array) but, is included to match C++ STL'''
        return self.__size

    def empty(self) -> bool:
        '''Returns true if array is empty'''
        return isinstance(None, self.__type)

    # Element Access
    # The following two dunder methods effectivly overload the [] operator

    # Magic Python Method that overloads operator[] access
    #
    # Returns the value at the given index
    def __getitem__(self, i: int) -> Any:
        if i >= self.__size:
            raise IndexError(
                f"ArrayError (Operator[]): Index '{i}' is not in the bounds of the array. (Max index: {self.__size - 1})")
        if not self.__defined[i]:
            raise self.UninitalizedValueError(
                f"ArrayError (Operator[]): Value at index '{i}' is undefined")

        return self.__data[i]

    # Magic Python Method that overloads operator[] assign
    #
    # Sets the array to the passed value at the passed index
    def __setitem__(self, i: int, value: Any) -> None:
        if isinstance(None, self.__type):
            self.__type = type(value)
        if i >= self.__size:
            raise IndexError(
                f"ArrayError (Operator[]): Index '{i}' is not in the bounds of the array. (Max index: {self.__size - 1})")
        if not isinstance(value, self.__type):
            raise TypeError(
                f"ArrayError (Operator[]): Value '{value}' is of type '{type(value)}' when type '{self.__type}' was expected.")
        self.__data[i] = value
        self.__defined[i] = True

    # Simialar to the previous Dunder methods; please just use the [] operator
    def at(self, i: int, *value: Any) -> Any:
        '''Returns the element at the given location. Will not accept assignments
           (ie: array.at() = value) however if you want to set the value at
           that location add the value as an argument (ie: array.at(index, value))'''
        if len(value) == 0:
            return self.__getitem__(i)

        if len(value) == 1:
            self.__setitem__(i, value[0])
            return

        raise self.ArgumentError(
            f"Invalid Arguments. Expected Either an index or an index and a value. ({value})")

    def front(self) -> Any:
        '''Returns the first element in the array'''
        if not self.__defined[0]:
            raise self.UninitalizedValueError(f"First value is undefined")
        return self.__data[0]

    def back(self) -> Any:
        '''Returns the last element in the array'''
        if not self.__defined[-1]:
            raise self.UninitalizedValueError(f"Last value is undefined")
        return self.__data[-1]

    def data(self) -> List[Any]:
        '''
        Returns a list containing the curent array

        This will return the underlying list that the array is stored as. 
        Order will be preserved but elements that are listed as undefined in
        the array will be set to None
        '''
        return self.__data

    # Modifiers

    def fill(self, val: Any) -> None:
        '''Fills the array with the passed value.
           To make the array empty, call fill(None)'''
        # Sets array to be empty
        if val is None:
            self.__data = [self.__type] * self.__size
            self.__defined = [False] * self.__size
            self.__index = -1
            return

        # Fill Array with current type
        if isinstance(val, self.__type):
            self.__data = [val for _ in range(self.__size)]
            self.__defined = [
                False if val is None else True for _ in range(self.__size)]
            return

        # Invalid type
        raise TypeError(
            f"Array Error (fill): Value '{val}' is of type '{type(val)}' when type '{self.__type}' was expected.")

    def swap(self, a: 'Array') -> None:
        '''Swaps the LHS elements with the RHS elements'''
        # This version has excpetions due to the fact that there are no compile
        # time errors for type checking and bounds checking.
        if self.__type is not a.__type:
            raise TypeError(
                f"ArrayError (swap): LHS array is of type '{self.__type}' and RHS array is of type '{a.__type}.'")
        if self.__size != a.__size:
            raise self.SizeError(
                f"ArrayError (swap): LHS is of length '{self.__size,}' while RHS is of length '{a.__size}.'")
        for i in range(self.__size):
            temp = self.__data[i], self.__defined[i]
            self.__data[i] = a.__data[i]
            self.__defined[i] = a.__defined[i]
            a.__data[i] = temp[0]
            a.__defined[i] = temp[1]
