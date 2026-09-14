disciples = ['john', 'luke', 'matthew', 'peter', 'james']
print(disciples[0].title())
print(disciples[1].upper())
print(disciples[2].lower())
print(disciples[3])
print(disciples[4])

message = f"{disciples[0]} is the most beloved, {disciples[3].title()}, is a hard guy naye yatyaamu"
message_2 = f"...{disciples[1].title()} and {disciples[2].title()} and {disciples[4].title()}"

print(message + message_2 + " i have no info about them")