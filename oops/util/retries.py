from tenacity import retry, stop_after_attempt, wait_exponential
import asyncio


@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    reraise=True,  # Ensures the original exception is raised if all retries fail
)
async def reliable_task():
    print("Trying...")
    raise ConnectionError("Transient error")


asyncio.run(reliable_task())


# retries using tenacity
