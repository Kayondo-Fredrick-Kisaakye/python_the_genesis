#what happens after a foor loop has finished executing?
#usually, you'll want to summmarize a block of out put or move on to other  work that your program must do

#any lines of code after the for loop that are not indented are executed once without repitition,
chics = ['doreen', 'favour', 'betty']
for chic in chics:
     print(f"{chic.title()}, you are light skinned!")
     print(f"we are hiring, {chic.title()}.\n")

print("thank you all, see you next time")

#when processing data with a for loop, youll find that this is a good way to summarize an operation that was perfomed
#on an entire data-set>>>EG-: >>>u might use FOR LOOP to initialize a game by running through a list of characters and
#displaying each character on the screen...
#you  might then write soome additional code after this loop that displays a PLAY NOW button after all the characters
#have been drawn to screen