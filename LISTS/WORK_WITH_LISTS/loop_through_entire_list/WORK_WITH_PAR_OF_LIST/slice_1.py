#you can woek with specificgroup of items in a list, called a SLICE in Python

#SLICING A LIST
#to make a SLICE, u specify the index of the first and last elements u want to work with
#As with the range() function, python stops one item before the second index u specify
#to output the first three elements in a list, u wud request indicies 0 to 3, which wud return elements 0,1,2

players = ['fred', 'wade', 'dave', 'tedd']
print(players[0:3])    #['fred', 'wade', 'dave']
print(players[1:3])    #['wade', 'dave']

#u omit the fisrt index in the slice, python auto starts at the beginning of list
print(players[:3])     #['fred', 'wade', 'dave']

#similar syntax works if you want a slice that includes the end of a list, like if u want items starting frpm the third
#to the last, you start with index 2 and omit lhe second index
print(players[2:])    #['dave', 'tedd']

#Recall that a negative index returns an element a certain distance from the end of a list, EG-:
#if i want to output the last three players on the list, we can use the slice:
#players[-3:]
print(players[-3:])    #['wade', 'dave', 'tedd']