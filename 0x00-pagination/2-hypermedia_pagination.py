#!/usr/bin/env python3
"""
Adds `get_hyper` method to `Server` class
"""
import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "return tuple of size 2"
    return (page_size * page - page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "get_page to be printed"
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        length = len(self.dataset())
        data = self.dataset()
        if start > length or end > length:
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """
        Args:
            page (int): page number
            page_size (int): number of items per page
        Returns:
            A dictionary of the following:
                * page_size, page, data, next_page, prev_page, total_pages
        """
        content_of_pages = self.get_page(page, page_size)
        totalLines = len(self.dataset())
        dictionary = {
            "page_size": page_size,
            "page": page,
            "data": content_of_pages,
            "next_page": (
                None
                if content_of_pages == [] or page >= totalLines
                else page + 1
            ),
            "prev_page": None if page == 1 else page - 1,
            "total_pages": math.ceil(totalLines/page_size)

        }
        return dictionary
