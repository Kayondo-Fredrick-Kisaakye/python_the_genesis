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

print(f"Hi, again guys\ni've found a bigger table so i'll invite more 3 people.")
guests.insert(0, 'bbosa')  #added as the first
guests.insert(4, 'suphian')  #added in the fifth place
guests.append('kato')     #added in the last place

print(f"hello, {guests[0].title()}, {message}.")  #bbosa
print(f"hello, {guests[1].title()}, {message}.")
print(f"hello, {guests[2].title()}, {message}.")
print(f"hello, {guests[3].title()}, {message}.")
print(f"hello, {guests[4].title()}, {message}.")  #suphian
print(f"hello, {guests[5].title()}, {message}.")
print(f"hello, {guests[6].title()}, {message}.")
print(f"hello, {guests[7].title()}, {message}.")
print(f"hello, {guests[8].title()}, {message}.")
print(f"hello, {guests[9].title()}, {message}.")  #kato

print(f"HAHA! SIKE!\n...i'm only inviting {guests[6].title()} and {guests[7].title()}, others go find sth else to do.")
print(guests)
remove_bbosa = guests.pop(0) #popped out bbosa
print(f"sorry mate, {remove_bbosa}, maybe sleep earlier tonight.")

remove_essie = guests.pop(0)
print(f"sorry mate, {remove_essie}, maybe sleep earlier tonight.")

remove_swabra = guests.pop(0)
print(f"sorry mate, {remove_swabra}, maybe sleep earlier tonight.")

remove_aminah = guests.pop(0)
print(f"sorry mate, {remove_aminah}, maybe sleep earlier tonight")

remove_suphian = guests.pop(0)
print(f"sorry mate, {remove_suphian}, maybe sleep earlier tonight.")

remove_ritah = guests.pop(0)
print(f"sorry mate, {remove_ritah}, maybe sleep earlier tonight.")

remove_timo = guests.pop(2)
print(f"sorry mate, {remove_timo}, maybe sleep earlier tonight.")

remove_kato = guests.pop(2)
print(f"sorry mate, {remove_kato}, maybe sleep earlier tonight.")

print(f"okay, {guests[0].title()}, don't come later than 8:00, pick up {guests[1].title()}.")
print(f"yeah, so {guests[0].title()} is going to pick you up from where you chose, don't come later than 8:00")

del guests[0]
del guests[0]
print(guests) #the list is now empty