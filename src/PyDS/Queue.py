from typing import Any
from dataclasses import dataclass, field
from PyDS.Error import Empty


@dataclass
class Queue:
    """Implementation of Queue ADT"""
    __list: list = field(default_factory=list)

    def enqueue(self, value: Any) -> None:
        """Insertion to the tail of the queue

        :param value: The value inserting to the tail
        :type value: Any
        """
        self.__list.append(value)

    def dequeue(self) -> Any:
        """Deletion at the front of the queue

        :return: A value at the front of queue
        :rtype: Any
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__list.pop(0)

    def front(self) -> Any:
        """Gets value at front of queue

        :return: A value at the front of queue
        :rtype: Any
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__list[0]

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def __len__(self) -> int:
        return len(self.__list)

    def __str__(self) -> str:
        return f'Queue({str(self.__list)})'

