from typing import Any
from dataclasses import dataclass, field

@dataclass
class Stack:
    __list: list = field(default_factory=list)  

    def push(self, value: Any) -> None:
        self.__list.append(value)
    
    def pop(self) -> Any:
        return self.__list.pop()
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __str__(self) -> str:
        return f'Stack({str(self.__list)})'

if __name__ == '__main__':
    s = Stack()
    for i in range(10):
        s.push(i)

    print(s)


    