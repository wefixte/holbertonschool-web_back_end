#!/usr/bin/env python3
""" Asynchronous coroutine that takes in an integer argument """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes in an integer argument
        wait for a random delay between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
