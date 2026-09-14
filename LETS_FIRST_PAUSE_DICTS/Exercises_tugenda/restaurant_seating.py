# Write a program that asks the user how many people are in their dinner group
# If the answer is more than eight, print a message saying
# they’ll have to wait for a table . Otherwise, report that their table is ready

prompt = "Welcome, tell us how many people are in your dinner group."
prompt += "\nEnter Number: "

number = int(input(prompt))

if number > 8:
    print("Youll have to wait for a table.")
else:
    print("Your their table is ready")
    
# Welcome, tell us how many people are in your dinner group.
# Enter Number: 9
# Youll have to wait for a table.