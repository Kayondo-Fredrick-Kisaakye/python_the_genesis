schools = ['st. peters', 'st. lawrence', 'st. paul']
babes = ['cindy', 'priscilla', 'nelly']
dudes = ['patrick', 'shuda', 'bismark']
names = ['kayondo fredrick kisaakye', 'sr. dyk']
schools_num = len(schools)   #number of items in the list, i give it a variable
babes_num = len(babes)
dudes_num = len(dudes)


print(f"My name is {names[0].title()}...aka {names[1].upper()},\ni was at {schools[0].title()}, {schools[1].title()} and {schools[2].title()}")
print(f"some of the girls i liked were, {babes[0].title()}, {babes[1].title()} and {babes[2].title()} \nthey were more than {babes_num}")
print(f"these are the guys, {dudes}")

dudes.insert(0, 'marvin')  #i put marvin in first place with insert
print(f"{dudes}, see who i've added?")
dudes.sort(reverse=True)
print(dudes)   #here i have reversed their order but i dont understand why its like this
#['marvin', 'patrick', 'shuda', 'bismark'], see who i've added?--line 15
#['shuda', 'patrick', 'marvin', 'bismark']                     --line 17

dudes.append('douglas')   #added douglas at the end with append
print(dudes)   #['shuda', 'patrick', 'marvin', 'bismark', 'douglas']

del dudes[0]   #deleted shuda, remember this remove forever
print(dudes)   #['patrick', 'marvin', 'bismark', 'douglas']

dudes.remove('bismark')  #removed bismark
print(dudes)   #['patrick', 'marvin', 'douglas']
print(dudes[2].upper())   #DOUGLAS capitalized

print(dudes)  #['patrick', 'marvin', 'douglas']
print(babes)  #['cindy', 'priscilla', 'nelly']
print(schools) #['st. peters', 'st. lawrence', 'st. paul']

schools.append(' slau univ ')
print(schools[3].strip())  #remove whitespace from both ][[[[[[[[[[[[[[[[[[[[[[[[[[][[

print(schools)  #['st. peters', 'st. lawrence', 'st. paul', ' slau univ ']
print(f"num of schools is {schools_num}")   #num of schools is 3-- i dont understan why it says 3 yet i added slau

website = "https://slau.co.ac"
print(website.removeprefix('https://'))  #slau.co.ac  -- removed 'https://'
print(website.removesuffix('.ac'))       #https://slau.co  -- removed '.ac'

cars = ['fiat', 'bently', 'daihatsu', 'mazda', 'toyota']
print(cars)

del cars[1]
print(cars)

cars.append('audi')
print(cars)

cars.insert(0, 'bmw')
print(cars)   #['bmw', 'fiat', 'daihatsu', 'mazda', 'toyota', 'audi']

cars.remove('daihatsu')
print(cars)   #['bmw', 'fiat', 'mazda', 'toyota', 'audi']

cars.pop(1)
print(cars)   #['bmw', 'mazda', 'toyota', 'audi']

popped_car = cars.pop(1)
print(f"i drive a, {popped_car}")  #i drive a, mazda

print(len(cars))   #3

print(cars)   #['bmw', 'toyota', 'audi']
cars.reverse()
print(cars)   #['audi', 'toyota', 'bmw']
print(cars.sort())  #None
print(cars)   #['audi', 'bmw', 'toyota']

#something is wrong here, let me revisit my book and see the SORT and SORTED parts again

boys = ['douglas', 'andrew', 'kevin', 'christopher']
print(boys)   #['douglas', 'andrew', 'kevin', 'christopher']
boys.sort()
print(boys)   #['andrew', 'christopher', 'douglas', 'kevin']
#it sorts parmanently

boys.sort(reverse=True)
print(boys)   #['kevin', 'douglas', 'christopher', 'andrew']
boys.sort(reverse=False)
print(boys)   #['andrew', 'christopher', 'douglas', 'kevin']

#temporary with SORTED()
girls = ['bree', 'pree', 'fhee']
print(girls)   #['bree', 'pree', 'fhee']
print(sorted(girls))  #['bree', 'fhee', 'pree']
print(girls)     #['bree', 'pree', 'fhee']

girls.reverse()
print(girls)     #['fhee', 'pree', 'bree']
