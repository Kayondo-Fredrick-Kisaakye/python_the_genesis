#sometimes u'll want to use the value of an item after removing it
#EG-: u might want to get the X and Y position of an alien that was just shot down so u can draw explosion
#>>>> in a web app, you mmight remove a user from active users and add them to inactive users

#the POP() METHOD ">>REMOVES THE LAST ITEM IN A LIST"<<, but let's u work with that item after removing it
#the POP comes from thinking of a list as a STACK of items and popping one item off the top of the stack
#in this analogy, the the top of the stack corresponds to the END OF THE LIST
#>>> lets pop a chicfrom a list of chics

chics = ['betty', 'ursula', 'gwen', 'jane', 'mitchelle'] #we start by define list of chics
print(chics)                                             #we print the  list  of chics

popped_chic = chics.pop()   #then we pop the value from  the list and assign it to variable POPPED__CHIC
print(chics)                #we print the list
print(popped_chic)          #to prove we still have access to removed value

#OUTPUT
"""
['betty', 'ursula', 'gwen', 'jane', 'mitchelle']
['betty', 'ursula', 'gwen', 'jane']
mitchelle
"""