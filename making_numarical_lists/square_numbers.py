#u can almost create any set of numbers with range()
#EG-: consider how u ight make a list of the first 10 square numbers
#(that is, the square of each integer from 1 through 10)
#in PY, two ASTERISKS(**) represent EXPONENTS

squares = []    #we start with EMPTY LIST called SQUARES
for value in range(1,11):  #tell PYTHON to loop through each value from 1 to 10 using RANGE()
    square = value ** 2  #in loop, current value is raised to second power, assigned to variable SQUARE
    squares.append(square)   #each new value of square is then appended to the list SQUARES
print(squares)            #finally, its printed--[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#to make this code mo concisely, omit the temporary var square and append each new value directly to the list
squares2 = []
for value in range(1,11):
     squares2.append(value**2)
print(squares2)