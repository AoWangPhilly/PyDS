from typing import Any
from dataclasses import dataclass, field
from PyDS.Error import Empty


@dataclass
class Stack:
    """Implementation of Stack ADT

    :param __list: A container that holds elements in stack
    :type __list: list[Any]
    """
    __list: list[Any] = field(default_factory=list)

    def push(self, value: Any) -> None:
        """Inserts value to the top of stack

        :param value: A value to insert
        :type value: Any
        """
        self.__list.append(value)

    def pop(self) -> Any:
        """Deletes value from top of stack

        :return: A value from the top of the list
        :rtype: Any
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.__list.pop()

    def top(self) -> Any:
        """Grab top value of stack without deletion

        :return: A value from the top of the list
        :rtype: Any
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.__list[-1]

    def is_empty(self) -> bool:
        """Checks to see if stack is empty

        :return: Whether or not the stack's empty
        :rtype: bool
        """
        return len(self.__list) == 0

    def __len__(self) -> int:
        return len(self.__list)

    def __str__(self) -> str:
        return f'Stack({str(self.__list)})'
