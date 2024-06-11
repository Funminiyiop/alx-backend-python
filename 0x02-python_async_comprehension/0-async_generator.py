#!/usr/bin/env python3
"""
An asynchronous generator function that loop 10 times, 
each time asynchronously wait 1 second, then 
yield a random number between 0 and 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This asynchronous function iterate 10 times, 
    wait 1 second and yield a random number between 0 and 10.

    Returns:
        Generator: object usable in a await instance.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
