import asyncio

lock = asyncio.Lock()

async def worker(num):
    print(f"Worker {num} waiting for lock")
    async with lock:
        print(f"Worker {num} acquired the lock")
        await asyncio.sleep(1)
        print(f"Worker {num} released the lock")

async def main():
    await asyncio.gather(worker(1), worker(2))

asyncio.run(main())
