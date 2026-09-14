# Make several dictionaries, where the name of each dictionary is the 
# name of a pet . In each dictionary, include the kind of animal and the owner’s 
# name . Store these dictionaries in a list called pets . Next, loop through your list 
# and as you do print everything you know about each pet

poppy = {
    'kind_of_animal':'dog',
    'owners_name':'fredrick',
}
alex = {
    'kind_of_animal':'dog',
    'owners_name':'fabian',
}
mittens = {
    'kind_of_animal':'cat',
    'owners_name':'penny',
}
mr_big = {
    'kind_of_animal':'guinea pig',
    'owners_name':'hizmerk',
}
napoleon = {
    'kind_of_animal':'pig',
    'owners_name':'john',
}

pets = [poppy, alex, mittens, mr_big, napoleon]

print("These are the pets at the clinic: ")
for pet in pets:
    print(pet[0])