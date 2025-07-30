#!/usr/bin/env python3
"""This module contains a function to sum a list of floats."""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums all the elements in a list of floats.

    Parameters:
    input_list (List[float]): A list of floats to sum.

    Returns:
    float: The sum of the floats in the list.
    """
    return sum(input_list)
