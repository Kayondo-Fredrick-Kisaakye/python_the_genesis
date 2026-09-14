#sometimes its important to check whether a list contains certain value before taking an action
#EG-: you might want to check whether a new username already exists in a list of current usernames before completing
#someones registration on a website, in a mapping project, you might want to check whether a submitted location already exists
#in a list of known locations

#to find out whether a particular value already in a list, use the key word IN ,
#lets consider some code you might write for a pizzeria, we'll make a list of toppings a customer wants for a pizza and then
#check whether certain toppings are in the list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mashrooms' in requested_toppings:
    print("true")
else:
    print("not true")