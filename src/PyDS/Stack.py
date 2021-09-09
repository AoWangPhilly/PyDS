from typing import Any


class Stack:
    def __init__(self) -> None:
        self.__list = []
    
    def push(self, value: Any) -> None:
        self.__list.append(value)
    
    def pop(self) -> Any:
        return self.__list.pop()
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __str__(self) -> str:
        return str(self.__list)

if __name__ == '__main__':
    s = Stack()

    