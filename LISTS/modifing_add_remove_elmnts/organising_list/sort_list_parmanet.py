#often, my lists will be created in an unpredictable order
#because i cant always control the order in which my users provide data
#although this is unavoidable most times, i'll frequently want to present my information in a particular order
#sometimes i'll want to preserve the original order
#PY provides a number of different ways to change my lists, depending on situation

#PY's SORT() METHOD makes it relatively easy to sort a list
#imagine i have a list of chics and want to change and store them alphabetically
#to keep it simple, i'll assume that all values are in lowercase

chics = ['barbra', 'annet', 'tiffany', 'shirat']
print(chics)   #['barbra', 'annet', 'tiffany', 'shirat']

chics.sort()
print(chics)   #['annet', 'barbra', 'shirat', 'tiffany']

#the SORT() METHOD changes the order parmanently
#the chics are now in alphabetical order, and we can never revert them to original order

#>>>you can also sort this list in reverse-alphabetical order by passing the arguement REVERESE=True to the sort() metod
#EG-:

boys = ['andrew', 'erick', 'titus', 'ssema', 'boris']
boys.sort()
print(boys)   #['andrew', 'boris', 'erick', 'ssema', 'titus']

boys.sort(reverse=True)
print(boys)   #['titus', 'ssema', 'erick', 'boris', 'andrew']