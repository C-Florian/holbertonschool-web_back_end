#!/usr/bin/env python3
"""Pagination helper module.

This module provides a single helper function `index_range` that
calculates the start and end indices for pagination.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end index for pagination.

    Given a 1-based page number and a page size, return the zero-based
    start index (inclusive) and end index (exclusive) to slice a list.

    Args:
        page: The current page number (1-indexed, >= 1).
        page_size: The number of items per page (>= 1).

    Returns:
        A tuple (start_index, end_index) suitable for slicing a list.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return start_index, end_index

