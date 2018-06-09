import random
# Attribute Critter
# Demonstrates creating and accessing object attributes

class Critter(object):
    """A virtual pet"""
    total = 0
    
    def status():
        print "\nThe total number of critters is", Critter.total 
        
    status = staticmethod(status)
    
    def __init__(self, name):
        print "A new critter has been born!"
        self.name = name
        self.__health = 100
        self.__sleep = 0
        self.__hunger = 50


    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"
        rep += "Health: " + str(self.__health) + "\n"
        rep += "Eat: " + str(self.__hunger) + "\n"
        rep += "Sleep: " + str(self.__sleep) + "\n"
        return rep

    def __cmp__(self, other):
        print "BATTLE"
        winner = random.randrange(2)
        if winner == 1:
            return 1
        else:
            return 0
    def name(self):
        return self.name
    
    def win(self):
        print self.name, "wins"
        self.changeHealth(10)
        self.changeHunger(-10)
        
    def lose(self):
        print self.name,"loses"
        self.changeHealth(-10)
        self.changeHunger(-10)
        self.__sleep+=1
        
    def eat(self):
        food = random.randrange(4)
        if(food == 3):
            print "ROTTEN FOOD"
            self.changeHealth(-10)
        elif(food == 2):
            print "YUMMY FOOD"
            self.changeHealth(10)
            self.changeHunger(10)            
        else:
            print "RATIONS"
            self.changeHunger(15)
        print "Eat"

    def sleep(self):
        self.__sleep = 0


    def changeHunger(self,amount):
        self.__hunger += amount
        if(self.__hunger > 100):
            self.__hunger = 100

            
    def changeHealth(self,amount):
        self.__health += amount
        if(self.__health > 100):
            self.__health = 100

    def endTurn(self):
        self.__sleep += 1
        if(self.__sleep > 5):
            self.changeHealth(-10)
        else:
            self.changeHealth(10)
            self.changeHunger(10)
        
    def isAlive(self):
        if(self.__health <= 0):
            return 0
        if(self.__hunger <= 0):
            return 0
        return 1
    
def other(value):
    if(value == 0):
        return 1
    else:
        return 0
    
#main
def main():
    crit = (Critter("Armaan"),Critter("Teja"))
    print "Crit1:", crit[0]
    print "Crit2:",crit[1]
    turns = 0
    whichCritter = turns
    while(crit[whichCritter].isAlive()):
        print "What would", crit[whichCritter].name,"like to do?"
        choice = raw_input("Eat? Sleep? or Battle?")
        if(choice.strip().lower() == "battle"):                
            if(crit[whichCritter] == crit[other(whichCritter)]):
                crit[whichCritter].win()
                crit[other(whichCritter)].lose()
            else:
                crit[whichCritter].lose()
                crit[other(whichCritter)].win()
        elif(choice.strip().lower() == "sleep"):
            crit[whichCritter].sleep()
        elif(choice.strip().lower() == "eat"):
            crit[whichCritter].eat()
            
        crit[whichCritter].endTurn()
        print "Crit1:", crit[0]
        print "Crit2:",crit[1]
        raw_input("\n\nPress the enter key to advance.")
        whichCritter = other(whichCritter)

    if(crit[0].isAlive()):
        print crit[0], "Survived"
    else:
        print crit[0], "DIED"
        
    if(crit[1].isAlive()):
        print crit[1], "Survived"
    else:
        print crit[1], "DIED"
    

main()
raw_input("\n\nPress the enter key to exit.")



