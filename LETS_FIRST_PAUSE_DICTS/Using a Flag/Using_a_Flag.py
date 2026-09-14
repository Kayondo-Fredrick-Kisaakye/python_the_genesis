# In the previous example, we had the program perform certain tasks while 
# a given condition was true. But what about more complicated programs in 
# which many different events could cause the program to stop running?

# For example, in a game, several different events can end the game. 
# When the player runs out of ships, their time runs out, or the cities they 
# were supposed to protect are all destroyed, the game should end. It needs 
# to end if any one of these events happens. If many possible events might 
# occur to stop the program, trying to test all these conditions in one while 
# statement becomes complicated and difficult.

# For a program that should run only as long as many conditions are true, 
# you can define one variable that determines whether or not the entire pro
# gram is active. This variable, called a flag, acts as a signal to the program. We 
# can write our programs so they run while the flag is set to True and stop run
# ning when any of several events sets the value of the flag to False. As a result, 
# our overall while statement needs to check only one condition: whether or 
# not the flag is currently True. Then, all our other tests (to see if an event has 
# occurred that should set the flag to False) can be neatly organized in the rest of the program.

# Let’s add a flag to parrot.py from the previous section. This flag, which 
# we’ll call active (though you can call it anything), will monitor whether or 
# not the program should continue running:

prompt = "\nTell me sth and i'll tell it back to you: "
prompt += "\nEnter 'quit' to end program: "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)

# We set the variable active to True 28 so the program starts in an active 
# state. Doing so makes the while statement simpler because no comparison is 
# made in the while statement itself; the logic is taken care of in other parts of 
# the program. As long as the active variable remains True, the loop will continue running 29

# In the if statement inside the while loop, we check the value of message 
# once the user enters their input. If the user enters 'quit' 32, we set active 
# to False, and the while loop stops. If the user enters anything other than 
# 'quit' 34, we print their input as a message.

# This program has the same output as the previous example where we 
# placed the conditional test directly in the while statement. But now that we 
# have a flag to indicate whether the overall program is in an active state, it 
# would be easy to add more tests (such as elif statements) for events that 
# should cause active to become False. This is useful in complicated programs 
# like games in which there may be many events that should each make the 
# program stop running. When any of these events causes the active flag to 
# become False, the main game loop will exit, a Game Over message can be 
# displayed, and the player can be given the option to play again.

