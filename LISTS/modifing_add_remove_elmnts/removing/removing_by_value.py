#sometimes you may not know the position of the value you want to remove
#if you only know the value of the item you want to remove, you can use REMOVE() METHOD

heroes = ['nelson mandela', 'gadafi', 'jomo kenyatta', 'yoweri']
print(heroes)

heroes.remove('yoweri')
print(heroes)

#here, the REMOVE() METHOD tells Python to figure out where 'yoweri' is and remove him
#OUTPUT:-
"""
['nelson mandela', 'gadafi', 'jomo kenyatta', 'yoweri']
['nelson mandela', 'gadafi', 'jomo kenyatta']
"""


#you can also use REMOVE() to work with a value that's being removed from a list
#lets remove DOOM and print a reason for removing him
heroes_promax = ['thanos', 'silver surfer', 'gen zod', 'dr doom']   #after defining the list
print(heroes_promax)

lethal_guy = 'dr doom'  #we asign the value 'dr doom' to lethal_guy
heroes_promax.remove(lethal_guy)  #we noe use variable to tell PY wic value  to remove
print(heroes_promax)             #dr doom has been removed
print(f"\n {lethal_guy.title()}, just wants control, maybe")  #but still accessible through variable lethal_guy

#OUTPUT:-
"""
['thanos', 'silver surfer', 'gen zod', 'dr doom']
['thanos', 'silver surfer', 'gen zod']

 Dr Doom, just wants control, maybe
"""

#the remove() method deletes the first occurrence of the value u specify
#if there's a possibility the value appears more than once in the list, u'll neeed to use a loop to make sure
#--that all occurrences of the value are removed