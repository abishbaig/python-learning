import asyncio
import time

async def fetchData(delay,id):
    print("Fetching Data from Server....")
    await asyncio.sleep(delay)
    print("Data Fetched")
    return {"Data: ",id}

async def main():
    print("Main Courotine Started")
    startTime = time.time()

    # -------------------------------------------------
    # Using Only Coroutines to handle async funcs but still don't execute parallely means the other task will not start after the 1st one is completed
    # task1 = fetchData(2,1)
    # task2 = fetchData(5,1)

    # result1 = await task1
    # print(result1)
    # result2 = await task2
    # print(result2)
    # -------------------------------------------------


    # -------------------------------------------------
    # Using Tasks to create and run multiple coroutines parallel in a sense that if one is waiting for some I/O the other gets executed in the event loop
    # task1 = asyncio.create_task(fetchData(5,1))
    # task2 = asyncio.create_task(fetchData(3,2))
    
    # result1 = await task1
    # result2 = await task2

    # print(result1)
    # print(result2)
    # -------------------------------------------------
    
    
    # -------------------------------------------------
    # Same thing done auto using gather() function, but gather() is bad at error handling as you can't cancel any coroutine yourself or if any coroutine fails the other might be affected too
    # task1 = asyncio.create_task(fetchData(5,1))
    # task2 = asyncio.create_task(fetchData(3,2))
    
    # results = await asyncio.gather(task1,task2)

    # for res in results:
    #     print(res)
    # -------------------------------------------------

    # -------------------------------------------------
    # Efficient way for creating tasks using taskgroup: Asynchronous context manager for managing groups of tasks
    # Can handle Exceptions and terminate all tasks while prompting wrong outputs
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i,sleep_duration in enumerate([2,1,3],start=1):
            task = tg.create_task(fetchData(sleep_duration,i))
            tasks.append(task)
    
    results = [tsk.result() for tsk in tasks]
    for x in results:
        print(x)
        
    # -------------------------------------------------


    endTime = time.time()

    print("Execution Time: ",endTime-startTime)
    print("Main Courotine Ended")


if __name__ == "__main__":
    asyncio.run(main())