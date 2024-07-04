#!/usr/bin/env python3
"""  Let's duck type an iterable object  module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a sequence along with its length"""
    return [(i, len(i)) for i in lst]
