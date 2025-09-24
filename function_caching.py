from functools import lru_cache
import time

@lru_cache(maxsize=None)
def printNum(x):
    time.sleep(3)
    print(x+2)


printNum(1)
printNum(2)
printNum(3)

# These will not be printed as they are already available in the cache memory 
# So the function will return them from their instead of recalculating them
printNum(1)
printNum(2)
printNum(3)