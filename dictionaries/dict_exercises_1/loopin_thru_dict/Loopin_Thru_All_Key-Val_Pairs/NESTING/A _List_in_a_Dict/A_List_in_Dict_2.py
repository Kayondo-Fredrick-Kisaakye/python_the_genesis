# You can nest a list inside a dictionary any time you want more than 
# one value to be associated with a single key in a dictionary. In the earlier 
# example of favorite programming languages, if we were to store each 
# person’s responses in a list, people could choose more than one favorite 
# language. When we loop through the dictionary, the value associated with 
# each person would be a list of languages rather than a single language. 
# Inside the dictionary’s for loop, we use another for loop to run through 
# the list of languages associated with each person:

favourite_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())
        
"""
Jen's favourite languages are:
        Python
        Ruby

Sarah's favourite languages are:
        C

Edward's favourite languages are:
        Ruby
        Go

Phil's favourite languages are:
        Python
        Haskell
"""
#You should not nest lists and dictionaries too deeply. If you’re nesting items much 
# deeper than what you see in the preceding examples or you’re working with someone 
# else’s code with significant levels of nesting, most likely a simpler way to solve the 
# problem exists.