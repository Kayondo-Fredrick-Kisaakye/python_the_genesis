player_one = {'shape':'triangle', 'points':'10'}
player_one_play = input("enter shape: ")

new_points = player_one["points"]

if player_one_play == player_one["shape"]:
    print("you just earned " + str(new_points) + " points!")
else:
    print("you lost " + str(new_points) + " points!")