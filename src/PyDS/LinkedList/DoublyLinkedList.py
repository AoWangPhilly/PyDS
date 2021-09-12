from __future__ import annotations

from dataclasses import dataclass
from PyDS.Error import Empty
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    next: Node
    prev: Node


@dataclass
class DoublyLinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    size: int = 0

    def prepend(self, value: Any) -> None:
        node = Node(value, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1

    def append(self, value: Any) -> None:
        ...

    def search(self, target: Any) -> int:
        ...

    def remove_front(self):
        ...

    def remove_end(self):
        ...

    def remove(self):
        ...

    def is_empty(self):
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self.is_empty():
            return 'DoublyLinkedList([])'

        output = 'DoublyLinkedList(['
        tmp = self.head
        while tmp != self.tail:
            output += f'{tmp.value}, '
            tmp = tmp.next

        output += f'{tmp.value}])'
        return output

if __name__ == '__main__':
    ll = DoublyLinkedList()
    for i in range(10):
        ll.prepend(i)

    print(ll)