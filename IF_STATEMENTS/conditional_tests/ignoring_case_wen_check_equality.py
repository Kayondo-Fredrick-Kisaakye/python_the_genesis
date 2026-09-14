#testing for equality is case sensitive in PYTHON, EG-: two values with different capitalization are not equal
"""
>>> car = 'audi'
>>> car == 'Audi'
False
"""

#if case matters, this behavior is advantageous, but if case don't matter, instead you just want to test the value
#of a variable, you can convert the variable's value to lowercase before doing comparison
"""
>>> car = 'Audi' 
>>> car.lower() == 'audi'
True
"""
#this test will return TRUE no matter how the value is formatted coz the test is now case insensitive
#the LOWER() method doesn't change the value that was originally stored in car
#so you can do this kind of comparison without affecting original variable

#we first assign the capitalized string 'Audi' to the variable car
#then convert th value of car to lowercase and compare the lowercase value string to 'audi'
#the two strings match, so Python returns TRUE
#websites enforce certain rules for the data that users enter in a manner similar to this,
#EG-: a site might use a conditional test like this to ensure that every user has a truly unique username, not just
#a variation on the capitalization of another person's username

#when someone submits a new username, that new username is converted to lowercase and compared to the lowercase
#versions of all existing usernames, during this check, a username like 'John' will be rejected of any variation of 'john'
#already in use