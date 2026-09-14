#you can do just about anything with each item in a for loop, lets build on the previous examples by printing a message to each chic
chics = ['doreen', 'favour', 'betty']
for chic in chics:
     print(f"{chic.title()}, you are light skinned!"]\

"""
Doreen, you are light skinned!
Favour, you are light skinned!
Betty, you are light skinned!
"""
#you can also write as many lines of code as you like in the for loop, every indented line following the line
#"FOR CHIC IN CHICS" is considered INSIDE the LOOP, and each indented line is executed once for each value in the list
#therefore you can do as much as you like with each value in the list
#lets add a second line to our message, telling each chic that we're hiring...

#check>>>>> hiring.py