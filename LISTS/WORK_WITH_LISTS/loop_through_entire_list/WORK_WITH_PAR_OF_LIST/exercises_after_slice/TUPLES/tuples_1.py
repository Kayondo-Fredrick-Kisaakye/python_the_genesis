#lists work well for sorting collections of items that can change throughout the life of a program
#the ability to modify lists is particularly important wen u're working with a list of users on a website
#or a list of characters in a game

#however, sometimes you'll want to create a list of items that cannot change.
#TUPLES allow you to do just that. PYTHON refers to values that cannot change as IMMUTABLE and immutable list is TUPLE

#DEFINING A TUPLE
#A tuple looks just like a list, except you use PARENTHESES instead of square brackets, once you define a tuple
#you can access individual elements by using item's index, just as you would for a list

#EG-:  if we have a rectangle that shud always be a certain size, we can ensure that its size doesnt change by putting
#the dimensions into a tuple:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#lets see if we try to change one of the items in tuple

#dimensions2 = (100, 25)
#dimensions2[0] = 150

"""Traceback (most recent call last):
  File "C:tuples_1.py", line 22, in <module>
    dimensions2[0] = 150
TypeError: 'tuple' object does not support item assignment
"""

#tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable.
#if you want to define a uple with one element, u need to include a trailing comma