import asyncio


async def q():
    print("Hello")
    await asyncio.sleep(3)


async def a():
    print("World")


async def main():
    await asyncio.gather(q(), a())


asyncio.run(main())
