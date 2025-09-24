import asyncio

semaphore = asyncio.Semaphore(2)

async def worker(name):
    print(f"{name} waiting to acquire semaphore")
    async with semaphore:
        print(f"{name} acquired semaphore")
        await asyncio.sleep(2)
        print(f"{name} releasing semaphore")

async def main():
    await asyncio.gather(worker("A"), worker("B"), worker("C"), worker("D"))

asyncio.run(main())
