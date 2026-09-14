admin_user = "Sr Dyk"
other_user = "Essie Kay"

user_name = input("Enter Username")
if user_name == admin_user:
    print("Welcome the big man!")
elif user_name == other_user:
    print("Welcome the big woman!")
else:
    print("Not Authorized!")