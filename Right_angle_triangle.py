print("Half Pyramid Pattern Of Stars (*)")

n = int(input(" Enter the number of rows: "))
 
for i in range(n):

    for k in range(i + 1):
        print("*", end = "")

    print()