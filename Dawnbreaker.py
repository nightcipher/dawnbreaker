#Dawnbreaker V 1.0
#By Nate Stonecipher
#Written 4-20-2016

import random
import pickle

textBlocks = open('TextBlocks.bin','rb')
raceMenu = pickle.load(textBlocks)
angelDesc = pickle.load(textBlocks)
aasimarDesc = pickle.load(textBlocks)
exaltedDesc = pickle.load(textBlocks)
classMenu = pickle.load(textBlocks)
knightDesc = pickle.load(textBlocks)
monkDesc = pickle.load(textBlocks)
wardenDesc = pickle.load(textBlocks)
actionMenu = pickle.load(textBlocks)
textBlocks.close()

class Player(object):
    def __init__(self, name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0,):
        self.name = name
        self.gender = gender
        self.race = race
        self.playerClass = playerClass
        self.hp = hp
        self.dam = dam
        self.dex = dex
        self.agi = agi
        self.isGod = isGod
    def __str__(self):
    	result = ""
    	result += self.name + " the " + self.gender + " " + self.race + " " + self.playerClass
    	result += "\nHP: " + str(self.hp) + "\nSTR: " + str(self.dam) + "\nDEX: " + str(self.dex) + "\nAGI: " + str(self.agi)
    	return result
    def attack(self, target):
        #roll to hit
        attackMod = random.randrange(1,10)
        defendMod = random.randrange(1,10)

        if self.dex * attackMod > target.agi * defendMod:
            print("Hit!")
            target.hp -= self.dam
            print(target.hp)
        else:
            print("Miss!")
        
class Knight(Player):
    #Solar Knight player class.
    def __init__(self,  name, gender, race, playerClass, hp, dam, dex, agi):
        super(Knight, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi)
        if race == "Angel":
            self.hp = 15
            self.dam = 7
            self.agi = 10
            self.dex = 5
        if race == "Aasimar":
            self.hp = 20
            self.dam = 6
            self.agi = 5
            self.dex = 8
        if race == "Exalted Mortal":
            self.hp = 10
            self.dam = 6
            self.agi = 7
            self.dex = 10

    def passive(self):
        pass
        #Static racial ability code goes here
    def active(self, target):
        pass
        #Special attacks go here

class Monk(Player):
    #Ember Monk player class.
    def __init__(self,  name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0):
        super(Monk, self).__init__(name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0)
        if race == "Angel":
            self.hp = 15
            self.dam = 7
            self.agi = 10
            self.dex = 5
        if race == "Aasimar":
            self.hp = 20
            self.dam = 6
            self.agi = 5
            self.dex = 8
        if race == "Exalted Mortal":
            self.hp = 10
            self.dam = 6
            self.agi = 7
            self.dex = 10
            
class Warden(Player):
    #Aurora Warden player class.
    def __init__(self,  name, gender, race, playerClass, hp, dam, dex, agi):
        super(Warden, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi)
        if race == "Angel":
            self.hp = 15
            self.dam = 7
            self.agi = 10
            self.dex = 5
        if race == "Aasimar":
            self.hp = 20
            self.dam = 6
            self.agi = 5
            self.dex = 8
        if race == "Exalted Mortal":
            self.hp = 10
            self.dam = 6
            self.agi = 7
            self.dex = 10

class God(Player):
    #Developer hack class.
    def __init__(self,  name, gender, race, playerClass, hp, dam, dex, agi):
        super(Warden, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi)
        if race == "Angel":
            self.hp = 1000000000000
            self.dam = 1000
            self.agi = 1000
            self.dex = 1000
        if race == "Aasimar":
            self.hp = 1000000000000
            self.dam = 1000
            self.agi = 1000
            self.dex = 1000
        if race == "Exalted Mortal":
            self.hp = 1000000000000
            self.dam = 1000
            self.agi = 1000
            self.dex = 1000

class Map(object):

    def __init__(self, size = 5, charX = 0, charY = 0):

        self.charX = charX
        self.charY = charY
        self.size = size
        self.grid = []

        for x in range(size):
            self.grid.append([])

        for x in self.grid:
            for y in range(size):
                x.append("-")
                #placeholder until tile objects are used
        self.grid[charX][charY] = 'X'

    def __str__(self):
        result = ""
        for x in range(self.size):
            for y in range(self.size):
                result += self.grid[x][y]
            result += "\n"
        return result

    def tileCheck(self, x, y):
        badTerrain = ('~', '#')
        if x == self.size or y == self.size:
            print("Out of bounds!")
            return False
        elif x < 0 or y < 0:
            print("Out of bounds!")
            return False
        elif self.grid[x][y] in badTerrain:
            print("You can't go that way!")
            return False
        else:
            return True

    def setTerrain(self, x, y, newTerrain):
        TERRAIN = ('-','~','#','!','@')
        if newTerrain in TERRAIN:
            self.grid[x][y] = newTerrain
        else:
            print("Error! That's not valid terrain.")
        #TODO: Use this function to generate actual terrain on map
        #TODO: Write function for an enemy-occupied tile with a hidden identity
        #Hidden identity = tile that looks normal on map

    def hideEnemies(self):
        hiddenMap = self.grid
        for n in hiddenMap:
            if n == '~':
                n = '-'
        result = ""
        for x in range(self.size):
            for y in range(self.size):
                tile = hiddenMap[x][y]
                if tile == '~':
                    tile = '-'
                    result += tile
                else:
                    result += tile
            result += "\n"
        return result

    def move(self, direction):
        if direction == 4:
            #Move West
            if self.tileCheck(self.charX, self.charY - 1):
                self.grid[self.charX][self.charY] = "-"
                self.charY -= 1
                self.grid[self.charX][self.charY] = "X"
        elif direction == 3:
            #Move East
            if self.tileCheck(self.charX, self.charY + 1):
                self.grid[self.charX][self.charY] = "-"
                self.charY += 1
                self.grid[self.charX][self.charY] = "X"
        elif direction == 2:
            #Move South
            if self.tileCheck(self.charX + 1, self.charY):
                self.grid[self.charX][self.charY] = "-"
                self.charX += 1
                self.grid[self.charX][self.charY] = "X"
        elif direction == 1:
            #Move North
            if self.tileCheck(self.charX - 1, self.charY):
                self.grid[self.charX][self.charY] = "-"
                self.charX -= 1
                self.grid[self.charX][self.charY] = "X"
        else:
            print("You didn't give me a cardinal direction!")

        
def createChar():
    '''Returns a Player object of the chosen special class.
    If not confirmed at the end of the function, returns None.'''

    finished = False
    while not finished:
        choice = input = ("Developer hack: Do you need god-mode to clear the game faster?\n [Y/N]")
        if choice.lower() == 'y':
            needJesus = True
        else:
            needJesus = False
            
    finished = False
    while not finished:
        #Generate Menu
        print("Approach the mirror, adventurer. Who do you see reflected in its depths?")
        print(raceMenu)
        choice = int(input("What race are you? [1,2,3]"))
        if choice == 1:
            #Angel
            print(angelDesc)
            confirm = input("You are an Angel? [Y/N]")
            if confirm.lower() == "y":
                charRace = "Angel"
                finished = True
        elif choice == 2:
            #Aasimar
            print(aasimarDesc)
            confirm = input("You are an Aasimar? [Y/N]")
            if confirm.lower() == "y":
                charRace = "Aasimar"
                finished = True
        elif choice == 3:
            #Exalted Mortal
            print(exaltedDesc)
            confirm = input("You are an Exalted Mortal? [Y/N]")
            if confirm.lower() == "y":
                charRace = "Exalted Mortal"
                finished =  True
        else:
            print("You can't choose that! Try again.")
    finished = False
    print("Very well. You are an " + charRace + ".")
    while not finished:
        print(classMenu)
        choice = int(input("What were you trained as? [1,2,3]"))
        if choice == 1:
            #Solar Knight
            print(knightDesc)
            confirm = input("So you are a Solar Knight? [Y/N]")
            if confirm.lower() == "y":                
                charClass = "Solar Knight"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 2:
            #Ember Monk
            print(monkDesc)
            confirm = input("So you are an Ember Monk? [Y/N]")
            if confirm.lower() == "y":                
                charClass = "Ember Monk"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 3:
            #Aurora Warden
            print(wardenDesc)
            confirm = input("So you are an Aurora Warden? [Y/N]")
            if confirm.lower() == "y":                
                charClass = "Aurora Warden"
                finished = True
            else:
                print("Let's try this again.")
        else:
            print("You can't choose that! Try again.")
    finished = False
    print("A fine profession.")
    while not finished:
        charName = input("How about your name? What are you called?")
        confirm = input("So you are called " + charName + "? [Y/N]")
        if confirm.lower() == "y":                
            finished = True
        else:
            print("Let's try this again.")
        
    finished = False
    while not finished:
        print("What gender are you, and what pronouns do you go by?")
        choice = int(input("You may choose from: \n[1] Male - 'He, Him'\n[2] Female - 'She, Her'\n[3] Nonbinary - 'They, Them'"))
        if choice == 1:
            #Male Gender
            confirm = input("So you identify as male? [Y/N]")
            if confirm.lower() == "y":                
                charGender = "Male"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 2:
            #Female Gender
            confirm = input("So you identify as female? [Y/N]")
            if confirm.lower() == "y":                
                charGender = "Female"
                finished = True
            else:
                print("Let's try this again.")
        elif choice == 3:
            #Nonbinary Gender
            confirm = input("So you identify as nonbinary? [Y/N]")
            if confirm.lower() == "y":                
                charGender = "Nonbinary"
                finished = True
            else:
                print("Let's try this again.")
        else:
            print("You can't choose that! Try again.")
            
    print("You've finished telling me about yourself. \nYou are " + charName + ", the " + charGender + " " + charRace + " " + charClass + ".")
    if needJesus:
        print("You're also using the developer cheat.")
    confirm = input("Is all that correct? if it isn't, we have to start all over. [Y/N]")
    if confirm.lower() == "y":
        if needJesus:
            charClass == "God"
            player = God(charName, charGender, charRace, charClass)
            return player
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

def combat():
    turn = 0
    stillFighting = True
    while stillFighting:
        turn += 1
        #Call racial passive here
        #Player turn begins
        print(actionMenu)
        action = int(input("\nWhat would you like to do?\n"))
        while action not in (1,2,3,4):
            print(actionMenu)
            action = int(input("\nWhat would you like to do?\n"))
        if action == 1:
            player.attack(enemy)
        if action == 2:
            pass
        if action == 3:
            pass
        if action ==4:
            difficulty = random.randrange(1,10)
            if player.agi * 10 > difficulty * 10:
                print("You ran away!")
                stillFighting = False
                ranAway = True
            else:
                print("You couldn't get away!")
        #Enemy turn
        if enemy.hp > 0:
            enemy.attack(player)
        elif player.hp <= 0:
            print("You died! Game over.")
            stillFighting = False
            playerDied = True
        else:
            print("You defeated the " + enemy.name + "!")
            stillFighting = False
            enemyDied = True
        
        
    
def mapMove():
    moving = True
    
    while moving:
        print("Which way woul you like to go?")
        choice = input("1 - North | 2 - South | 3 - East | 4 - West\n")
        if choice == 1:
            theMap.move(choice)
            moving = False
        elif choice == 2:
            theMap.move(choice)
            moving = False
        elif choice == 3:
            theMap.move(choice)
            moving = False
        elif choice == 4:
            theMap.move(choice)
            moving = False
        else:
            print("That wasn't a valid choice.")
            theMap.move(choice)

    resolving = True

    while resolving:
        #check terrain to see what event occurs
        if theMap.grid[theMap.charX][theMap.charY] == '~':
            seed = random.randrange(1, 3)
            #initiate combat
            if seed == 1:
                enemy = devil
                combat()
            elif seed == 2:
                enemy = lesserFiend
                combat()
        
    
        
def main():
    #Generate Player
    player = None
    while player == None:
        player = createChar()
        print(player)
    
    #Generate enemies
    lesserFiend = Player("Lesser Fiend", "Male", "Demon", "Grunt", 15, 5, 5, 2)
    fiendLord = Player("Fiend Lord", "Male", "Demon", "Boss", 30, 7, 6, 1)
    devil = Player("Devil", "Male", "Demon", "Cannon Fodder", 5, 3, 10, 4)
    
    print("The temple lies to the south, marked by the @ symbol.")
    theMap = Map()
    theMap.setTerrain(3, 4, '@')
    theMap.setTerrain(2, 2, '~')
    print(theMap)
    theMap.move(2)
main()
