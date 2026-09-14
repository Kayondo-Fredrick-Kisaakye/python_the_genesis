#approach described earlier for generating the list squares consisted of using three or four lines of code
#a LIST COMPREHENSION allows to generate thhis same list in one line
#it combines the FOR LOOP and the creation of new elements into one line, and automatically appends each new element

squares = [value**2 for value in range(1,11)]
print(squares)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#using this syntax, begin with a descriptive name for list
#open a set of [] brackets and define the expression for the values u want t store in new list
#here, the expression is VALUE**2, wic raises the value to the second power
#then write a FOR LOOP to generate the numbers u want to feed into expression, and close [] brackets

#in this example, the FOR LOOP is for value in range(1,11), wics feeds the values 1 through 10into expression value**2
#NOTE that no colon is used at  the end of the for statement,