# //pyodbc, aioodbc, aiohttp
# asyncio functionality, coroutines, Threadpoolexecutor,

import asyncio
from concurrent.futures import ThreadPoolExecutor,as_completed



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

async def get_status_async(session, url: str):
    

    async with session.get(url) as resp:
        return  url,resp.status


async def usingAsyncIO():
    import aiohttp

    urls = ["https://google.com", "https://python.org", "https://github.com"]

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(get_status_async(session,url)) for url in urls]

            for done in asyncio.as_completed(tasks):
                url, status = await done
                print('completed:', url, status)

asyncio.run(usingAsyncIO())

def get_status(url: str):
    import requests

    response = requests.get(url)
    return response.status_code



# ThreadPoolExecutor is mostly required when the thread is going to make a blocking call (event loop).
# This would avoid blocking the event loop

# InterpreterPoolExecuter will be useful for CPU intensive work - when nogil is enabled
#  every thread will get its own gil and memory thereby really enabling CPU bound tasks

# In threadpoolexecutor scenario multiple threads always share the same gil - so same limitation

# when we are using libraries - like aiohttp which supports asyncio calls threadpoolexecutor not required
# and we can use asyncio

def usingThreadPoolExecuter():

    urls = ["https://google.com", "https://python.org", "https://github.com"]

    with ThreadPoolExecutor() as executor: 
        results = executor.map(get_status, urls)

    print(list(results))

def usingThreadPoolExecuterSubmit():

    urls = ["https://google.com", "https://python.org", "https://github.com"]

    with ThreadPoolExecutor() as executor: 
        futures = [executor.submit(get_status, url) for url in urls]

    for future in as_completed(futures): # pyright: ignore[reportArgumentType]
        print(future.result())
  


# usingThreadPoolExecuter()
# usingThreadPoolExecuterSubmit()