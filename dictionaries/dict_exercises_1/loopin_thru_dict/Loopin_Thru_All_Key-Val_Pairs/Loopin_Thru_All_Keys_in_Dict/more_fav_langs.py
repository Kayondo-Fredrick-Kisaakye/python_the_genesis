# The keys() method is useful when you don’t need to work with all the
# values in a dictionary. Let’s loop through the favorite_languages dictionary
# and print the names of everyone who took the poll

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())