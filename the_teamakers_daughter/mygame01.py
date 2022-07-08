#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# imports
import pyfiglet
import threading
import os
from rooms import roominfo

title = pyfiglet.figlet_format("Ishindu's fate" ,font = "slant")

def decision():
    print("You took too long! you have suffocated!!")
    os._exit(os.EX_OK) 


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands

    print(title)    

    print('''
    ======================================================================
    This is the story of the gods
    Location: SouthEast Nigeria, pre-colonial Alaigbo(igboland).
    ======================================================================
    Commands:
    go [direction]
    get [item]
    
    # directions[north, south, east, west]
    ''')

def showStatus():
    """determine the current status of the player"""
    #print description
    print(roominfo[currentRoom]['desc'])
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

    move = ''
    while move == '':  
        move = input('>')
         
    move = move.lower().split(" ", 1)
    os.system('clear')  # clear the screen

    #get moves: player is in the hall and gets key
    #if move == 'get' 'key'  
    if move[0] == 'get' and move[1] == 'key':
        #if the room contains key, and the key is the one they want to get
        if "item" in roominfo[currentRoom] and move[1] in roominfo[currentRoom]['item']:
            #add key to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('you have collected a ' + move[1])

            #delete key from the room
            del roominfo[currentRoom]['item']
            print(f"inventory : {inventory}")
            continue
        else:
            print('You cant get ' + move[1] + '!')
            #otherwise, if key isn't there to get

    #if player is in the South_wing and gets map or lantern
    if move[0] == 'get' and move[1] == 'map':
         #if the room contains an item, and the item is the one they want to get
        if "item" in roominfo[currentRoom] and move[1] in roominfo[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('you have just acquired a ' + move[1] + '. You glance through and theres directions around the shrine.\n'
            '===================\n'
            '|   MAP oF MBARI  |\n'
            '===================\n'
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
            del roominfo[currentRoom]['item'][0]

    elif move[0] == 'get' and move[1] == 'lantern':
        if "item" in roominfo[currentRoom] and move[1] in roominfo[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('you have collected a ' + move[1])

            #delete the item from the room
            del roominfo[currentRoom]['item'][1]

            print(f"inventory : {inventory}")
        else:
            print('You cant get ' + move[1] + '!')
            #otherwise, if the item isn't there to get
            continue


    ## player go moves
    if move[0] == 'go' :
        if move[1] in roominfo[currentRoom]:
            currentRoom = roominfo[currentRoom][move[1]]
            print(currentRoom)
            if currentRoom == "South_wing" :
                print('the Hall is north of the South_wing')

            elif currentRoom == "Secret_doorway" :  
                if 'key' in inventory:
                    print(
                    "================================================================================================================================================================= \n"
                    "You have suddenly found yourself in a crypt and the door quickly snaps shut behind you.It is pitch dark and drafty. \n"
                    "================================================================================================================================================================= " )
                    if 'lantern' in inventory:
                        S = threading.Timer(15.0, decision)
                        print(
                        "================================================================================================================================================================= \n"
                        "luckily you snagged a lantern from the south wing. you turn your latern on and as the light brightens the room, you notice 3 distinctly marked statues. \n "
                        '3 figures are arranged carefully against the crypt\'s interior wall. They are marked boldly with the numbers 6 7 2 respectively. You now have 15 seconds to \n'
                        'figure out the combinations and escape before you suffocate \n'
                        "================================================================================================================================================================= \n")
                        S.start()
                        move = input('>')
                        if move == '276':
                            S.cancel()
                            inventory += ['golden_orb']
                            del roominfo[currentRoom]['item']
                            print("THE GODS ARE WITH YOU! They have bestowed on you the golden_orb with which to banish Ekwensu. You live to fight another day warrior")

                        else:
                            decision()
                        # os._exit will FORCE the program to end!    
                    else:
                        print( "================================================================================================================================================================= \n"
                            'You have entered the crypt with no lantern to see around. You could not find the statues that would give you th ecode to the booby trap. You are crushed. GAME OVER!!! \n'
                            "=================================================================================================================================================================")
                        os._exit(os.EX_OK)             
                else:
                    print('You cannot go that way. You need a key')
                continue
            elif currentRoom == "East_wing" :
                if 'Ekwensu' in roominfo[currentRoom]['item'] and "golden_orb" in inventory:
                    print('You entered the room Ekwensu dwells in. You have the golden orb in your possession. Ala has granted you the power to seal Ekwensu away in her womb forever... \n'
                    'Thank you for your service Warrior, YOU WIN!')
                    os._exit(os.EX_OK)
                elif 'Ekwensu' in roominfo[currentRoom]['item'] and "golden_orb" not in inventory:  
                    print('You entered the room Ekwensu dwells in. You do not have the golden orb with you. You cannot defeat the tricky Ekwensu without the power of Ala. You have failed this \n'
                    'time Warrior. GAME OVER!!')
                    os._exit(os.EX_OK)
            else:
                print("You cannot go " + move[1] + '!')
    
        
    ## Define how a player can win
    if currentRoom == 'Grove_mouth' and 'key' in inventory:
        print('You have succeeded in vanquising the evil mascqurade Ekwensu and discovered the ULTRA RARE telepotion... YOU WIN!')
        break
    