from typing import Any
from dataclasses import dataclass, field
from PyDS.Error import Empty

@dataclass
class Stack:
    __list: list = field(default_factory=list)  

    def push(self, value: Any) -> None:
        self.__list.append(value)
    
    def pop(self) -> Any:
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.__list.pop()
    
    def top(self) -> Any:
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.__list[-1]

    def is_empty(self) -> bool:
        return len(self.__list) == 0
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __str__(self) -> str:
        return f'Stack({str(self.__list)})'

if __name__ == '__main__':
    s = Stack()
    for i in range(10):
        s.push(i)
    
    for i in range(10):
        s.pop()

    s.pop()


    