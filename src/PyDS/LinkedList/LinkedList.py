from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from PyDS.Error import Empty


@dataclass
class Node:
    value: Any
    next: Optional[Node]


@dataclass
class LinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    size: int = 0

    def append(self, value: Any) -> None:
        node = Node(value, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            tmp = self.tail
            tmp.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value: Any) -> None:
        node = Node(value, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def search(self, target: Any) -> int:
        tmp = self.head
        i = 0
        while tmp:
            if tmp.value == target:
                return i
            tmp = tmp.next
            i += 1
        return -1

    def get_at(self, index: int) -> Any:
        if self.is_empty():
            raise Empty("Linked List is empty")

        if index < 0 or index > self.size - 1:
            raise IndexError('Index is out of bounds')

        tmp = self.head
        i = 0
        while tmp:
            if i == index:
                return tmp.value
            tmp = tmp.next
            i += 1

    def remove_front(self) -> None:
        if self.is_empty():
            raise Empty("Linked List is empty")

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def remove_last(self) -> None:
        if self.is_empty():
            raise Empty("Linked List is empty")

        tmp = self.head

        if tmp.next is None:
            self.head = None
            self.tail = None

        while tmp != self.tail:
            prev = tmp
            tmp = tmp.next

        self.tail = prev
        self.size -= 1

    def remove(self, target: Any) -> None:
        if self.is_empty():
            raise Empty("Linked List is empty")

    def remove_at(self, index: int) -> None:
        if self.is_empty():
            raise Empty("Linked List is empty")

    def is_empty(self) -> bool:
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self.head is None or self.tail is None:
            return 'LinkedList([])'

        output = 'LinkedList(['
        tmp = self.head
        while tmp != self.tail:
            output += f'{tmp.value}, '
            tmp = tmp.next

        output += f'{tmp.value}])'
        return output


# if __name__ == '__main__':
#     ll = LinkedList()
#     arr = range(5)
#     for i in arr:
#         ll.prepend(i)
#
#     print(ll)
