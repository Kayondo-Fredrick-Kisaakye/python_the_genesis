favorite_cars = {
    'jen': 'pajero',
    'sarah': 'c63',
    'edward': 'range rover',
    'phil': 'land cruiser',
}

friends = ['sarah', 'phil']
for name in favorite_cars.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", i see your favorite car is " + favorite_cars[name].title() + "!")