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
import os

class Caves:
    roomnumber
    exit1
    exit2
    exit3
    warning
    
    Caves():
        roomnumber=exit1=exit2=exit3=0
        warning=""
    Caves(w,rn,e1,e2,e3):
        warning=w
        roomnumber=rn
        exit1=e1
        exit2=e2
        exit3=e3
    extra
    caves(cin = raw_input(""):
        roomnumber = cin.next()
        exit1 = cin.next()
        exit2 = cin.next()
        exit3 = cin.next()
        extra = cin.next()
        warning = cin.next()
    toString():
        return roomnumber + " ", exit1, " ", exit2, " ", warning
    
    getRoomNumber():
        return roomnumber
    getExit1():
        return exit1
    getExit2():
        return exit2
    getExit3():
        return exit3
    getWarning():
        return warning