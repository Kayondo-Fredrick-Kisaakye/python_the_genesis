chics = ['doreen', 'favour', 'betty']
for chic in chics:
     print(f"{chic.title()}, you are light skinned!")
     print(f"we are hiring, {chic.title()}.\n")

"""
Doreen, you are light skinned!
we are hiring, Doreen.

Favour, you are light skinned!
we are hiring, Favour.

Betty, you are light skinned!
we are hiring, Betty.
"""
#bicoz we have indented both calls to print(), each line will be executed once for every chic in the list
#the (\n) new line in the second print() call inserts a blank line after each pass through the loop.
#this creates a set of messages that are neatly grouped for each person

#you can use as  many lines as you like in yourr for loops,in practice, u'll often find it usefull to do
#a number of different operations with each item in a list when you usea for loop.

