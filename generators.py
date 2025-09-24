def myGeneratorFunc():
    for x in range(100):
        yield x

myGen = myGeneratorFunc()
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))
print(next(myGen))