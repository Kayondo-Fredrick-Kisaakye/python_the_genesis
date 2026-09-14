# Accepting Input in Python 2.7

"""If you’re using Python 2.7, you should use the raw_input() function when 
prompting for user input. This function interprets all input as a string, just 
as input() does in Python 3.
Python 2.7 has an input() function as well, but this function interprets 
the user’s input as Python code and attempts to run the input. At best you’ll 
get an error that Python doesn’t understand the input; at worst you’ll run 
code that you didn’t intend to run. If you’re using Python 2.7, use raw_input() 
instead of input().
"""
