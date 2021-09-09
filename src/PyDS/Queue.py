from typing import Any
from dataclasses import dataclass, field
from PyDS.Error import Empty


@dataclass
class Queue:
    __list: list = field(default_factory=list)

    def enqueue(self, value: Any) -> None:
        self.__list.append(value)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__list.pop(0)

    def front(self) -> Any:
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__list[0]

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def __len__(self) -> int:
        return len(self.__list)

    def __str__(self) -> str:
        return f'Queue({str(self.__list)})'

