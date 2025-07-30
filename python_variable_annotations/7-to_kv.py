#!/usr/bin/env python3
"""This module contains a function to return a tuple with a string and the square of a number."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string and the second element is the square of v.

    Parameters:
    k (str): The string key.
    v (Union[int, float]): The number to square.

    Returns:
    Tuple[str, float]: A tuple with the string and the square of v.
    """
    return (k, float(v ** 2))
