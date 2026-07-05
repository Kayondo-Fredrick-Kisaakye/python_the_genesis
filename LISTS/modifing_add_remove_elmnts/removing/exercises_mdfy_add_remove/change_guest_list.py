guests = ['essie', 'swabra', 'aminah', 'ritah', 'shuda', 'rodney', 'ronnie']
message = "i'd love to see you at dinner tonight at mine's"

print(f"hello, {guests[0].title()}, {message}.")
print(f"hello, {guests[1].title()}, {message}.")
print(f"hello, {guests[2].title()}, {message}.")
print(f"hello, {guests[3].title()}, {message}.")
print(f"hello, {guests[4].title()}, {message}.")
print(f"hello, {guests[5].title()}, {message}.")
print(f"hello, {guests[6].title()}, {message}.")

print(f"Hi, guys \nUnfortunately, {guests[6].title()} won't make it so i'll exclude him")
guests[6] = 'timo' #here ive replaced ronnie with timo

print(f"hello, {guests[0].title()}, {message}.")
print(f"hello, {guests[1].title()}, {message}.")
print(f"hello, {guests[2].title()}, {message}.")
print(f"hello, {guests[3].title()}, {message}.")
print(f"hello, {guests[4].title()}, {message}.")
print(f"hello, {guests[5].title()}, {message}.")
print(f"hello, {guests[6].title()}, {message}.")  #timo is invited