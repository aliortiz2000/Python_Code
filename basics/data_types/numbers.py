"""
Numbers
    There are three numeric types in Python:
        int
        float
        complex
        
    Int
        Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    
    Float
        Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
        
    Complex
        Complex numbers are written with a "j" as the imaginary part:
"""
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))




"""
Random Number
    Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers.
    Import the random module, and display a random number between 1 and 9:
"""
import random

print(random.randrange(1, 10))