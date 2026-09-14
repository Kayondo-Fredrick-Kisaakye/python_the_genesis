name_one = input("Enter name_one: ")
name_two = input("Enter name_two: ")

names = (name_one.title(), name_two.title())

for name in names:
    print(f"{name}, is your name!")