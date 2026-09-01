decimal_number = float(input("Enter a positive decimal number: "))

if decimal_number == 0:
    print("Binary: 0")
else:
    number = decimal_number
    remainders = []

    # The outside loop finds each binary digit.
    while number > 0:
        quotient = 0
        remainder = number

        
        while remainder >= 2:
            remainder = remainder - 2
            quotient = quotient + 1

        remainders.append(remainder)
        number = quotient

    
    binary_number = ""
    position = len(remainders) - 1

    while position >= 0:
        binary_number = binary_number + str(remainders[position])
        position = position - 1

    print("Binary:", binary_number)