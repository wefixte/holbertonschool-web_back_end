#!/usr/bin/env python3
""" Returns a list of typles """

from typing import List
from typing import Iterable
from typing import Tuple
from typing import Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples
    Args:
       lst: inputt iterable of sequences
    """
    return [(i, len(i)) for i in lst]
