import asyncio


async def teatime():
    await asyncio.sleep(1)
    print('take a cup of tea')
    await asyncio.sleep(1)


async def read():
    print('Reading for 1 hour...', end='')
    await teatime()
    print('...reading for 1 hour')


asyncio.run(read())