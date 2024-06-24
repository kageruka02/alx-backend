#!/usr/bin/env python3
" return page range"
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "return tuple of size 2"
    return (page_size * page - page_size, page_size * page)
