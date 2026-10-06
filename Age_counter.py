try:
    age = int(input("Please enter your age: "))
    if age % 2 == 0:
        print("This is an even age.")
    else:
        print("This is an odd age.")

    if age < 18:
        print("You are a minor.")
    elif age > 18:
        print("You are an adult.")
except ValueError:
    print("This isn't a valid output.")
finally:
    print("Thank you for using the age counter.")