"""A module for depth-first (in-order) traversal of trees."""

from inspect import stack
from typing import Iterable
from tree import T


def in_order(t: T | None) -> Iterable[int]:
    """In-order traversal of a tree.

    >>> tree = T(2, T(1, None, None), T(4, T(3, None, None), T(5, None, None)))
    >>> list(in_order(tree))
    [1, 2, 3, 4, 5]
    """
    s = []
    order = []
    while(True):
        if t:
            s.append(t)
            t = t.left
        elif s:
            t = s.pop()
            order.append(t.val)
            t = t.right
        else:
            break
    return order

