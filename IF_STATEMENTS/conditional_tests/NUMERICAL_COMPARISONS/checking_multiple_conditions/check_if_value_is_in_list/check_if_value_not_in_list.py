#checking whether a value is not in the list__
#othertimes its important to know if a value does not appear in a list, you can use the keyword NOT
#EG-: consider a list of users who are banned before allowing that person to submit a comment
#you can check whether a user has been banned before allowing them to comment if they were banned from commenting

banned_users = ['marvin', 'johnson', 'dickson', 'muha']
user = 'kimbowa'

if user not in banned_users:
    print(f"{user.title()}, you can post a response")

#the if statement here reads quite clearly, if the value of user is not in the list banned_users,
#python returns TRUE and executes the indented line
#the user 'kimbowa' is not in the list so he gets the message