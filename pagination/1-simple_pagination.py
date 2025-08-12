#!/usr/bin/env python3
"""Simple pagination module.

Contains the Server class for paginating `Popular_Baby_Names.csv`
with a method `get_page` to retrieve specific pages.
"""

import csv
from typing import List
from 0-simple_helper_function import index_range

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # remove header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a specific page from the dataset.

        Args:
            page: Page number (1-indexed).
            page_size: Number of items per page.

        Returns:
            A list of rows for the requested page.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]

