# import random

# TODO Create an empty list to maintain the player names
player_names = []
# players = []
count = 0

# add_players = input("Would you like to add players? y/n ")
# while True:
    # TODO Ask the user if they'd like to add players to the list.
    # add_players = input("Would you like to add players? y/n ")
    # If the user answers "Yes", let them type in a name and add it to the list.
    # if add_players == lower(y):
while add_players.lower() == 'yes':
        name = input("\nEnter player name: ")
        player_names.append(name)
        add_players = input("Would you like to add players? y/n ")

        # If the user answers "No", print out the team 'roster'
    # else:
    #     print("Roaster")
    #     for i in player_names:
    #         print(i)
    #         count+=1

            # TODO print the number of players on the team
        # print(count)
print("\nThere are {} players on the team.".format(len(player_names)))
        # TODO Print the player number and the player name
        # The player number should start at the number one
player_number = 1
for player in player_names:
    print("Player {}: {}".format(player_number, player_names)
    player_number += 1


# TODO Select a goalkeeper from the above roster
# goalkeeper = random.randint(player_number)
# goalkeeper = player_number[0]
keeper = input("PLease select the goal keeper by player number. (1-{})".format(player_names)))
keeper = int(keeper)
# TODO Print the goal keeper's name
# Remember that lists use a zero based index
# print("goalkeeper is {}:{}".format(player_number, name))
print("Great!! The goalkeeper for the game will be {}".format(player_names[keeper - 1]))
