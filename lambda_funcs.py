def power(exponent):
    return lambda num: num ** exponent

square = power(2)

print(square(4))
print(square(2))


# Example: 2
power_gen = lambda num,exponent: num**exponent
print(power_gen(2,2))