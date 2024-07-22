#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of the dataset in a deletion-resilient manner.

        Args:
            index (int): The start index of the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary with pagination metadata.
        """
        indexed_data = self.indexed_dataset()
        total_data = len(indexed_data)
        assert isinstance(index, int) and 0 <= index < total_data

        data = []
        next_index = index
        for i in range(page_size):
            while next_index not in indexed_data:
                next_index += 1
            data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
