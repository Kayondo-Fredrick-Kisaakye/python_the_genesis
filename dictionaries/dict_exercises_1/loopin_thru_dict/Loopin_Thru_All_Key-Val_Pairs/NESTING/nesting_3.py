# These aliens all have the same characteristics, but Python considers each 
# one a separate object, which allows us to modify each alien individually.
# How might you work with a set of aliens like this? Imagine that one 
# aspect of a game has some aliens changing color and moving faster as the 
# game progresses. When it’s time to change colors, we can use a for loop and 
# an if statement to change the color of aliens. For example, to change the 
# first three aliens to yellow, medium-speed aliens worth 10 points each, we 
# could do this:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(0,30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
# Show the first 5 aliens:
for alien in aliens[0:10]:
    print(alien)
print("...")


# It’s common to store a number of dictionaries in a list when each dic
# tionary contains many kinds of information about one object. For example, 
# you might create a dictionary for each user on a website, as we did in user.py 
# on page 103, and store the individual dictionaries in a list called users. All 
# of the dictionaries in the list should have an identical structure so you can 
# loop through the list and work with each dictionary object in the same way