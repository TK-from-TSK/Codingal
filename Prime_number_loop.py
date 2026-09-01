lower = int(input("Enter your lower number: "))
upper = int(input("Enter your upper number: "))

print("Prime numbers from", lower, "to", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)