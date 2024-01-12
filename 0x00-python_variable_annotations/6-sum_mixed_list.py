#!/usr/bin/env python3
''' function takes a list of integers and floats
and returns their sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum with float"""
    return float(sum(mxd_lst))
