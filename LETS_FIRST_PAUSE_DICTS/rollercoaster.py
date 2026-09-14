height = input("How tall are you: ")
height = int(height)

if height >=36:
    print("\nYou are tall enough to ride!")
else:
    print("Please go and grow more height to ride!")
    
"""
The program can compare height to 36 because height = int(height) 
converts the input value to a numerical representation before the compari
son is made. If the number entered is greater than or equal to 36, we tell 
the user that they’re tall enough:
"""
