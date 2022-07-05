import mygame01

move = move[0]
cmd = move[1]


def condition():
    if move == 'get' and cmd == 'key' :
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('you have collected a ' + move[1])

            #delete the item from the room
            del rooms[currentRoom]['item']

        

    elif move == 'get' and cmd == 'map':
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

    elif move == 'get' and cmd == 'lantern':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:        


    #else:
        # move == 'get' and cmd == 'telepotion':
        # if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:   