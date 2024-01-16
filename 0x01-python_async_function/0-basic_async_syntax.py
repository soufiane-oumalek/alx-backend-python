#!/usr/bin/env python3
'''import random and asyncio.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''function  doc'''
    time_w = random.random() * max_delay
    await asyncio.sleep(time_w)
    return time_w
