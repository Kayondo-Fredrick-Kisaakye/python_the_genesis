our_exes = {
    'fredrick':['cindy', 'shania', 'gihozo'],
    'nyanzi':['diana', 'mahara'],
    'marvin':['shantel', 'tina', 'shirat'],
    'jexi':['hajat', 'viola', 'jane'],
}

for name, exes in our_exes.items():
    print(name.title() + "'s exes are listed below:")
    for exe in exes:
        print("\t" + exe.title())