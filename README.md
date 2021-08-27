# CppStlPython
A port of the C++ Standard Template Library to Python. All templates have been ported as best as possible. Template methods that refer to move semantics and memory management have been omitted. Those features are not supported in Python. Furthermore, iteration functions in a Pythonic fashion rather than in a C++ fashion.

## Requirements
- Python 3.5
- pip

## Quickstart Guide

To install this package, use the pip.

```bash
pip3 install CppStlPython
```

Once you have installed this package, make sure to import it.

Importing the entire package
```python
   import CppStlPython
```

Importing specific containers
```python
   from CppStlPython import Array, Vector
```

## Container Status
| Container Name | Completion Status |
| ---------------|:-----------------:|
| [Array][A] | :heavy_check_mark: |
| [Deque][D] | :black_square_button: |
| [Forward List][FL] | :black_square_button: |
| [List][L] | :black_square_button: |
| [Map][M] | :black_square_button: |
| [Queue][Q] | :black_square_button: |
| [Set][ST] | :black_square_button: |
| [Stack][SA] | :black_square_button: |
| [Unordered Map][UM] | :black_square_button: |
| [Unordered Set][US] | :black_square_button: |
| [Vector][V] | :heavy_check_mark: |


<!-- Identifiers, in alphabetical order -->

[A]: https://www.cplusplus.com/reference/array "Array"
[D]: https://www.cplusplus.com/reference/Deque "Deque"
[FL]: https://www.cplusplus.com/reference/Forward_List "Forward List"
[L]: https://www.cplusplus.com/reference/List "List"
[M]: https://www.cplusplus.com/reference/Map "Map"
[Q]: https://www.cplusplus.com/reference/Queue "Queue"
[ST]: https://www.cplusplus.com/reference/Set "Set"
[SA]: https://www.cplusplus.com/reference/Stack "Stack"
[UM]: https://www.cplusplus.com/reference/Unordered_Map "Unordered_Map"
[US]: https://www.cplusplus.com/reference/Unordered_Set "Unordered_Set"
[V]: https://www.cplusplus.com/reference/Vector "Vector"

