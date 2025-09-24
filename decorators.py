# # Example : Simple Example of Decorators
# def greetUser(func):
#     def greet(time,name):
#         func(name)
#         print(f"Good {time}")
#     return greet

# @greetUser
# def turnOn(name):
#     print(f"Welcome Sir, {name}")

# # With Arbitaray Keyword Arguments
# def signIn(func):
#     def credentials(**kwargs):
#         if(kwargs["email"] == "abish" and kwargs["password"] == "123"):
#             func()
#         else:
#             print("Failed to SignIn")
#     return credentials

# @signIn
# def openApp():
#     print("Welcome to Our App")
#     turnOn("Morning","Abish")



# # Example : args & kwargs
# def timer_wrapper(func):
#     """A wrapper function to time the execution of another function."""
#     import time
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds.")
#         return result
#     return wrapper

# @timer_wrapper
# def calculate_sum(n):
#     """Calculates the sum of numbers up to n."""
#     total = 0
#     for i in range(n + 1):
#         total += i
#     return total

# Example: Passing Arguments in Decorator Itself
# def changecase(n):
#   def changecase(func):
#     def myinner():
#       if n == 1:
#         a = func().lower()
#       else:
#         a = func().upper()
#       return a
#     return myinner
#   return changecase

# @changecase(1)
# def myfunction():
#   return "Hello Linus"

# Example: Many Decorators - Order Wise Execution
# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# def addgreeting(func):
#   def myinner():
#     return "Hello " + func() + " Have a good day!"
#   return myinner

# @changecase
# @addgreeting
# def myfunction():
#   return "Tobias"

# Example: Preserving Metadata of Original Functions
import functools

def changecase(func):
  @functools.wraps(func) # Without this the original func is now reference to this inner() func
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"



def main():
    # Without Syntactic Sugar @ keyword
    #  # greetUser will take an function as an argument : name only, and will return an wrapper function object
    # func = greetUser(turnOn)
    # # This will be associated with greet function and as our outer argument function is calling inside it so here we will pass the argument
    # func("Morning","Abish")

# ---------------------------------------------------------------------
    # With @ keyword == without logic but more readability
    # turnOn = greetUser(turnOn)
    # turnOn(time,name)

    # openApp(email="abish",password="123")
    

    # When calculate_sum is called, it's actually the 'wrapper' function that runs,
    # which then calls the original calculate_sum and adds timing functionality.
    # result = calculate_sum(1000000)
    # print(f"Sum: {result}")

    print(myfunction.__name__)

    




# Dunder Method that defines that if the program is run directly the first thing to execute is below this if statement in whole program
if __name__=="__main__":
    main()