nieces = []
nephews = []

nieces.append('hadasah')
nieces.append('paula')
nieces.append('evangelina')
nieces.append('hannah')  #append adds at te end

nephews.insert(0, 'elisha')
nephews.insert(1, 'micheal')
nephews.insert(2, 'fabian')   #this one extends others to the right wen inserting to the index

print(nieces)    #['hadasah', 'paula', 'evangelina', 'hannah']
print(nephews)   #['elisha', 'micheal', 'fabian']

nieces[3] = 'favour'  #modifying -
print(nieces)    #['hadasah', 'paula', 'evangelina', 'favour']

del nieces[3]
print(nieces)   #['hadasah', 'paula', 'evangelina']