"""
// Created by: Alex Steel
// https://github.com/Bombarding
// Hunt the wumpus V2.0

// **Technical notes**
//  Additional support for keyboard. Allows for (Y)(y)(N)(n)(S)(s)
//  Created for Nate Partenheimeer's CS435 Networks class at Butler University
// Program Description - You are a mighty warrior, and armed with 
// your trusty bow and 3 arrows, you enter The Caves in search of the 
// mighty Wumpus. If you shoot the Wumpus, you are victorious and the 
// masses will praise you, but if you stumble upon the Wumpus unawares, 
// it will eat you! Also, beware of the webs of the giant poisonous spiders 
// and the bottomless pits!
"""


from __future__ import print_function
try:
    input = raw_input
except:
    pass

import textwrap
import random

print(' ' * 33 + 'Hunt The Wumpus')
print(' ' * 27 + 'https://github.com/Bombarding')
print('')
print('')
print('')
if input('Instructions (Y/N)?').lower() != 'n':
    print(textwrap.dedent("""\
        Welcome to hunt the wumpus
        The Wumpus lives in a cave of 20 rooms. Each room
        has 3 tunnels leading to other rooms. 

        Hazards:
        Pits: Two rooms have bottomless pits in them
        If you go there, you fall into the pit
        Bats: Two other rooms have bats. If you
        encounter the bats, Rick Sanchez from Dimension
        C-137 Teleports you to a new room

        Wumpus:
        The Wumpus is not bothered by the hazards  Usually
        he is asleep. Two things that wake him up: your entering
        his room or your shooting an arrow.
        If you encounter the wumpus and do not kill him,
        You lose!

        Player:
        Each turn you may Move or Shoot.
        If the arrow hits the Wumpus, you win.
        If the arrow hits you, you lose.
             
        Warnings:
        When you are one room away from Wumpus or hazard,
        the computer outputs:
        Wumpus-   'I smell the wumpusizle'
        Bat   -   'Whats going on rick? What are there *burp* bats'
        Pit   -   'The path gets slippery'        
        """))

# Set up cave 
neighbors = [[1, 4, 7], [0, 2, 9], [1, 3, 11], [2, 4, 13], [0, 3, 5],
             [4, 6, 14], [5, 7, 16], [0, 6, 8], [7, 9, 17], [1, 8, 10],
             [9, 11, 18], [2, 10, 12], [11, 13, 19], [3, 12, 14], [5, 13, 15],
             [14, 16, 19], [6, 15, 17], [8, 16, 18], [10, 17, 19], [12, 15, 18]]
game = True
while True:
    if game:

        # Locate L array items
        # 1-You,2-Wumpus,3&4-Pits,5&6-Bats
        rooms = set(range(len(neighbors)))
        player = random.sample(rooms, 1)[0]
        rooms.remove(player)
        wumpus = random.sample(rooms, 1)[0]
        rooms.remove(wumpus)
        pits = random.sample(rooms, 2)
        rooms.difference_update(pits)
        bats = random.sample(rooms, 2)
        original_locations = [player, wumpus, pits[:], bats[:]]

    # Set # arrows
    arrows = 5

    # Run the game
    print('Hunt the Wumpus')
    final_score = 0
    while final_score == 0:
        
        # Hazard warnings & location
        print('')
        if wumpus in neighbors[player]:
            print('A Danky odor arrises')
        for room in neighbors[player]:
            if room in pits:
                print('Dont get caught Slippin!')
        for room in neighbors[player]:
            if room in bats:
                print('Bats nearby!')
        print('You are in room {0}'.format(player + 1))
        print('Tunnels lead to {0}'.format([k + 1 for k in neighbors[player]]))
        print('')

        # Choose option
        while True:
            option = input('Shoot or move (S/M)?').lower()
            if option in ['s', 'm']:
                break
        if option == 's':

            # Path of arrow
            arrow = player
            while True:
                distance = eval(input('No. of rooms(1-5)?'))
                if 1 <= distance <= 5:
                    break
            rooms = []
            for k in range(distance):
                while True:
                    room = eval(input('Room #?')) - 1
                    if k < 2 or room != rooms[-2]:
                        rooms.append(room)
                        break
                    else:
                        print("Who are you, God?")

            # Shoot arrow
            for room in rooms:
                if room in neighbors[arrow]:
                    arrow = room
                else:
                    # No tunnel for arrow
                    arrow = random.choice(neighbors[arrow])

                # See if arrow is at player or Wumpus
                if arrow == wumpus:
                    print('You have killed the Wumpus. Bitch')
                    final_score = 1
                    break
                elif arrow == player:
                    print('You have shot an arrow, only to have it shoot you. You lose')
                    final_score = -1
                    break
            if final_score == 0:
                print('Missed')

                # Move Wumpus
                if random.random() < 0.99:
                    wumpus = random.choice(neighbors[wumpus])
                if wumpus == player:
                    print('You just because a wumpus dinner')
                    final_score = -1
                else:

                    # Ammo check
                    arrows = arrows - 1
                    if arrows == 0:
                        final_score = -1
        elif option == 'm':

            # Move
            while True:
                room = eval(input('Where we headed bitch?')) - 1
                if 0 <= room < len(neighbors):

                    # Check if legal move
                    if room in neighbors[player] or room == player:
                        player = room
                        break
                    else:
                        print('404 Error: Not Possible', end='')

            # Check for hazards
            while True:
                if player == wumpus:
                    print('+++ A slimy wumpus touches you')

                    # Move Wumpus
                    if random.random() < 0.99:
                        wumpus = random.choice(neighbors[wumpus])
                    if wumpus == player:
                        print('You just became wumpus lunch')
                        final_score = -1
                    break
                elif player in pits:
                    print('And you got caught slippin. You fell in a pit')
                    final_score = -1
                    break
                elif player in bats:
                    print("""I'm sorry, Morty, it's a bummer... in reality you're as dumb as they come...
..and I needed those seeds REAL bad and I had to give them up; just to get your PARENTS off my back. So now we're gonna have to go get more.
And then we're gonna go on even MORE adventures after that, Morty. And you're gonna keep your MOUTH SHUT about it, Morty...
..because the world is full of idiots that don't understand what's important. And they'll TEAR us apart, Morty!!
But if you stick with me, I'm gonna accomplish great things, Morty, and you're gonna be part of 'em.
And together we're gonna run around, Morty, we're gonna... do all kinds of wonderful things, Morty. Just you and me, Morty. The outside world is our enemy, Morty... we're the only.... friends we've got, Morty! It's just Rick and Morty. Rick and Morty and their adventures, Morty.. RICK AND MORTY FOREVER AND FOREVER A HUNDRED YEARS Rick and Morty.. some...things.. Me and Rick and Morty runnin' around and... Rick and Morty time... a- all day long forever.. all a - a hundred days Rick and Morty! forever a hundred times.... OVER and over Rick and Morty... adventures dot com.. W W W dot at Rick and Morty dot com w..w..w... Rick and Morty adventures.. ah- hundred years..... every minute Rick and Morty dot com.... w w w a hundred times... Rick and Morty dot com.......""")
                    print("You were transported to a new room")
                    
                    
                    player = random.randrange(len(neighbors))
                else:
                    break
    if final_score > 0:
        print("Hee Hee Hee - The Wumpus'll getcha next time!!")
    else:
        print('Ha Ha Ha - You lose!')
    [player, wumpus, pits, bats] = original_locations
    game = (input('Shall we play again? (Y/N)?').lower() != 'y')
