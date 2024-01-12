#!/usr/bin/env python3
'''function takes a float returns a function that multiplies a float
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
