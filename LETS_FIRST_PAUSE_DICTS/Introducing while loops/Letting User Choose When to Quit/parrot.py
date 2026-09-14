# We can make the parrot.py program run as long as the user wants by putting 
# most of the program inside a while loop. We’ll define a quit value and then 
# keep the program running as long as the user has not entered the quit value:

prompt = "\nTell me something and i will tell it back to you: "
prompt += "\nEnter 'quit' to end program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

"""
At 5, we define a prompt that tells the user their two options: enter
ing a message or entering the quit value (in this case, 'quit'). Then we set 
up a variable message 8 to store whatever value the user enters. We define 
message as an empty string, "", so Python has something to check the first 
time it reaches the while line. The first time the program runs and Python 
reaches the while statement, it needs to compare the value of message to 
'quit', but no user input has been entered yet. If Python has nothing to 
compare, it won’t be able to continue running the program. To solve this 
problem, we make sure to give message an initial value. Although it’s just an 
empty string, it will make sense to Python and allow it to perform the com
parison that makes the while loop work. This while loop 9 runs as long as 
the value of message is not 'quit'.
The first time through the loop, message is just an empty string, so Python 
enters the loop. At message = input(prompt), Python displays the prompt and 
waits for the user to enter their input. Whatever they enter is stored in message 
and printed; then, Python reevaluates the condition in the while statement. 
As long as the user has not entered the word 'quit', the prompt is displayed 
again and Python waits for more input. When the user finally enters 'quit', 
Python stops executing the while loop and the program ends

Tell me something and i will tell it back to you: 
Enter 'quit' to end program. hello
hello

Tell me something and i will tell it back to you: 
Enter 'quit' to end program. hello again
hello again

Tell me something and i will tell it back to you: 
Enter 'quit' to end program. i am dyk
i am dyk

Tell me something and i will tell it back to you: 
Enter 'quit' to end program. quit
quit
"""
