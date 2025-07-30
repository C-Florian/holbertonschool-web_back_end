#!/usr/bin/env python3
"""Measure average runtime per coroutine for wait_n."""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay) and
    return the average time per coroutine (total_time / n).

    Args:
        n: Number of coroutines to run.
        max_delay: Maximum delay for each coroutine.

    Returns:
        The average elapsed time per coroutine as a float.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start
    return total / n
