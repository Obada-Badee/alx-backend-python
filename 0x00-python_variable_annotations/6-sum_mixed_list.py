#!/usr/bin/env python3
""" Complex types - mixed list module """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Type-annotated function returns their sum as a float. """
    fsum: float = 0
    for num in mxd_lst:
        fsum += float(num)
    return fsum
