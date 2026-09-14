guests = ['kyomya', 'marvin', 'nalikka', 'viola', 'nelly']
vips = ('mark', 'herbert')

for guest in guests:
    print(f"Hello, {guest}, good to see you here!") #used a loop to print a message to everyone in guest list

print("\n")

for vip in vips:
    print(f"GOOD TO HAVE YOU HERE TODAY {vip}, ENJOY YOUR EVENING!")# loop print message to vip tuple guys

print("\n")

for guest in guests[:4]:
    print(f"You {guests[:4]}, guy head east to find your seats.")  #tried to   use a slice to print the text to 4
