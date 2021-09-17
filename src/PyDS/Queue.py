from typing import Any, List
from dataclasses import dataclass, field
from PyDS.Error import Empty


@dataclass
class Queue:
    """Implementation of Queue ADT

    :param __list: A container that holds elements in queue
    :type __list: list[Any]
    """
    __capacity: int = 64
    __list: List[Any] = field(default_factory=lambda: [None] * Queue.__capacity)
    __front: int = 0
    __end: int = 0
    __size: int = 0

    def enqueue(self, value: Any) -> None:
        """Insertion to the tail of the queue

        :param value: The value inserting to the tail
        :type value: Any
        """
        if self.__size == self.__capacity:
            self.__resize()
        self.__end %= self.__capacity
        self.__list[self.__end] = value
        self.__size += 1
        self.__end += 1

    def dequeue(self) -> Any:
        """Deletion at the front of the queue

        :return: A value at the front of queue
        :rtype: Any
        """
        if self.is_empty():
            raise Empty("Queue is empty")
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

    def __resize(self) -> None:
        list_ = [None] * 2 * self.__capacity
        front = self.__front

        for i in range(self.__size):
            list_[i] = self.__list[front]
            front = (front + 1) % self.__capacity

        self.__front = 0
        self.__list = list_
        self.__capacity *= 2

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        if self.is_empty():
            return 'Queue([])'
        front = self.__front
        output = 'Queue(['
        while front != self.__end - 1:
            output += f'{self.__list[front]}, '
            front = (front + 1) % self.__capacity
        output += f'{self.__list[front]}])'
        return output


if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    for i in range(10):
        q.dequeue()
    for i in range(9):
        q.enqueue(i)
    print(q)
