# This program works well, except that it prints the word 'quit' as if it 
# were an actual message. A simple if test fixes this:

prompt = "Tell me something and i will tell it back to you: "
prompt += "\nEnter 'quit to end program: "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)