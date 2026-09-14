# A more realistic example would involve more than three aliens with 
# code that automatically generates each alien. In the following example we 
# use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
    
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))