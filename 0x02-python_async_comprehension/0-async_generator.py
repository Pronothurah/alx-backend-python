#!/usr/bin/env python3
"""Task 0 Module"""
import asyncio
import random


async def async_generator():
    """coroutine which loops 10 times,"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
