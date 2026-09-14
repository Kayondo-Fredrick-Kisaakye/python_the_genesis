mypizzas = ['beef pizza', 'chicken pizza', 'pork pizza']
frdpizzas = mypizzas[:]

mypizzas.append('fish pizza')
frdpizzas.append('vegan pizza')

print(mypizzas)
print(frdpizzas)

print("my favorite pizzas are:")
for mypizza in mypizzas:
    print(mypizza.title())

print("\n my friends fav pizzas are:")
for frdpizza in frdpizzas:
    print(frdpizza.title())