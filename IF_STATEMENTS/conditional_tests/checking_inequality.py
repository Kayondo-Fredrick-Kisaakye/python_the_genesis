#wen you want to determine whether two values are not equal, u can use the INEQUALITY OPERATOR(!=)
#lets use another if statement to examine how to use the inequality operator
#we'll store a requested pizza topping in a variable and then print a message if the person did not order anchovies

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#this code compares the value of requested_topping to the value 'anchovies'
#if they do not match, python returns TRUE and executes code following if statement
#if they match, python returns FALSE and does not execute code below if statement

#most of conditional expresions i write will test for equality, but sometimes you''l find it more efficient to test inrquality
