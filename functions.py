# *args returns a tuple of arguments
def my_function(*args):
  print("The youngest child is " + args[2])

my_function("Emil", "Tobias", "Linus")

# **kwargs returns a dictionary of keyword arguments
def my_function(**kwargs):
  print("His last name is " + kwargs["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Positonal ONLY Arguments : Before (, /)
# Keyword ONLY Arguments : After (* ,)
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)