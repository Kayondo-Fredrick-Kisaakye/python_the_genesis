prompt = "To end program, Type 'stop': "
prompt += "\nType Here: "

typed_word = ""
while typed_word != 'stop':
    typed_word = input(prompt)
    
    if typed_word != 'stop':
        print(typed_word)