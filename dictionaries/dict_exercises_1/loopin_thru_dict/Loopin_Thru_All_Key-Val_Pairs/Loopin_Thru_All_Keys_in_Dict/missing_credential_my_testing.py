# You can also use the keys() method to find out if a particular person
# was polled. This time, let’s find out if Erin took the poll:

name = input("NAME: ")
age = input("AGE: ")
sex = input("SEX: ")

credentials = {
    'name':name,
    'age': age,
    'sex': sex,
    }

if name not in credentials.values():
    print("Answer everything!")

# FAILED TO DO IT!