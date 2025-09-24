# class Person:
#     def __init__(self):
#         self.name = None
#         self.age = None
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def printPerson(self):
#         print(f"Name: {self.name}\nAge: {self.age}")
        

# class Student(Person):
#     def __init__(self,name,age,id):
#         super().__init__(name,age)
#         self.id = id

# s1 = Student("Abish",22,126)
# print(s1.printPerson())

# ------------------------------------------------------------
# Single Inheritance
# class Person:
#     age = 22
#     def __new__(cls):
#         print("Person Created")
#         return super().__new__(cls)
    
#     def __init__(self):
#         print("Person Instantiated")
#         self.name = "Abish"
#         print(self)

#     def hello(self):
#         print("Hello")


# class Student(Person):
#     def __new__(cls):
#         print("Student Created")
#         return super().__new__(cls)
#     def __init__(self):
#         # super().__init__()
#         print("Student Instantiated")

# s1 = Student()
# s1.hello()



# ------------------------------------------------------------
# # Multiple Inheritance
# class Car:
#     def __new__(cls):
#         print("Car")
#         return super().__new__(cls)


# class Toyota:
#     def __new__(cls):
#         print("Toyota")
#         return super().__new__(cls)


# class Mehran(Car,Toyota):
#     def __new__(cls):
#         print("Mehran")
#         return super().__new__(cls)

#     def __init__(self):
#         print("Mehran Instance")

# m1 = Mehran()
# print(Mehran.__mro__)


# ------------------------------------------------------------
# Dict of Class Attributes
class Person:
    name = "Abish"
    def __init__(self):
        self.name = "Abish"
    
    def hello(self):
        print(self.name)
    
class Student(Person):
    def __init__(self):
        # super().__init__()
        self.id = 126

    def name(self):
        print(self.id)

s1 = Student()
# print(Student.__dict__)
print(s1.__dict__)
