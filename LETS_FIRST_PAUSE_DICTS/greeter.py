# You can store your prompt in a variable and pass that variable to the input() 
# function. This allows you to build your prompt over several lines, then write 
# a clean input() statement.

prompt = "if you tell us who you are, we can personalize the messages you see."
prompt += "\nWhats your first name?: "

name = input(prompt)
print("\nHello," + name + "!")

"""
This example shows one way to build a multi-line string. The first line 
stores the first part of the message in the variable prompt. In the second line, 
the operator += takes the string that was stored in prompt and adds the new 
string onto the end.
The prompt now spans two lines, again with space after the question 
mark for clarity:
"""
# if you tell us who you are, we can personalize the messages you see.
#Whats your first name?: kayondo

#Hello,kayondo!