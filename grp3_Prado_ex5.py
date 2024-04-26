import math

# Number functions

x = 17
y = 15 
remainder = math.remainder(x,y)
print(f"The remainder of {x,y} is {remainder}")

# Power and logarithmic functions

x = 3
y = 2 
power = math.pow(x,y)
print(f"{x} to the power of {y} is equal to {power}")

# Trigonometric functions

angle_rad = math.radians(45)
sin_value = math.sin(angle_rad)
print("Sine of", angle_rad, "radian is:", sin_value)

# Angular Conversion functions 

angle_deg = 90
angle_rad = math.radians(angle_deg)
print(angle_deg, "degrees in radians is:", angle_rad)

# Hyperbolic functions
num = 2
cosh_value = math.cosh(num)
print("Hyperbolic cosine of", num, "is:", cosh_value)