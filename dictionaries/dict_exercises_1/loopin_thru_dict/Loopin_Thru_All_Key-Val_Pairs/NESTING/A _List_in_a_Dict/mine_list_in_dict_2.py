fav_cars = {
    'jexi':['mercedes', 'bmw'],
    'marvol':['hyundai', 'honda'],
    'sr dyk':['lexus', 'toyota', 'audi'],
    'shvda':['range rover', 'lexus'],
}

for name, cars in fav_cars.items():
    print(name.title() + "'s favorite cars are:")
    for car in cars:
        print("\t" + car.title())