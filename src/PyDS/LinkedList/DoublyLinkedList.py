from __future__ import annotations

from dataclasses import dataclass
from PyDS.Error import Empty
from typing import Any


@dataclass
class Node:
    value: Any
    next: Node
    prev: Node


@dataclass
class DoublyLinkedList:
    head: Node
    tail: Node

    def prepend(self, value: Any) -> None:
        ...

    def append(self, value: Any) -> None:
        ...

    def search(self, target: Any) -> int:
        ...
    
    def remove_front(self):
        ...

    def remove_end(self):
        ...

    def remove(self):
        ...

    def __len__(self) -> int:
        ...

    def __str__(self) -> str:
        ...
