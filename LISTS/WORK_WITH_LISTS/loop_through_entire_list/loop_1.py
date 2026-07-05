#you'll often want to run through all entries in a list
#performiing the same task wit each item
#like,,in a game you might want to move every element on the screen by   the same amount
#in a list of members, u might want to perform the same statistical operration on every element

#r perhaps, u'll want to display each headline from a  list of articles oon a website
#,,when you want to do the same action with every item in a list, u can use PY's FOR LOOP<<<

#say we have a list of chics' names, and we want to print out each name in list
#we could do this by retrieving each name from the list individualy, but this approach cud cause several zibs
#if one, it would be repeatitive to do this with a  long list of names
#also, we'd have to change our code each time the list length changed
#using FOR LOOP avoids both of these issues by letting PYTHON manage these issues internally

#lets use FOR LOOP to print chis' names

chics = ['doreen', 'josephine', 'favour', 'mitchelle']   #define list
for chic in chics:                      #define FOR LOOP
    print(chic)                    #prints name that has been assigned to chic

#python then repeats these last two lines, once for  each name in list