#Dawnbreaker V 1.0
#By Nate Stonecipher
#Written 4-20-2016

import random
raceMenu = '''
|=========================|
|=== Choose Your Race ====|
|=========================|
|                         |
|1) Angel                 |
|                         |
|2) Aasimar               |
|                         |
|3) Exalted Mortal        |
|                         |
|=========================|
|=========================|
|=========================|
'''
classMenu = '''
|=========================|
|=== Choose Your Class ===|
|=========================|
|                         |
|1) Solar Knight          |
|                         |
|2) Ember Monk            |
|                         |
|3) Aurora Warden         |
|                         |
|=========================|
|=========================|
|=========================|
'''
class Player(object):
    def __init__(self, name, gender, race, playerClass, hp, dam, dex, agi):
        self.name = name
        self.gender = gender
        self.race = race
        self.playerClass = playerClass
        self.hp = hp
        self.dam = dam
        self.dex = dex
        sef.agi = agi
    def __str__(self):
    	result = ""
    	result += self.name + " the " + self.gender + " " + self.race + " " + self.playerClass
    	return result
    def attack(self, target):
        #roll to hit
        playerMod = random.randrange(1,10)
        enemyMod = random.randrange(1,10)
        
        
    
class Monk(Player):
    #Ember Monk player class.
    def __init__(self,  name, gender, race, playerClass, hp, dam, dex, agi):
        super(Monk, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi)
        
class Knight(Player):
    #Solar Knight player class.
    def __init__(self,  name, gender, race, playerClass, hp, dam, dex, agi):
        super(Knight, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi)
        
class Warden(Player):
    #Aurora Warden player class.
    def __init__(self,  name, gender, race, playerClass, hp, dam, dex, agi):
        super(Warden, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi)
        
        
def createChar():
    '''Returns a Player object of the chosen special class.
    If not confirmed at the end of the function, returns None.'''
    finished = False
    while not finished:
        #Generate Menu
        print("Approach the mirror, adventurer. Who do you see reflected in its depths?")
        print(raceMenu)
        #TODO: Import long descriptions from external file
        choice = int(input("What race are you? [1,2,3]"))
        if choice == 1:
            #Angel
            charRace = "Angel"
            finished = True
        elif choice == 2:
            #Aasimar
            charRace = "Aasimar"
            finished = True
        elif choice == 3:
            #Blessed Mortal
            charRace = "Exalted Mortal"
            finished =  True
        else:
            print("You can't choose that! Try again.")
    finished = False
    print("Very well. You are an", charRace, ".")
    while not finished:
        print(classMenu)
        #TODO: Import long descriptions from external file
        choice = input("What were you trained as? [1,2,3]")
        if choice == 1:
            #Solar Knight
            confirm = input("So you are a Solar Knight? [Y/N]")
            if confirm.lower() = y:                
                charClass = "Solar Knight"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 2:
            #Ember Monk
            confirm = input("So you are an Ember Monk? [Y/N]")
            if confirm.lower() = y:                
                charClass = "Ember Monk"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 3:
            #Aurora Warden
            confirm = input("So you are an Aurora Warden? [Y/N]")
            if confirm.lower() = y:                
                charClass = "Aurora Warden"
                finished = True
            else:
                print("Let's try this again.")
        else:
            print("You can't choose that! Try again.")
    finished = False
    print("Ah, trained in the ways of the", charClass, ".")
    while not finished:
        charName = input("How about your name? What are you called?")
        confirm = input("So you are called", charName, "? [Y/N]")
        if confirm.lower() = y:                
            finished = True
        else:
            print("Let's try this again.")
        
    finished = False
    while not finished:
        print("What gender are you, and what pronouns do you go by?")
        choice = input("You may choose from: \n[1] Male - 'He, Him'\n[2] Female - 'She, Her'\n[3] Nonbinary - 'They, Them'")
        if choice == 1:
            #Male Gender
            confirm = input("So you identify as male? [Y/N]")
            if confirm.lower() = y:                
                charGender = "Male"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 2:
            #Female Gender
            confirm = input("So you identify as female? [Y/N]")
            if confirm.lower() = y:                
                charGender = "Female"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 3:
            #Nonbinary Gender
            confirm = input("So you identify as nonbinary? [Y/N]")
            if confirm.lower() = y:                
                charGender = "Nonbinary"
                finished = True
            else:
                print("Let's try this again.")
        else:
            print("You can't choose that! Try again.")
    print("You've finished telling me about yourself. You are:", charName, "the", charGender, " ", charRace, " ", charClass)
    confirm = input("Is all that right? if it isn't, we have to start all over. [Y/N]")
            if confirm.lower() = y:                
                if charClass == "Solar Knight":
                    player = Knight(charName, charGender, charRace, charClass)
                    return player
                elif charClass == "Ember Monk":
                    player = Monk(charName, charGender, charRace, charClass)
                    return player
                elif charClass =="Aurora Warden":
                    player = Warden(charName, charGender, charRace, charClass)
                    return player
            else:
                print("We will begin again, then.")
                return None
def main():
    player = None
    while player == None:
        player = createChar()
