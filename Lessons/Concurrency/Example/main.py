import asyncio


async def very_slow_operation():
    await asyncio.sleep(5)
    print("Hello, async!")


async def function():
    await asyncio.gather(very_slow_operation(), very_slow_operation(), very_slow_operation(), very_slow_operation())
    print("Hello, my friends!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(function())
