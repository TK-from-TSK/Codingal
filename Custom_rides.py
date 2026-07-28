print("Select your ride: ")
print("1. 2 wheeler")
print("2. 4 wheeler")


choice = int( input("Enter your choice: ") )


if( choice == 1 ): 
  print( "what type of bike? " )
  print("1.Motorbike")
  print("2.Scooter")

  
  choice2=int(input("Enter you choice: "))
  if choice2==1: 
    print("You have selected motorbike")
  else:
    print("You have selected scooter")


elif( choice == 2 ): 
  print( "what type of car?" )
  print("1.Lamborghini")
  print("2.Ferrari")
  choice3=int(input("enter your choice: "))

  if choice3==1: 
    print("You have selected Lamborghini")
  else:
    print("You have selected Ferrari")

else: 
  print("Enter the options given above only")