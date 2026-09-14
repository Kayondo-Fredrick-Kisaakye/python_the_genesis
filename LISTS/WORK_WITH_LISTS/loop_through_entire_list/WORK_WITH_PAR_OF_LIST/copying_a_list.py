#often u'll want to start with an existing list and make an entirely new list based on first one
#to copy a list, u can make a slice that includes the entire original list by omiting the first index and second
#([:])...this tells python to make a slice that starts at the first item and ends with the last item,
#producing a copy of the entire list

my_foods = ['pizza', 'burger', 'hotdog', 'meatball']    #we make a list called my_foods
friend_foods = my_foods[:]                              #we make a new one called friend_foods
#we make a copy of my_foods by asking for a slice of my_foods without specifiying any indices
#and asssign the copy to friend_foods

print("My favourite foods  are:")
print(my_foods)

print("\nMy friend's favouritte foods are:")
print(friend_foods)
#we print each list, we see that they both contain same foods

#to prove we actually have 2 separate lists, well add a new food to each list and show that each list keeps track ofthe appropriate persons fav foods
my_foods.append('eggroll')
friend_foods.append('sausage')
print(my_foods)
print(friend_foods)

"""
['pizza', 'burger', 'hotdog', 'meatball', 'eggroll']
['pizza', 'burger', 'hotdog', 'meatball', 'sausage']
"""