prompt = "Enter a number and i'll tell you whether it is even or odd."
prompt += "\nEnter number: "

number = int(input(prompt))

if number % 2 == 0:
    print("\n The number " + str(number)  + " is even.")
else:
    print("\nThe numbeer " + str(number) + " odd.")
    
"""Even numbers are always divisible by two, so if the modulo of a number 
and two is zero (here, if number % 2 == 0) the number is even. Otherwise, 
it’s odd.
"""
