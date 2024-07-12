#!/usr/bin/env python3
""" an asynchronous coroutine that takes in an integer argument
    seconds and eventually returns it."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Returns a random wait """
    time_delayed = random.uniform(0, max_delay)
    await asyncio.sleep(time_delayed)
    return time_delayed
