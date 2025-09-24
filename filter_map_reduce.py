from functools import reduce

list1 = [1,2,3,4,5,6]

print(list(filter(lambda x: x>3,list1)))

print(list(map(lambda x: x**2, list1)))

print(reduce(lambda x, y: x+y,list1))