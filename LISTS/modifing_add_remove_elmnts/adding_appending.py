#SOME REASONS WHY YOU MIGHT ADD
#>>>new characters appear in a game
#>>>new data to a visualization
#>>>new registerd users

#appending to the END of LIST
#simplest  way, wen u append, the new element is added to the end
cars = ['honda', 'audi', 'bmw', 'toyota']
print(cars)  #['honda', 'audi', 'bmw', 'toyota']

cars.append('fiat')
print(cars)  #['honda', 'audi', 'bmw', 'toyota', 'fiat']

#its als0 dynamic, you can start with an empty list, and keep on adding with 'append() calls'
boys = []
boys.append('jordan')
print(boys)   #['jordan']

boys.append('herbert')
print(boys)   #['jordan', 'herbert']

#biulding lists like this is very common cus you often wont know the data your users want to store in a program until
#until after program is running...to put your users in control, start by defining an empty list that will hold their values
#then APPEND each new value provided to list you just created