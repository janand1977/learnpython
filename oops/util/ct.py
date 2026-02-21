# //pyodbc, aioodbc, aiohttp
# asyncio functionality, coroutines, Threadpoolexecutor,

import asyncio
from concurrent.futures import ThreadPoolExecutor


async def fn1(num: int):
    print(f"This is fn1:{num}")
    return num + 1


async def fn2(num: int):
    print(f"This is fn2:{num}")
    return num + 1


async def main():

    c1 = fn1(5)
    c2 = fn2(2)

    result = await asyncio.gather(c1, c2)
    print(result[0])
    print(result[1])


# asyncio.run(main())

# def get_status():


# def usingThreadPoolExecuter():

#     urls = ["https://google.com", "https://python.org", "https://github.com"]

#     with ThreadPoolExecutor as executor:
#         executor.
