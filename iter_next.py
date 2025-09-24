myTuple = (1,2,3)
myIter = iter(myTuple)

try:
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
except StopIteration as e:
    print("Tuple Bounds Exceeded")

# --------------------------------------
# Making Our Class an Iterable Object
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# for x in myiter:
#   print(x)