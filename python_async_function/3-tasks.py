#!/usr/bin/env python3
"""Create asyncio.Task wrappers around wait_random."""

from __future__ import annotations

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay: The maximum delay to pass to wait_random.

    Returns:
        An asyncio.Task that is scheduled immediately.
    """
    return asyncio.create_task(wait_random(max_delay))
