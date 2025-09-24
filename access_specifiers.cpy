# Only a Conceptual Implementation - Still Accessible Using Name Mangling
class Person:
    def __init__(self):
        self.__name = "Hello" # Private Method
        self._age = 21 # Protected Method
    
p1 = Person()
# print(p1.__name) # Throws Attribute Error
print(p1._Person__name) # Accessible Using name mangle