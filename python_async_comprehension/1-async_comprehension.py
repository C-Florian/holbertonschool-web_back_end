#!/usr/bin/env python3
"""Async comprehension.

Collect 10 random floats produced by the async generator.
"""

from typing import List

# Import as attendu par les fichiers main de correction
async_generator = __import__('0-async_generator').async_generator  # type: ignore


async def async_comprehension() -> List[float]:
    """Collect 10 floats from async_generator using an async comprehension."""
    return [x async for x in async_generator()]
