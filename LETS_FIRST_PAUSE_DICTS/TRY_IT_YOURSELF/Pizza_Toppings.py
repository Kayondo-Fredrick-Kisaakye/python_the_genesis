# Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value . As they enter each topping, 
# print a message saying you’ll add that topping to their pizza 

prompt = "\nWelcome, enter the toppings you want on your pizza: "
prompt += "\nEnter 'quit' to end request process: "

user_input = ""
while user_input != 'quit':
    user_input = input(prompt)
    
    if user_input != 'quit':
        print("i'll add " + user_input.title() + " to your pizza")

"""
Welcome, enter the toppings you want on your pizza: 
Enter 'quit' to end request process: mushrooms
i'll add Mushrooms to your pizza

Welcome, enter the toppings you want on your pizza: 
Enter 'quit' to end request process: zest
i'll add Zest to your pizza

Welcome, enter the toppings you want on your pizza: 
Enter 'quit' to end request process: petrol
i'll add Petrol to your pizza

Welcome, enter the toppings you want on your pizza: 
Enter 'quit' to end request process: quit
"""
