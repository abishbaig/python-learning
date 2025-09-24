# Runtime Polymorphism: Method Overriding

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

# Compile Time Polymorphism: Method Overloading
class Order:
    def __init__(self,price):
        self.price = price
    
    def __gt__(self,obj):
        return self.price > obj.price
    

    
o1 = Order(10)
o2 = Order(20)

print(o1>o2)