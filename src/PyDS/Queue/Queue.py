from typing import Any, List
from dataclasses import dataclass, field
from PyDS.Error import Empty


@dataclass
class Queue:
    """Implementation of Queue ADT

    :param __capacity: The maximum number of elements a queue can hold
    :type __capacity: int
    :param __list: A container that holds n-elements in queue
    :type __list: list[Any]
    :param __front: The index pointing at front of queue
    :type __front: int
    :param __size: The size of the queue
    :type __size: int
    """
    __capacity: int = 64
    __list: List[Any] = field(default_factory=lambda: [None] * Queue.__capacity)
    __front: int = 0
    __size: int = 0

    def enqueue(self, value: Any) -> None:
        """Insertion to the tail of the queue

        :param value: The value inserting to the tail
        :type value: Any
        """
        if self.__size == self.__capacity:
            self.__resize(capacity=2 * self.__capacity)
        end = (self.__front + self.__size) % self.__capacity
        self.__list[end] = value
        self.__size += 1

    def dequeue(self) -> Any:
        """Deletion at the front of the queue

        :return: A value at the front of queue
        :rtype: Any
        """
        if self.is_empty():
            raise Empty("Queue is empty")

        if 0 < self.__size < (self.__capacity // 4):
            self.__resize(capacity=self.__capacity // 2)

        value = self.__list[self.__front]
        self.__list[self.__front] = None
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        return value

    def front(self) -> Any:
        """Gets value at front of queue

        :return: A value at the front of queue
        :rtype: Any
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__list[self.__front]

    def is_empty(self) -> bool:
        """Checks to see if queue is empty

        :return: Whether or not the queue's empty
        :rtype: bool
        """
        return self.__size == 0

    def __resize(self, capacity: int) -> None:
        """Resize queue with twice the capacity"""
        list_ = [None] * capacity
        front = self.__front

        for i in range(self.__size):
            list_[i] = self.__list[front]
            front = (front + 1) % self.__capacity

        self.__front = 0
        self.__list = list_
        self.__capacity = capacity

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        if self.is_empty():
            return 'Queue([])'
        front = self.__front
        output = 'Queue(['
        for _ in range(self.__size - 1):
            output += f'{self.__list[front]}, '
            front = (front + 1) % self.__capacity
        output += f'{self.__list[front]}])'
        return output
