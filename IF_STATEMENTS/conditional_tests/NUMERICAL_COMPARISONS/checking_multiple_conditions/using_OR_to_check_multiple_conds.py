#the keyword OR allows you to check multiple conditions as well, but it passes when either or both of the tests pass
#an OR expression fails only when both individual tests fail
#lets consider two ages again, but this time we'll look for only one person to be over 21:

"""
#>>> age_0 = 22
#>>> age_1 = 18
#>>> age_0 >= 21 or age_1 >= 21
True
#>>> age_0 = 18
#>>> age_0 >= 21 or age_1 >= 21
False
"""
#we start with 2 age variables again, bicoz the test for age_0 passes, the overall expression evaluates to TRUE
#we then lower age_0 to 18, in final test, both tests now fail and the expression evaluates to FALSE