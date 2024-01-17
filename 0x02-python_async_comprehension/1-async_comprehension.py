#!/usr/bin/env python3
""" import modules """
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Function documantation"""
    return [key async for key in async_generator()]
