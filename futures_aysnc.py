import asyncio
from asyncio import Future

async def set_future_result(fut):
    await asyncio.sleep(1)
    fut.set_result('Result is ready!')

# Futures are implemented on lower level and async and await are already preimplemented by it
# Future is an promise of the result it will provide us in the future after awaitining of the task
async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    asyncio.create_task(set_future_result(fut))
    print("Waiting for future result...")
    result = await fut
    print(result)

asyncio.run(main())
