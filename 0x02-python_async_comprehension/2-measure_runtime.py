#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time


ascomp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that should measure the total runtime and return it."""
    s = time.perf_counter()
    await asyncio.gather(ascomp(), ascomp(), ascomp(), ascomp())
    elapsed = time.perf_counter() - s
    return elapsed
