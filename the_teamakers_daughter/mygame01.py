#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# imports
import pyfiglet
from rooms import rooms

title = pyfiglet.figlet_format("The Adubi War" ,font = "slant")


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands

    print(title)    

    print('''
    This is the story of the gods
    Location: SouthEast Nigeria, pre-colonial Alaigbo(igboland).
    ========
    Commands:
    go [direction]
    get [item]
    
    # directions[north, south, east, west]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print description
    print(rooms[currentRoom]['desc'])
    #print the current inventory
    print('Inventory : ' + str(inventory))

#an inventory, which is initially empty
inventory = []
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)
    

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
    continue


    #if they type 'get' first
    if move[0] == 'get' and move[1] == 'key':
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('you have collected a ' + move[1])

            #delete the item from the room
            del rooms[currentRoom]['item']
            continue

        #otherwise, if the item isn't there to get

    if move[0] == 'get' and move[1] == 'map':
         #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('you have just acquired a' + move[1] + '. You glance through and theres directions around the shrine.\n'
            '==================='
            '|   MAP oF MBARI  |'
            '==================='
            'You are in the south wing \n'
            'To the north of the south wing is the Hall \n'
            'To the east of the hall is the east wing \n'
            'To the west of the hall, you will find a secret doorway \n'
            'Find ekwensu before he finds you \n'
            'and pray to your Alusi that you have the means to trap his essence forever \n'
            'to complete this quest is to find your way to the mouth of the sacred grove. \n'
            'BEWARE of TRAPS!!!'
            )
            #delete the item from the room
            del rooms[currentRoom]['item']
            continue
      
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
            continue

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You have succeeded in vanquising the evil mascqurade Ekwensu and discovered the ULTRA RARE telepotion... YOU WIN!')
        break

    ## Define how player gets inside the crypt
    if currentRoom == 'secret_doorway' and 'key' in inventory:
        print('You have suddenly found yourself in a crypt and the dor quickly snaps shut behind you.It is pitch dark and drafty.')
        if 'lantern' in inventory:
            print('luckily you snagged a lantern from the south wing. you turn your latern on and as the light brightens the room, you notice 3 distinctly marked statues. \n '
            'six figures are arranged carefully against the crypt\'s interior wall. They are marked boldly with the numbers 6 7 2 respectively. You now have 15 seconds to \n'
            'figure out the combinations and escape before you suffocate')

        else:
            print('you have no lantern to see around. You have suffocated.')
    #break        
        

