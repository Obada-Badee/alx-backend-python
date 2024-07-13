#!/usr/bin/env python3
""" A module alters wait_n into task_wait_n"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """  will spawn wait_random n times with the specified max_delay. """
    r = await asyncio.gather(*(task_wait_random(max_delay) for i in range(n)))
    return sorted(r)
