#!/usr/bin/env python3
"""This module contains a function to get the floor of a float number."""

import math

def floor(n: float) -> int:
    """
    Returns the floor (largest integer less than or equal to) of a float.

    Parameters:
    n (float): The float to round down.

    Returns:
    int: The floor of the input float.
    """
    return math.floor(n)
