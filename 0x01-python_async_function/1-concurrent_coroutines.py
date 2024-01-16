#!/usr/bin/env python3
"""import Module"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function doc"""
    list_time = []
    for _ in range(n):
        list_time .append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*list_time))
