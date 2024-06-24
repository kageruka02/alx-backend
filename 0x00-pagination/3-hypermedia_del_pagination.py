#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Union, Dict


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
            truncated_dataset = dataset[:1000]
            length = len(dataset)
            self.__indexed_dataset = {i: dataset[i] for i in range(length)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Args:
            index (int): starting index of the page
            page_size (int): number of items per page
        Returns:
            A dictionary with the following key-value pairs:
                * index: the current start index of the return page
                * next_index: the next index to query with
                * page_size: the current page size
                * data: the actual page of the dataset
        """
        dataDictionary = self.indexed_dataset()
        assert index <= len(dataDictionary)
        count = 0
        current_index = index
        short_list = []
        while count < page_size and current_index < len(dataDictionary):
            if current_index in dataDictionary:
                count += 1
                short_list.append(dataDictionary[current_index])
            current_index += 1
        while True:
            if dataDictionary[current_index] is None and current_index < len(
                dataDictionary
            ):
                current_index += 1
            else:
                break
        length = len(dataDictionary)
        next_index = current_index if current_index < length else None
        return {
            "index": index,
            "data": short_list,
            "page_size": page_size,
            "next_index": next_index,
        }
