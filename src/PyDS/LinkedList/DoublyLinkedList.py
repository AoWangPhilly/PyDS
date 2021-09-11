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

