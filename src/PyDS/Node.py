from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    """Implementation of Node containing a value
       and pointing to the next node.
    """
    value: Any
    next: Optional[Node]


@dataclass
class DoublyNode(Node):
    prev: Optional[Node]
