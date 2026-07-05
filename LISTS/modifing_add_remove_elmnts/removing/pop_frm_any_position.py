#u can use pop() to remove an item from any position in a list by including the INDEX of the item you want to remove in  the parentheses
chics = ['vicky', 'ephrance', 'esther', 'betty']
young_chic = chics.pop(2)

print(f"the youngest is {young_chic.title()}")

#remember that each time u use POP(), the item u work with is nolonger stored in the list
#>>> if you're unsure to use DEL STATEMENT or POP() METHOD, here's a simple way to decide-:
#    When you want to delete an item from a list and not use it anyway, use DEL STATEMENT
#    If you  want  to use an item as you remove it, use the POP() METHOD
