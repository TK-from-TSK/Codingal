string = input("Enter your name:  ")

string2 = ""

for i in string:
    string2 = i + string2
print("Original name:", string)

print("Reversed name:", string2)