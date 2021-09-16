from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional
from PyDS.Node import DoublyNode
from PyDS.Error import Empty


@dataclass
class DoublyLinkedList:
    head: Optional[DoublyNode] = None
    tail: Optional[DoublyNode] = None
    size: int = 0

    def prepend(self, value: Any) -> None:
        node = DoublyNode(value, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.size += 1

    def append(self, value: Any) -> None:
        node = DoublyNode(value, None, None)
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
        return -1

    def remove_front(self) -> None:
        if self.is_empty():
            raise Empty('Doubly Linked List is empty')

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def remove_end(self):
        if self.is_empty():
            raise Empty('Doubly Linked List is empty')

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

    def remove(self, target: Any) -> None:
        if self.is_empty():
            raise Empty('Doubly Linked List is empty')

        tmp = self.head

        if tmp.value == target:
            self.remove_front()
            return

        while tmp != self.tail:
            if tmp.value == target:
                break
            tmp = tmp.next

        if tmp.value == target:
            if tmp == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                tmp.prev.next = tmp.next
            self.size -= 1

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

