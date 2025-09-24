ages = [5, 12, 17, 18, 24, 32]

# Filter the array, and return a new array with only the values equal to or above 18:
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# # Adults will only contain items that are filtered through the myFunc : True
# adults = filter(myFunc, ages)

# for x in adults:
#   print(x)


# Mapping an Function to each item of the iterable
# def square(x):
#   return x**2

# double_ages = map(square,ages)
# for x in double_ages:
#   print(x)

# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
for y in x:
    print(y)