#!/usr/bin/env python3
""" Create async task module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """Create a task object"""
    return asyncio.create_task(wait_random(max_delay))
