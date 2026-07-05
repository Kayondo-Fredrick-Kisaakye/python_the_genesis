#to maintain the original order of list but present it in a sorted order
#you can use the SORTED() FUNCTION, it lets you display your list in a particular order but doesnt affect actual one

cars = ['bmw', 'audi', 'toyota', 'subaru']

print(" here is the order of the list")
print(cars)   #['bmw', 'audi', 'toyota', 'subaru']-- first printed original order

print("\n here is the sorted order of the list")
print(sorted(cars))   #['audi', 'bmw', 'subaru', 'toyota']-- then printed alphabetical order

print(" \nhere is the original order again")
print(cars)   #['bmw', 'audi', 'toyota', 'subaru']-- then we print in original order to prove

#the SORTED() FUNCTION also accepts REVERSE=TRUE if you need in reverse-alphabetical order


#NOTE:- sorting a list alphabetically is abit complex wen all values are not in lowercase
       #there are several ways to interpret capital letters when determining a sort order
       #and specifing the exact order can be more complex than we want to deal with at this time
       #however, most approaches to sorting will build dirrectly on what i learned in this section
