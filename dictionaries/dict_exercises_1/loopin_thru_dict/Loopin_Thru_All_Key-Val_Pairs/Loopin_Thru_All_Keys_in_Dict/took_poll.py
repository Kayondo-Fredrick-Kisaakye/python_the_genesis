# You can also use the keys() method to find out if a particular person
# was polled. This time, let’s find out if Erin took the poll:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin did not take the poll")