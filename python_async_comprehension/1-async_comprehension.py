#!/usr/bin/env python3
""" Coroutine that will collect 10 random numbers
using an async comprehensing"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Coroutine that will collect 10 random numbers """
    return [i async for i in async_generator()]
