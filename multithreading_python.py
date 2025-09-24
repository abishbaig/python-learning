import threading
import time

def squares():
    print("Calculating Squares....")
    for i in range(10):
        time.sleep(1)
        print(f"Square of {i}: {i**2}")

def cubes():
    print("Calculating Cubes....")
    for i in range(10):
        time.sleep(1)
        print(f"Cube of {i}: {i**2}")

def main():
    start = time.time()
    
    task1 = threading.Thread(target=squares)
    task2 = threading.Thread(target=cubes)

    task1.start()
    task2.start()

    task1.join()
    task2.join()

    end = time.time()
    print(f"Execution Time: {end-start}")

main()