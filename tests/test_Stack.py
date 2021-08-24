from typing import TypeVar, Generic

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(2)
    print((stack.pop()))
    stack.push('x')
    print((stack.pop()))
