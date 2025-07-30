#!/usr/bin/env python3
"""This module contains a function to return a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the multiplier.

    Parameters:
    multiplier (float): The multiplier to use.

    Returns:
    Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    return lambda x: x * multiplier
