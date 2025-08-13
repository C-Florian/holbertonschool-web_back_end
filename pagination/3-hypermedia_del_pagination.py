#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]  #  respecter la troncature
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient page starting from `index`.

        Returns:
          {
            "index": index (start requested),
            "next_index": first index after the returned page,
            "page_size": number of items actually returned,
            "data": list of rows
          }
        """
        #  signature exacte exigée par le checker (index: int = None)
        assert isinstance(page_size, int) and page_size > 0
        if index is None:
            index = 0
        assert isinstance(index, int) and index >= 0

        idx_map = self.indexed_dataset()
        #  borne de validité basée sur la vue indexée (0..len(idx_map)-1)
        assert index < len(idx_map)

        data: List[List] = []
        cursor = index

        # collecter jusqu'à page_size éléments existants,
        # en sautant les clés absentes si des suppressions surviennent
        while len(data) < page_size and cursor < len(idx_map) or len(data) < page_size:
            if cursor in idx_map:
                data.append(idx_map[cursor])
            # si on dépasse la plus grande clé, on s'arrête
            if not idx_map:
                break
            # on continue à avancer tant qu'on peut récupérer des éléments
            cursor += 1
            # optimisation d'arrêt : si on a passé toutes les clés possibles
            if cursor > max(idx_map.keys()):
                break

        return {
            "index": index,
            "next_index": cursor,
            "page_size": len(data),
            "data": data,
        }
