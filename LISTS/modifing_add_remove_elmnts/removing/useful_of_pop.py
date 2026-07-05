#so, imagine that the cars in the list are stored in chronological order, according to wen we bought them
#if  this is the case,  we can apply the POP() METHOD to print a statement about the last car we bought

cars = ['toyota fortuner', 'land cruiser 76', 'mazda mx5', 'mercedes g63']
last_bought = cars.pop()

print(f"the most recent car i've bought is the {last_bought.title()}.")
#OUTPUT:- the most recent car i've bought is the Mercedes G63.