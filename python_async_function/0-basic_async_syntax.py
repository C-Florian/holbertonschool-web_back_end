#!/usr/bin/env python3
"""Basic async syntax: wait for a random delay and return it."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.

    Args:
        max_delay: The maximum number of seconds to wait (inclusive).

    Returns:
        The actual delay time (float) that was awaited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
