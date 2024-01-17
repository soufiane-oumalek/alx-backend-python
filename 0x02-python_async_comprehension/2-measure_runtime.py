#!/usr/bin/env python3
""" import modules """
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function documantation"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - start
