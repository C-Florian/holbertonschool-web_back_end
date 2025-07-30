#!/usr/bin/env python3
"""Measure runtime of four parallel async comprehensions."""

from typing import Final
import asyncio
import time

# Import as attendu par les fichiers main de correction
async_comprehension = __import__('1-async_comprehension').async_comprehension  # type: ignore


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel, return elapsed seconds."""
    start: Final[float] = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: Final[float] = time.perf_counter()
    return end - start
