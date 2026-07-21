original_cost = float(input("Enter the actual cost: "))
Sales_cost = float(input("Enter the cost for your product: "))

if Sales_cost > original_cost:
        print("You made a profit of", Sales_cost - original_cost)
else:
    print("You incurred a loss of", original_cost - Sales_cost)