
h = int(input("Enter the base number: "))
p = int(input("Enter the exponent: "))


result = 1


for i in range(p):
    result = result * h 


print(f"{h} raised to the power of {p} is: {result}")
