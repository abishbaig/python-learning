# Example 1: try ... except block
# print(0/0) # -> Throws Error

# try:
#     print(0/0)
# except ZeroDivisionError:
#     print("Infinity Occured")
# finally:
#     print("Block Finished")

# --------------------------------------------------
# Example 2: Handling NameError -> Variable is Undefined
# try:
#     print(x)
# except NameError:
#     print("?")

# --------------------------------------------------
# Example 3: Raising our Own Exceptions
# try:
#     x = 5
#     if x < 6:
#         raise Exception("x is < 6")
# except Exception as e:
#     print(e)
# print(x)

# --------------------------------------------------
# Example 4: Use of AssertionErrors while in debug/development mode
# try:
#     x = 10
#     assert(x<6), "x is > 6"
# except AssertionError as e:
#     print(e)
# print(x)


x = 5
if x < 6:
    raise Exception("x is < 6")
print(x)