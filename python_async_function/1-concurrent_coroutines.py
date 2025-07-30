#!/usr/bin/env python3
"""Run multiple coroutines concurrently and return their delays in order."""

from __future__ import annotations

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the given max_delay and return the delays
    in ascending order, without calling sort() explicitly.

    Args:
        n: Number of coroutines to spawn.
        max_delay: Maximum delay for each wait_random call.

    Returns:
        A list of float delays in ascending completion order (thus ascending).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []

    # As tasks complete, their results tend to arrive in increasing delay order.
    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    # Because asyncio.as_completed yields in completion order, and smaller
    # delays complete first, 'delays' is ascending without calling sort().
    return delays
