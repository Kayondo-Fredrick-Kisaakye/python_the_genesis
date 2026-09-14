church_and_goer = {
    'fredrick':'wh naalya',
    'peshency':'wh jogo',
    'belinda':'wh kabubbu',
    'samchi':'wh naalya'
}

print("The following churches were mentioned:\n")
for church in sorted(church_and_goer.values()):
    print(church.title())
# This approach pulls all the values from the dictionary without checking
# for repeats. That might work fine with a small number of values, but in a
# poll with a large number of respondents, this would result in a very repeti
# tive list. To see each language chosen without repetition, we can use a set.
# A set is similar to a list except that each item in the set must be unique:

# When you wrap set() around a list that contains duplicate items, Python
# identifies the unique items in the list and builds a set from those items. At u
# we use set() to pull out the unique languages in favorite_languages.values().
# The result is a nonrepetitive list of languages that have been mentioned
# by people taking the poll:
# """for language in set(favorite_languages.values()):"""

print("The following churches were mentioned:(no repeat)")
for church in set(church_and_goer.values()):
    print(church.title())

# The following churches were mentioned:
#
# Wh Jogo
# Wh Kabubbu
# Wh Naalya
# Wh Naalya
# The following churches were mentioned:(no repeat)
# Wh Kabubbu
# Wh Naalya
# Wh Jogo