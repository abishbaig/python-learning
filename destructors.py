class Person:
    def __init__(self):
        print("Person Created")
    def __enter__(self):
        print("Entered Block")
    def __del__(self):
        print("Person Destroyed")
    def __exit__(self,exc_type,exc_value,traceback):
        print("Exited Block")

with Person():
    print("Inside Block")
