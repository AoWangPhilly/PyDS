from typing import Any, List
from dataclasses import dataclass, field
from PyDS.Error import Empty


@dataclass
class Stack:
    """Implementation of Stack ADT

    :param __capacity: The maximum number of elements a container can hold
    :type __capacity: int
    :param __list: A container that holds elements in stack
    :type __list: List[Any]
    :param __size: The number of elements in stack
    :type __size: int
    """

    __capacity: int = 64
    __list: List[Any] = field(default_factory=lambda: [None] * Stack.__capacity)
    __size: int = 0

    def push(self, value: Any) -> None:
        """Inserts value to the top of stack

        :param value: A value to insert
        :type value: Any
        """
        if self.__size == self.__capacity:
            self.__resize()
        self.__list[self.__size] = value
        self.__size += 1

    def pop(self) -> Any:
        """Deletes value from top of stack

        :return: A value from the top of the list
        :rtype: Any
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        self.__size -= 1
        value = self.__list[self.__size]
        self.__list[self.__size] = None
        return value

    def top(self) -> Any:
        """Grab top value of stack without deletion

        :return: A value from the top of the list
        :rtype: Any
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.__list[self.__size - 1]

    def is_empty(self) -> bool:
        """Checks to see if stack is empty

        :return: Whether or not the stack's empty
        :rtype: bool
        """
        return self.__size == 0

    def __resize(self) -> None:
        """Resizes stack when list reaches capacity
        """
        self.__capacity *= 2
        list_ = self.__capacity * [None]
        for index in range(self.__size):
            list_[index] = self.__list[index]
        self.__list = list_

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        return f'Stack({self.__list[:self.__size]})'
