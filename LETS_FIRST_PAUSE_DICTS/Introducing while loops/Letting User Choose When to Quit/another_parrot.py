prompt = "Tell me sth i'll say it back: "
prompt += "\nEnter 'quit' to stop program: "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)