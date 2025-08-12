#!/usr/bin/env python3
"""Hypermedia pagination module.

Extends the simple pagination Server class with a method `get_hyper`
that returns both the page data and useful navigation metadata.
"""
import math
from typing import Dict, Any
from 1-simple_pagination import Server as SimpleServer

class Server(SimpleServer):
    """Server class with hypermedia pagination."""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dictionary with page data and hypermedia metadata.

        Args:
            page: Page number (1-indexed).
            page_size: Number of items per page.

        Returns:
            A dictionary containing:
                - page_size: length of returned data
                - page: current page number
                - data: list of dataset rows for the page
                - next_page: next page number or None
                - prev_page: previous page number or None
                - total_pages: total number of pages in dataset
        """

        data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

