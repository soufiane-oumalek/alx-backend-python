#!/usr/bin/env python3
''' function takes a string and an int OR float
 returns a tuple.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return str k and float v"""
    return (k, float(v**2))
