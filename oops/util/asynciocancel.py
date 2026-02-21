import asyncio


# async def fn2Cancel():
#     import asyncio

#     try:
#         print("Entering func to cancel")
#         asyncio.sleep(2)
#     except asyncio.CancelledError:
#         print("op cancelled")
#     finally:
#         print("exiting")


# async def main():
#     task = asyncio.create_task(fn2Cancel())
#     asyncio.sleep(1)
#     print("main routine cancelling task")
#     task.cancel()

#     try:
#         await task
#     except asyncio.CancelledError:
#         print("task cancelled")
#     finally:
#         print("exiting main")


# asyncio.run(main())


async def fnA():
    await asyncio.sleep(2)
    raise ValueError("Task has failed")


async def fnB():
    try:
        await asyncio.sleep(2)
    except asyncio.CancelledError:
        print("op cancelled because fnA threw failed")


async def mainTask():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fnA())
            tg.create_task(fnB())
    except ExceptionGroup as eg:
        print("mainTask cancelled error")
    finally:
        print("ending main task")


asyncio.run(mainTask())
