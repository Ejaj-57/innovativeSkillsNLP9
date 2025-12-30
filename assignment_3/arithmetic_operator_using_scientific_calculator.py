# Power, Roots, Exponential
import math

a = 5
b = 2

print(a ** b)          
print(math.sqrt(a))      
print(a ** (1/3))        
print(math.exp(a))       


# Logarithmic Operations

import math

x = 10

print(math.log(x))       
print(math.log10(x))     
print(math.log(x, 2))    

# Trigonometric Functions

import math

angle_deg = 30
angle_rad = math.radians(angle_deg)

print(math.sin(angle_rad))
print(math.cos(angle_rad))
print(math.tan(angle_rad))

# Inverse Trigonometric
x = 0.5

print(math.degrees(math.asin(x)))
print(math.degrees(math.acos(x)))
print(math.degrees(math.atan(x)))

# Factorial
import math

n = 5
print(math.factorial(n))

# Absolute Value & Rounding
x = -7.89

print(abs(x))        # Absolute
print(round(x, 1))   # Rounded
print(math.floor(x)) # Floor
print(math.ceil(x))  # Ceiling

# Modulus, Remainder & Sign

a = -10
b = 3

print(a % b)               
print(math.remainder(a,b)) 

# Percentage

value = 45
total = 200

percentage = (value / total) * 100
print(percentage)


# Permutation & Combination

import math

n = 5
r = 2

print(math.perm(n, r))  # nPr
print(math.comb(n, r))  # nCr

# Exponential & Scientific Notation

import math

x = 12345

mantissa, exponent = math.frexp(x)
print(mantissa, exponent)


# Degree–Radian Conversion


import math

print(math.radians(180))
print(math.degrees(math.pi))


# Hyperbolic Functions

import math

x = 1

print(math.sinh(x))
print(math.cosh(x))
print(math.tanh(x))


# Square & Reciprocal

x = 4

print(x ** 2)     # x²
print(1 / x)      # 1/x



