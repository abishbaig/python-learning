class Person:
    def __new__(cls,*args,**kwargs):
        print("Person Class Object Is Created")
        return super().__new__(cls)

    def __init__(self):
        print("Person Class Object Is Instantiated")
        self.name = None
        self.age = None
    
    def setName(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    
    def info(self):
        print("Name : ",self.name)
        print("Age  : ",self.age)
    
    # Just like Overriding << operator in C++ 
    def __str__(self):
        return f"{self.name}, {self.age}"
    
p1 = Person()
p1.setName("Abish")
p1.setAge(22)
p1.info()
print(p1)