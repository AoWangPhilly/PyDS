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
        node = Node(value, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.size += 1

    def search(self, target: Any) -> int:
        tmp = self.head
        i = 0
        while tmp:
            if tmp.value == target:
                return i
            tmp = tmp.next
            i += 1
        return i

    def remove_front(self):
        if self.is_empty():
            raise Empty('Doubly Linked List is empty')
        
    def remove_end(self):
        if self.is_empty():
            raise Empty('Doubly Linked List is empty')

    def remove(self):
        if self.is_empty():
            raise Empty('Doubly Linked List is empty')

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
    from random import randint
    ll = DoublyLinkedList()
    for i in [49, 24, 95, 89, 39, 98, 44, 10, 14]:
        ll.append(i)

    print(ll.search(14))