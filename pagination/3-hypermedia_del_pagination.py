#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

Implements a Server that exposes a deletion-resilient pagination method.
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset: List[List] = None
        self.__indexed_dataset: Dict[int, List] = None

    def dataset(self) -> List[List]:
        """Cached dataset (header removed)."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by original position (sparse map).

        Keys are original 0-based positions. If rows are deleted later,
        their keys are simply missing (not re-numbered).
        """
        if self.__indexed_dataset is None:
            data = self.dataset()
            # Index *tout* le dataset (pas seulement un tronçon)
            self.__indexed_dataset = {i: data[i] for i in range(len(data))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Return a deletion-resilient page starting from `index`.

        Args:
            index: 0-based starting index in the original dataset.
            page_size: number of items to return.

        Returns:
            {
              "index": index (start requested),
              "next_index": first index after the returned page,
              "page_size": number of items actually returned,
              "data": page rows (list of lists)
            }

        Raises:
            AssertionError if arguments are invalid or out of range.
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        idx = self.indexed_dataset()
        # borne haute = plus grand index existant (après suppressions)
        max_key = max(idx.keys()) if idx else -1
        # index doit être dans [0, max_key + 1)
        assert index <= max_key

        data: List[List] = []
        cursor = index

        # On balaye vers l'avant et on collecte les entrées EXISTANTES
        # (celles dont la clé est encore présente)
        while len(data) < page_size and cursor <= max_key:
            if cursor in idx:
                data.append(idx[cursor])
            cursor += 1

        # cursor pointe sur le 1er index *après* le dernier élément retourné
        next_index = cursor
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }

