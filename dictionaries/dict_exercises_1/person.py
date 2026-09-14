# Use a dictionary to store information about a person you know .
# Store their first name, last name, age, and the city in which they live . You
# should have keys such as first_name, last_name, age, and city . Print each
# piece of information stored in your dictionary

first_name = input("First Name: ")
last_name = input("Last Name: ")
age = input("Age: ")
city = input("City: ")

person_info = {
    'first_name':first_name,
    'last_name':last_name,
    'age':age,
    'city':city,
}

print("Name: " + str(person_info['first_name'].title()))
print("Other Name: " + str(person_info['last_name'].title()))
print("Age: " + str(person_info['age']))
print("City: " + str(person_info['city'].title()))

""" 
First Name: kayodo
Last Name: fredrick
Age: 21
City: kira
Name: Kayodo
Other Name: Fredrick
Age: 21
City: Kira

Process finished with exit code 0
"""