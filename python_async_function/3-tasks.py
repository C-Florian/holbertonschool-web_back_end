#!/usr/bin/env python3
"""Create asyncio.Task wrappers around wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    The task is scheduled on the current running event loop and must be
    awaited by the caller from within an async context.

    Args:
        max_delay: Maximum delay to pass to wait_random.

    Returns:
        An asyncio.Task scheduled immediately.
    """
    return asyncio.create_task(wait_random(max_delay))
