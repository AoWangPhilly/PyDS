from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from PyDS.Error import Empty


@dataclass
class Node:
    """Implementation of Node containing a value
       and pointing to the next node.
    """
    value: Any
    next: Optional[Node]


@dataclass
class LinkedList:
    """Implementation of Singly Linked List

    :param head: A node at the front of list
    :type head: Optional[Node]
    :param tail: A node at the end of list
    :type head: Optional[Node]
    :param size: The length of list
    :type size: int
    """
    head: Optional[Node] = None
    tail: Optional[Node] = None
    size: int = 0

    def append(self, value: Any) -> None:
        """Adds node to the end of list

        :param value: A value
        :type value: Any
        """
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
        """Adds node to the front of list

        :param value: A value
        :type value: Any
        """
        node = Node(value, None)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def search(self, target: Any) -> int:
        """Searches value in list and retrieves its index

        :param target: The value you need to find
        :type target: Any
        :return: The index of value found, otherwise -1
        :rtype: int
        """
        tmp = self.head
        i = 0
        while tmp:
            if tmp.value == target:
                return i
            tmp = tmp.next
            i += 1
        return -1

    def get_at(self, index: int) -> Any:
        """Gets value at a certain index

        :param index: The index of the value you're trying to get
        :type index: int
        :return: The value at certain index
        :rtype: Any
        """
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
        """Removes node at the front of list
        """
        if self.is_empty():
            raise Empty("Linked List is empty")

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1

    def remove_last(self) -> None:
        """Removes node at end of list
        """
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
        """Removes node containing a certain value

        :param target: The value you're trying to delete
        :type target: Any
        """
        if self.is_empty():
            raise Empty("Linked List is empty")

        tmp = self.head

        # Remove front
        if tmp.value == target:
            self.remove_front()
            return

        # Remove in between
        while tmp != self.tail:
            if tmp.value == target:
                break
            prev = tmp
            tmp = tmp.next

        # Remove at end
        if tmp.value == target:
            if tmp == self.tail:
                self.tail = prev
            else:
                prev.next = tmp.next
            self.size -= 1

    def is_empty(self) -> bool:
        """Checks to see if linked list is empty

        :return: Whether or not list is empty
        :rtype: bool
        """
        return self.size == 0

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        if self.head is not None and self.tail is not None:
            output = 'LinkedList(['
            tmp = self.head
            while tmp != self.tail:
                output += f'{tmp.value}, '
                tmp = tmp.next

            output += f'{tmp.value}])'
            return output

        return 'LinkedList([])'
