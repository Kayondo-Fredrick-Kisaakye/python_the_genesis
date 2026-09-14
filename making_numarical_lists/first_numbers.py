#many resons to  store a set of numbers exist,  EG-:> youll need to keep track of position each character in game
#and you might want to keep track of a players high scores as wee
#in data visualization u'll almost always work with sets of numbers,
#such as temperature, distance, population sizes or longitude or latitude values

#lists are ideal for storing sets of numbers, and PY provides a  variety of tools to help work with lists o numbers
#using RANGE() FUNCTION
#it makes it easy to generate a series of numbers, forexample here

for value in range(1,5):
    print(value)

#OUTPUT:
"""
1
2
3
4
"""
#it looks like it should print 1 to 5, but it doesnt
##this is a result of "off-by-one" behavior i'll often see in languages
#the RANGE() function causes PYTHON to start counting at the first value you give it, and it stops at the second value u providee
#because it stops at that second value, the output never contains the end value, which wud be 5 here
#to print 5, you stop at 6

#if my output is different from what i expect when i'm using range(), i'll try adjusting my end my end value by one
#you can alos pass RANGE() only one arguement and it will start the sequence of numbers at 0,,,
#EG-: range(6)

