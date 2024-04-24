#!/usr/bin/env python3
""" Returns a tuple with a string and a float"""

from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple with a string and a float
    Args:
        k: key of the tuple - string
        v: value of the tuple - int or float
    """
    return (k, v * v)
