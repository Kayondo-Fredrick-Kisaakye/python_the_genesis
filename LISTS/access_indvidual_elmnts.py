#LISTS are ordered collections, so you can access any element by telling PY the position, or INDEX
#to access, write te name of the list then the index of the item enclosed in square brackets

benz = ['G', 'GLS', 'GLE', 'GLC', 'GLA', 'GLB']
print(benz[2])  #OUTPUT - GLE

#u can also use the string methods from (intro) on any element in the list
#EG-: u can make "GLE" become "gle"

print(benz[2].lower()) #OUTPUT - gle

#INDEX positions start at 0 not 1
#this how things work on the lower level...using this counting system, u can get any element by
# subtracting ONE from its position in the list...EG-:
#to access the FOURTH, you request the THIRD
print(benz[0])  #G
print(benz[1])  #GLS

#u'll want to get last items nga tomanyi how big the list is
#this convention extends to otheer negative indexes
#INDEX -2 returns SECOND ITEM FROM THE END, -3 THIRD FROM THE END etc