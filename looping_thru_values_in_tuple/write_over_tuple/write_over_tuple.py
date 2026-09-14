#though you can't modify a tuple, u can assigna new varia to a variable that represents a tuple
#EG-: if we wanted to change the dimensions of this rectangle, we cud redefine the entire tuple

dimensions = (200, 50)
print("ORIGINAL DIMENSIONS")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nNEW DIMENSIONS")
for dimension in dimensions:
    print(dimension)

"""
ORIGINAL DIMENSIONS
200
50

NEW DIMENSIONS
400
100

"""
#use tuples wen you want to store a set of values that should not be changed as the program lives