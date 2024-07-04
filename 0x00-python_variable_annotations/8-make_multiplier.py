#!/usr/bin/env python3
""" Complex types - functions module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiply with multiplier"""
    def multiply(arg: float) -> float:
        return arg * multiplier
    return multiply
