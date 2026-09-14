first_name = input("First Name: ")
last_name = input("Last Name: ")
age = input("Age: ")
city = input("City: ")

person_info = {
    'first_name':first_name.title(),
    'last_name':last_name.title(),
    'age':age,
    'city':city.title(),
}
must_person_info = {
    'first_name':'Kayondo',
    'last_name':'Fredrick',
    'age':'21',
    'city':'Kira',
}

if person_info == must_person_info:
    print("Name: " + str(person_info['first_name']))
    print("Other Name: " + str(person_info['last_name']))
    print("Age: " + str(person_info['age']))
    print("City: " + str(person_info['city']))
else:
    print("INVALID CREDENTIALS")