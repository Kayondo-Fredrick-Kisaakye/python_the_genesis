#you can use individual values from a list as you would any other variable
#EG-: u can use F-STRING to create a message based on value from list

#lets try pulling the first boy from the list and compose a message using that value
boys = ['fredrick', 'douglas', 'patrick', 'john']
message = f"My name is {boys[0].title()}"
print(message)   #My name is Fredrick

#build a sentence using value at boys[0] and assign it to variable 'message'