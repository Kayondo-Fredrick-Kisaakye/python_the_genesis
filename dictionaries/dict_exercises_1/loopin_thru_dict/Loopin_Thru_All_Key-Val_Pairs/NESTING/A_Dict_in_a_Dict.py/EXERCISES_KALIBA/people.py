# Start with the program you wrote for Exercise 6-1 (page 102) . 
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people . Loop through your list of people . As you 
# loop through the list, print everything you know about each person

crush_one = {
    'first_name':'nakawooya',
    'second_name':'shantel',
    'user_age':22,
    'crush_city':'masaka',
}
crush_two = {
    'first_name':'mutoni',
    'second_name':'nelly',
    'user_age':21,
    'crush_city':'ssembabule',
}
crush_three = {
    'first_name':'gihozo',
    'second_name':'vanessa',
    'user_age':23,
    'crush_city':'bombo',
}

crushes= [crush_one, crush_two, crush_three]

print("These were my crushes: ")
for crush in crushes:
    print("\t" + crush['first_name'].title() + " " + crush['second_name'].title())
    
print("This is where i met them: ")
for crush in crushes:
    print("\t" + crush['first_name'].title() + " is from" + " " + crush['crush_city'].title())
    
print("This was their age: ")
for crush in crushes:
    print("\t" + crush['first_name'].title() + " " + crush['second_name'].title() + " is " + str(crush['user_age']))

# print("The total of their ages is: "+ int(crush_one['user_age']+crush_two['user_age']+crush_three['user_age']))

