# Simple Example
import multiprocessing
import time

# def squares():
#     print("Calculating Squares....")
#     for i in range(10):
#         time.sleep(1)
#         print(f"Square of {i}: {i**2}")


# Example to Share Data between Processes using IPC Array & Variable
# def squares(numbers,array,v):
#     for idx,n in enumerate(numbers):
#         array[idx] = n**n
#         v.value = n

# Multiprocessing Queue Example 
# def squares(numbers,q):
#     for n in numbers:
#        q.put(n**n)

# def cubes():
#     print("Calculating Cubes....")
#     for i in range(10):
#         time.sleep(1)
#         print(f"Cube of {i}: {i**3}")


# Multiprocssing Locks
def depositMoney(balance,lock):
    for _ in range(100):
        time.sleep(0.01)
        # Critical Section
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()
        # print(balance.value)
    
def withdrawMoney(balance,lock):
    for _ in range(100):
        time.sleep(0.01)
        # Critical Section
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()
        # print(balance.value)
    

def main():
    start = time.time()

    # numbers = [1,2,3]

    # array = multiprocessing.Array('i',3)
    # value = multiprocessing.Value('i',0)    

    # que = multiprocessing.Queue()
    # task1 = multiprocessing.Process(target=squares,args=(numbers,que))
    # # task2 = multiprocessing.Process(target=cubes)

    balance = multiprocessing.Value('d',100)
    lock = multiprocessing.Lock()
    task1 = multiprocessing.Process(target=depositMoney,args=(balance,lock))
    task2 = multiprocessing.Process(target=withdrawMoney,args=(balance,lock))

    task1.start()
    task2.start()

    task1.join()
    task2.join()

    # # Printing Values of multiprocessing queue
    # while que.empty() is False:
    #     print(que.get())

    # print(f"Result Array: {array[:]}")
    # print(f"Result Value: {value.value}")

    print(f"Balance: {balance.value}")

    end = time.time()
    print(f"Execution Time: {end-start}")

if __name__=="__main__":
    main()