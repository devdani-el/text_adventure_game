from time import sleep
from sys import exit

nick = []

# Introduction
def introduction():
    print('''
  88  88  88  88   888888888888888  88888    88   8888   88  88    888888
 888  888 88  88  88     88  88	    88  88   88 88    88 88  88   88
88 8888 88 8888    8888  88  8888   88888    88 88    88 88  88    8888
88  88  88  88        88 88  88	    88  88   88 88    88 88  88       88
88  88  88  88 88888888  88  888888 88   888 88   8888    8888 88888888''')
    print('''
	    88888    88  88   88   88 8888888   888888   8888     88    88
	    88   88  88  88  888   88 88         88     88    88  888   88
	    88    88 88  88 88 888 88 88   88    8888   88    88 88 888 88
	    88   88  88  88 88   8888 88    888  88     88    88 88   8888
	    88888     8888  88     88  888888 88 888888   8888  888     88
''')
    print('Welcome to the Text Adventure Game!')
    sleep(2)
    print('You find yourself in front of a mysterious dungeon.')
    sleep(2)
    print('Your goal is to navigate through and find the treasure.')
    sleep(2)
    print('But before...\n')
    sleep(2)

def nickname():
    name = str(input('What is your name, noble adventurer: ')).strip().capitalize()
    nick.append(name)
    return name

# choose path
def choose_path():
    while True:
        print(f'\nAdventurer, {nickname()}')
        print('Make your future... ⚔️')
        sleep(2)
        print('1 - Enter the dungeon')
        print('2 - go away to explore')
        choose = int(input('Enter 1 or 2: '))
        if choose == 1:
            break
        else:
            go_away()
        return choose_path
    

def go_away():
    print('\nYou chose to move on.')
    sleep(2)
    print('You LOSE! 👾👾👾')
    exit()


# explore dungeon
def explore_dungeon():
    print('\nYou entered the dark dungeon 🏯')
    sleep(2)
    print('Two doors were found.')
    sleep(2)
    print('Which one do you want to open?')
    sleep(1)
    print('1 - Right door 🚪')
    print('2 - Left  door 🚪')
    choose = int(input('Enter 1 or 2: '))
    if choose == 1:
        treasure_room()
    else:
        left_door()
        game_over()
    return explore_dungeon

def left_door():
    print("\nOh no! You've come across a large basilisk.")
    sleep(2)
    game_over()

# treasure room
def treasure_room():
    print("\nBravo! Adventurer, you've found the treasure room. ")
    sleep(2)
    print('You WON! 🪙🪙🪙')
    print(f'{nick[0]}, you have completed your journey! Return home with your treasure.')


# game over
def game_over():
    print('\nYou LOSE! 👾👾👾')
    sleep(2)
    exit()
    


# main
def main():
    introduction()
    choose_path()
    explore_dungeon()


if __name__ == '__main__':
    main()