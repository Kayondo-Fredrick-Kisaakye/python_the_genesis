#u can use a slice in a for loop if you want to loop through a subset of the elements in list
#in the next example, we can loop through the first three players and print their nmaes as part of a rooster
players = ['tedd', 'nedd', 'dave', 'kent', 'jake']

print("HERE ARE THE FIRST THREE PLAYERS ON MY TEAM")
for player in players[:3]:
    print(player.title())

#slices are useful in a number of situations, wen you're creating a game, you could add a player's final score to a list every
#time that the player finishes playing...you could then get a players top three scores by sorting the list in decreasing
#order and takin a slice that includes just the first three scores...

#wen working with data, u can use slices to process your data in chunks of a specific size
#or, wen building a web app, u cud use slices to display info in a series of pages with an appropriate amount of information on each page
