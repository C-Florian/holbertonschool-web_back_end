#!/usr/bin/env python3
"""Basic async syntax: wait for a random delay and return it."""

from __future__ import annotations

import asyncio
import random
from typing import Final


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.

    Args:
        max_delay: The maximum number of seconds to wait (inclusive).

    Returns:
        The actual delay time (float) that was awaited.
    """
    # random.uniform is inclusive on both ends
    delay: Final[float] = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
