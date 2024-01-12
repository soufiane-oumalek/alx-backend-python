#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:
."""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return list or else None """
    if lst:
        return lst[0]
    else:
        return None
