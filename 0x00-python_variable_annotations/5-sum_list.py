#!/usr/bin/env python3
""" Complex types - list of floats module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ a type-annotated function returns a float"""
    fsum: float = 0
    for num in input_list:
        fsum += num
    return fsum
