#!/usr/bin/env python3
"""Run multiple tasks using task_wait_random and collect their delays."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the given max_delay and return the
    delays in ascending completion order (without explicitly calling sort()).

    Args:
        n: Number of tasks to spawn.
        max_delay: Maximum delay for each task.

    Returns:
        A list of float delays in ascending completion order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)
    return delays
