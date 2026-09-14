name = str(input("Name: ").title())
age = int(input("Age: "))
city = str(input("City: ").title())
year = int(input("Year: "))

info = {
    'username':name,
    'userage':age,
    'usercity':city,
    'useryear':year,
}

print("This is your info: ")
print("Your name is " + str(info['username']) + " and you are " + str(info['userage']))

print("\nMore info...")
print("You come from " + str(info['usercity']) + " and you were born in " + str(info['useryear']))

# output
"""
Name: kayondo
Age: 21
City: kira
Year: 2004
This is your info: 
Your name is Kayondo and you are 21

More info...
You come from Kira and you were born in 2004
"""
