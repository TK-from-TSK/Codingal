PI = 3.14159

def circumference_from_radius():
    radius = float(input("Enter the radius: "))
    return 2 * PI * radius

def circumference_from_diameter():
    diameter = float(input("Enter the diameter: "))
    return PI * diameter

if __name__ == "__main__":
    choice = input("Enter 'r' to use radius or 'd' to use diameter: ").lower()
    
    if choice == 'r':
        result = circumference_from_radius()
        print(f"The circumference is: {round(result, 2)}")
    elif choice == 'd':
        result = circumference_from_diameter()
        print(f"The circumference is: {round(result, 2)}")
    else:
        print("Invalid choice! Please enter 'r' or 'd'.")
