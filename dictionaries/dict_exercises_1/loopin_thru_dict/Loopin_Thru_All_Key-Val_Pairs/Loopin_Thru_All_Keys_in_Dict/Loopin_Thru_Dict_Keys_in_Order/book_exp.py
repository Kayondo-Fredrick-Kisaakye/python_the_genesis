# A dictionary always maintains a clear connection between each key and
# its associated value, but you never get the items from a dictionary in any
# predictable order. That’s not a problem, because you’ll usually just want
# to obtain the correct value associated with each key.
# One way to return items in a certain order is to sort the keys as they’re
# returned in the for loop. You can use the sorted() function to get a copy of
# the keys in order:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + "Thanks for feedback!")

# This for statement is like other for statements except that we’ve wrapped
# the sorted() function around the dictionary.keys() method. This tells Python
# to list all keys in the dictionary and sort that list before looping through it.
# The output shows everyone who took the poll with the names displayed in
# order: ALPHABETICAL

"""
EdwardThanks for feedback!
JenThanks for feedback!
PhilThanks for feedback!
SarahThanks for feedback!
"""