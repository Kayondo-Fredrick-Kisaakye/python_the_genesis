# Sometimes you’ll want to store a set of dictionaries in a list or a list of 
# items as a value in a dictionary. This is called nesting. You can nest a set 
# of dictionaries inside a list, a list of items inside a dictionary, or even a 
# dictionary inside another dictionary. Nesting is a powerful feature, as the 
# following examples will demonstrate

# A List of Dictionaries
# The alien_0 dictionary contains a variety of information about one alien, 
# but it has no room to store information about a second alien, much less a 
# screen full of aliens. How can you manage a fleet of aliens? One way is to 
# make a list of aliens in which each alien is a dictionary of information about 
# that alien. For example, the following code builds a list of three aliens:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)