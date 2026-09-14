#some times u might need two conditions to be TRUE to take an action,
#other times u might be satisfied with just one condition being TRUE
#the key words AND and OR can help you in these sitituations

#using AND to check multiple conditions
"""
#>>> age_0 = 22
#>>> age_1 = 18
#>>> age_0 >= 21 and age_1 >= 21
False
#>>> age_1 = 22
#>>> age_0 >= 21 and age_1 >= 21
True
"""
#first, we define two ages, age_0 and age_1
#then we check whether both ages are 21 or older
#the test on the left passes, but the test on the right fails, so the overall conditional expression evaluates to FALSE
#we then change age_1 to 22
#the value of age_1 is now greater than 21, so both individual tests pass, causing the overall conditional expression to evaluate as TRUE

#to improve redanbility, you can use pareentheses around the individual tests, but they are not required,
#if you use them, your test would look like this
"""
(age_0 >= 21) and (age_1 >= 21)
"""
