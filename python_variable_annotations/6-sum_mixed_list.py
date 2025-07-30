#!/usr/bin/env python3
"""This module contains a function to sum a mixed list of integers and floats."""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all the elements in a mixed list (integers and floats).

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)
