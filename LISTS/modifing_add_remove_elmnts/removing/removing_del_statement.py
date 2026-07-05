#often you'll want to remove an item or a set of items from a list
#EG-: when a player shoots an alien, u most likely want to remove it from the list of active aliens
#>>>> or when a user decides to cancel their account on a web application you made
#>>>> you'll want to remove that user from active users
#>>>> you can remove an item according to it's POSITION in the list or according to VALUE

snacks = ['chips', 'chinchin', 'popcorns', 'grenades']
print(snacks)   #['chips', 'chinchin', 'popcorns', 'grenades']

del snacks[3]
print(snacks)   #['chips', 'chinchin', 'popcorns']

#here i've used del statement to remove 'grenades'
#YOU CAN REMOVE item from any position using del statement if you know INDEX
del snacks[0]
print(snacks)   #['chinchin', 'popcorns']

#here: - you can NOLONGER access the value that was removed from the list after the DEL STATEMENT is used