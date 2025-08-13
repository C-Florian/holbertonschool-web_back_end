#!/usr/bin/env python3
"""Simple pagination over Popular_Baby_Names.csv.

Provides a Server class with `get_page(page, page_size)` to return
a specific slice of the dataset, and includes the `index_range` helper.
"""

import csv
from typing import List, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute the start (inclusive) and end (exclusive) indices for a page.

    Args:
        page: 1-based page number (must be >= 1).
        page_size: number of items per page (must be >= 1).

    Returns:
        A tuple (start, end) suitable for slicing a list: data[start:end].
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: Optional[List[List]] = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset (header row removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # drop header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the page slice of the dataset.

        Validates inputs, computes the slice via `index_range`, and returns
        an empty list if the slice is out of range.

        Args:
            page: 1-based page number (>= 1).
            page_size: number of items per page (>= 1).

        Returns:
            A list of rows representing the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
