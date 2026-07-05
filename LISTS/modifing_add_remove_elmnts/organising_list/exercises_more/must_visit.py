places = ['egypt', 'switzerland', 'south africa', 'maldives', 'madagascar', 'japan']
print(places)   #['switzerland', 'south africa', 'maldives', 'madagascar']

print(sorted(places))   #['madagascar', 'maldives', 'south africa', 'switzerland']

print(places)   #['switzerland', 'south africa', 'maldives', 'madagascar']

places.sort(reverse=True)  #---added EGYPY later
print(places)   #['switzerland', 'south africa', 'maldives', 'madagascar', 'japan', 'egypt']

places.sort(reverse=False)
print(places)   #['egypt', 'japan', 'madagascar', 'maldives', 'south africa', 'switzerland']

places.sort()
print(places)   #['egypt', 'japan', 'madagascar', 'maldives', 'south africa', 'switzerland']

places.sort(reverse=True)
print(places)   #['switzerland', 'south africa', 'maldives', 'madagascar', 'japan', 'egypt']
