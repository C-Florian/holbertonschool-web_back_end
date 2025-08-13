#!/usr/bin/env python3
"""Hypermedia pagination over Popular_Baby_Names.csv.

This module replicates the simple pagination from task 1 and adds
`get_hyper`, which returns both page data and navigation metadata.
"""

import csv
import math
from typing import Any, Dict, List, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute the start (inclusive) and end (exclusive) indices for a page.

    Args:
        page: 1-based page number (>= 1).
        page_size: number of items per page (>= 1).

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
                data = [row for row in reader]
            self.__dataset = data[1:]  # drop header
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dict with page data and hypermedia metadata.

        The returned structure contains:
          - page_size: length of returned data
          - page: current page number
          - data: list of rows for the current page
          - next_page: next page number or None
          - prev_page: previous page number or None
          - total_pages: total number of pages in the dataset

        Args:
            page: 1-based page number (>= 1).
            page_size: number of items per page (>= 1).

        Returns:
            A dictionary with page content and navigation metadata.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
