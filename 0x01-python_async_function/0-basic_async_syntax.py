#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
async def main():
    delay = await wait_random()
    print(f"The random delay is: {delay} seconds")

# Create an event loop and run the main coroutine
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
