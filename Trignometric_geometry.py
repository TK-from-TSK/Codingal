import math

angle = float(input("Enter an angle in degrees: "))

# Convert degrees to radians
radians = math.radians(angle)

# Calculate trigonometric values
print("sin(", angle, ") =", math.sin(radians))
print("cos(", angle, ") =", math.cos(radians))

if math.cos(radians) == 0:
    print("tan(", angle, ") is undefined.")
else:
    print("tan(", angle, ") =", math.tan(radians))