# Without Property Decorator
# class Student:
#     def __init__(self,programming,ds):
#         self.programming = programming
#         self.ds = ds
    
#     def score(self):
#         print(self.programming+self.ds)

# s1 = Student(10,10)
# s1.score()
        
# ---------------------------------------------------------
# With Property Decorator
class Student:
    def __init__(self,programming,ds):
        self.programming = programming
        self.ds = ds
    
    @property
    def score(self):
        return self.programming+self.ds

s1 = Student(10,10)
print(s1.score) # Acting as an Attribute   