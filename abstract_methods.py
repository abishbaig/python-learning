from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass

# s1 = Shape("Circle") # Generates TypeError coz the class has became abstract so no object can be created of it
# Must override the abstract methods in derived classes

class Circle(Shape):
    def __init__(self,name):
        super().__init__(name)

    def area(self):
        print("Area Method Overriden")

c1 = Circle("Circle")
c1.area()

