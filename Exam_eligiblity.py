medical_cause = input("Do you have a medical cause? Y/N").strip().upper()

if medical_cause == "Y":
    print("You are allowed..")

else:
    attendance = int(input("Enter your attendance: "))

    if attendance >= 75:
        print("You are allowed..")
    else:
        print("Sorry, try again next time...")