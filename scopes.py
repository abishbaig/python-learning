# # Function with Global Var: Function must be called first to use its global vars
# def func():
#     global x
#     x = 300

# func()

# print(x)

# Accessing Global Var in Local Function
# x = 300
# def func():
#     global x
#     # x = 100
#     return x

# print(func())

# Nested Functions and Non-Local Vars
def func1():
    x = 100
    def func2():
        nonlocal x
        x = 200
        return x
    print(func2())
    return x

print(func1())