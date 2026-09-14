# Now you can access either the color or the point value of alien_0. If a 
# player shoots down this alien, you can look up how many points they should 
# earn using code like this:

alien_0 = {
    'color':'green',
    'points':5,
}

new_points =  alien_0['points']
print("You just earned " + str(new_points) + " points")

# Once the dictionary has been defined, the code at 10 pulls the value 
# associated with the key 'points' from the dictionary. This value is then 
# stored in the variable new_points. The line at 11 converts this integer value 
# to a string and prints a statement about how many points the player just earned: