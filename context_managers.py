# class SimpleContext:
#     def __enter__(self):
#         print("Entering context")
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")

# with SimpleContext():
#     print("Inside the block")

from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Setup")
    yield
    print("Cleanup")

with managed_resource():
    print("Doing something")
