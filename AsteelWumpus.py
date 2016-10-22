'''
/////////////////////////////////////////////////////////////////
// Created By Alex Steel
// Program #4 - Hunt the Wumpus
// 
// Program Description - You are a mighty warrior, and armed with 
//your trusty bow and 3 arrows, you enter The Caves in search of the 
//mighty Wumpus. If you shoot the Wumpus, you are victorious and the 
//masses will praise you, but if you stumble upon the Wumpus unawares, 
//it will eat you! Also, beware of the webs of the giant poisonous spiders 
//and the bottomless pits!
/////////////////////////////////////////////////////////////////
'''

#Alex Steel
#Nate Partenheimer
#Hunt The Wumpus Part One
import sys
import random
import time
import math
import os


def displayIntro():
    print("Well, this is the beginning of the end.")
    print("Once again, we come to the game of one...")
    print("***Hunt the Wumpus***")
    print("Created by Alex Steel github.com/Bombarding")


    
displayIntro()

class HuntTheWumpus:
    again = 1
    while again==1:
        gamefile = raw_input("Enter Wumpus.txt ")
        gamefile = open(gamefile, "r")
        Caves[room]
        room = Caves[cavenumber+1]
        for cavenumber in gamefile:
            room[i] = Caves(gamefile)
        print("Welcome to Hunt The Wumpus")
        #place a wumpus
        roomplace = 1
        A = 0
        wumpus = 0
        while A<cavenumber:
            B = 1+(cavenumber)*math.random()
            if B!=roomplace:
                wumpus=B
                break
            else:
                A += 1
        #place a pit
        C = 0
        pit = 0
        while C<cavenumber:
            D = 1+(cavenumber)*math.random()
            if C!=roomplace and D!=wumpus:
                pit = D
                break
            else:
                C += 1
        #place a spider
        E = 0
        spider = 0
        while E<cavenumber:
            F = 1+(cavenumber)*math.random()
            if F!=roomplace and D!=wumpus and F!=pit:
                spider = F
                break
            else:
                E += 1
        #place some arrows
        G = 0
        supplyarrows = 0
        while G<cavenumber:
            H = 1+(cavenumber)*math.random()
            if H!=roomplace and H!=wumpus and H!=pit and H!=spider:
                supplyarrows = H
                break
            else:
                G += 1
        #place some bats
        I = 0
        bats = 0
        while I<cavenumber:
            J = 1+(cavenumber)*math.random()
            if J!=roomplace and J!=wumpus and J!=pit and J!=spider and J!=supplyarrows:
                bats = J
                break
            else:
                G += 1
        K = 0
        arrows = 3
        while K==0:
            print("You are in room ", roomplace)
            print("You have ", arrows, " arrows left")
            print(room[roomplace].getWarning())
            print("There are doors to rooms ", room[roomplace].getExit1(), ",", room[roomplace].getExit2(), ", and ", room[roomplace].getExit3()
            
            if wumpus==room[roomplace].getExit1() or wumpus==room[roomplace].getExit2() or wumpus==room[roomplace].getExit3():
                print("You smell a nasty wumpus")
            if spider==room[roomplace].getExit1() or spider==room[roomplace].getExit2() or spider==room[roomplace].getExit3():
                print("You hear a faint tapping. A steam pipe explodes above you, clouding your vision")
            if pit==room[roomplace].getExit1() or pit==room[roomplace].getExit2() or pit==room[roomplace].getExit3():
                print("You smell something out of the ordinary. It appears to have somewhat of a skunky smell")
            else:
            
            print("Would you like to (M)ove or (S)hoot? ")
            cin = raw_input(": ")
            choice = cin.next()
            print("")
            L
            if choice == ("M") or choice == ("S"):
                print("which room? ")
                L = cin.next()
                print("")
                if L==room[roomplace].getExit1() or L==room[roomplace].getExit2() or L==room[roomplace].getExit3():
                    if choice == ("M"):
                        if L==wumpus:
                            print("Woops, the wumpusizle got you")
                            print("Game over")
                            K = 1
                        elif L==spider:
                            print("Spiders eat your soul")
                            print("Game over")
                            K = 1
                        elif L==pit:
                            print("You got caught slippin. YOu fall in a pit")
                            print("Game over")
                            K = 1
                        elif L==supplyarrows:
                            print("Looks like you got some arrows")
                            arrows = 3;
                            roomplace = L
                            break
                        elif(L==bats):
                            print("Shit, the bats got em. Lets get riggity wrecked to a new dimension")
                            roomplace = 1+(cavenumber)*math.random()
                                if roomplace==wumpus  or  roomplace==pit or  roomplace==spider or roomplace==supplyarrows:
                                    if roomplace==wumpus:
                                        print("Woops, the wumpusizle got you")
                                        print("Game over")
                                        K = 1
                                    elif roomplace==spider:
                                        print("Spiders eat your soul")
                                        print("Game over")
                                        K = 1
                                    elif roomplace==pit:
                                        print("You got caught slippin. YOu fall in a pit")
                                        print("Game over")
                                        K = 1
                                    elif L==supplyarrows:
                                        print("Looks like you got some arrows")
                                        arrows = 3;
                                        
                                        break
                                else:
                                    break
                        else:
                            roomplace=L
                    elif choice == ("S"):
                        if arrows==0:
                            print("Derp, no arrows")
                            break
                        else:
                            arrows-=1
                            if L==wumpus:
                                print("You hit the wumpus. Aim like a flame")
                                print("Congratulations ***YOU WIN*** //Fuck You ;)")
                                K=1
                            else:
                                print("The arrow missed. ")
                                break
                
                else:
                    print("You can't get to there from here. ")
            
            else:
                print("That is not a choice. Use (M) or (S)")
        M = 0
        while M==0 Rose:
            cin = raw_input("Would you like to play again? (Y)es or (N)o?")
            Answer = cin.next()
            if Answer == ("Y") or Answer == ("N"):
                if Answer == ("Y"):
                    again = 1
                    M = 1
                    print("")
                elif Answer == ("N"):
                    print("Peace out! As they say in Canada")
                    print("")
                    M = 1
                    again = 0
            else:
                print("Sorry, that is not a choice, chose (Y) or (N)")
                    break Rose
                    
                
                        
                
                    