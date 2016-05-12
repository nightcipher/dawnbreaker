#Dawnbreaker V 1.0
#By Nate Stonecipher
#Written 4-20-2016

import random
import pickle
import sys

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

class Entity(object):
    def __init__(self, name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0, fullHealth = 20):
        self.name = name
        self.gender = gender
        self.race = race
        self.playerClass = playerClass
        self.hp = hp
        self.dam = dam
        self.dex = dex
        self.agi = agi
        self.fullHealth = fullHealth
    def __str__(self):
    	result = ""
    	result += self.name + " the " + self.gender + " " + self.race + " " + self.playerClass
    	result += "\nHP: " + str(self.hp) + "\nSTR: " + str(self.dam) + "\nDEX: " + str(self.dex) + "\nAGI: " + str(self.agi)
    	return result
    def attack(self, target):
        #roll to hit
        attackMod = random.randrange(1,11)
        defendMod = random.randrange(1,11)

        if attackMod == 10 and defendMod != 10:
            if self.race == "Exalted Mortal":
                print("Rancor critical hit!")
                target.hp -= self.dam * 4
            else:
                print("Attacker critical hit!")
                target.hp -= self.dam * 2
            
        elif defendMod == 10:
            if target.race == "Exalted Mortal":
                print("Rancor counterstrike!")
                self.hp -= target.dam * 2
            else:
                print("Defender counterstrike!")
                self.hp -= target.dam
            
        elif self.dex * attackMod > target.agi * defendMod:
            print("Attacker hit!")
            target.hp -= self.dam
            
        else:
            print("Attacker miss!")
            
        
class Knight(Entity):
    #Solar Knight player class.
    def __init__(self,  name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0, fullHealth = 20):
        super(Knight, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi, fullHealth)
        if race == "Angel":
            self.hp = 25
            self.dam = 7
            self.agi = 10
            self.dex = 5
            self.fullHealth = 25
        #Static racial ability code goes here
        elif race == "Aasimar":
            self.hp = 30
            self.dam = 6
            self.agi = 5
            self.dex = 8
            self.fullHealth = 30
        #Static racial ability code goes here
        elif race == "Exalted Mortal":
            self.hp = 20
            self.dam = 5
            self.agi = 7
            self.dex = 10
            self.fullHealth = 20
        elif race == "God":
            self.hp = 1000000000000
            self.dam = 1000
            self.agi = 1000
            self.dex = 1000

    def passive(self, target):
        if self.race == "Angel":
            #Radiance: Deals damage each turn
            target.hp -= 3
            print("Radiance burns your foe!")
            print("Enemy has " + str(target.hp) + " remaining!")
        if self.race == "Aasimar":
            #Rejuvenation: Restores HP each turn
            self.hp += random.randrange(1,6)
            print("Your divine blood heals your wounds!")
            print("Your health is now:", self.hp)
        if self.race == "Exalted Mortal":
            print("Your blessing makes your strikes hit harder!")
            
    def primarySpecial(self, target):
        #Deliverance: Double attack, half hit chance
        attackMod = random.randrange(1,6)
        #Get a number 1-5 for calculating hit chance, half of normal hit chance
        defendMod = random.randrange(1,11)

        if attackMod == 5 and defendMod != 10:
            if self.race == "Exalted Mortal":
                print("Rancor critical hit!")
                target.hp -= self.dam * 8
            else:
                print("Attacker critical hit!")
                target.hp -= self.dam * 4
            
        elif defendMod == 10:
            print("Defender counterstrike!")
            self.hp -= target.dam

        elif self.dex * attackMod > target.agi * defendMod:
            print("Hit!")
            target.hp -= self.dam * 2

        else:
            print("Miss!")
            
        #First special attack
    def secondarySpecial(self, target):
        print("You smite your foe, stunning them!")
        target.hp -= self.dam / 2
        enemyStunned = True
        #Second special attack

class Monk(Entity):
    #Ember Monk player class.
    def __init__(self,  name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0, fullHealth = 30):
        super(Monk, self).__init__(name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0, fullHealth = 30)
        if race == "Angel":
            self.hp = 25
            self.dam = 7
            self.agi = 10
            self.dex = 5
            self.fullHealth = 25

        elif race == "Aasimar":
            self.hp = 30
            self.dam = 6
            self.agi = 5
            self.dex = 8
            self.fullHealth = 30
        elif race == "Exalted Mortal":
            self.hp = 20
            self.dam = 5
            self.agi = 7
            self.dex = 10
            self.fullHealth = 20
        elif race == "God":
            self.hp = 1000000000000
            self.dam = 1000
            self.agi = 1000
            self.dex = 1000

    def passive(self, target):
        if self.race == "Angel":
            #Radiance: Deals damage each turn
            target.hp -= 3
            print("Radiance burns your foe!")
            print("Enemy has " + str(target.hp) + " remaining!")
        if self.race == "Aasimar":
            #Rejuvenation: Heals each turn
            self.hp += random.randrange(1,6)
            print("Your divine blood heals your wounds!")
            print("Your health is now:", self.hp)
        if self.race == "Exalted Mortal":
            print("Your blessing makes your strikes hit harder!")


    def primarySpecial(self, target):
        #Radiant Flames: Ignites target for damage over time
        attackMod = random.randrange(1,11)
        defendMod = random.randrange(1,11)

        if attackMod == 10 and defendMod != 10:
            if self.race == "Exalted Mortal":
                print("Flames of intense rancor burn your foe!")
                target.hp -= self.dam * 2
                enemyAblaze = 8
                print("Enemy has " + str(target.hp) + " HP remaining!")

            else:
                print("Flames harshly scorch your foe!")
                target.hp -= self.dam
                enemyAblaze = 4
                print("Enemy has " + str(target.hp) + " HP remaining!")

            
        elif defendMod == 10:
            print("Defender counterstrike!")
            self.hp -= target.dam

        elif self.dex * attackMod > target.agi * defendMod:
            print("Flames scorch your foe!")
            target.hp -= self.dam / 2
            enemyAblaze = 3
            print("Enemy has " + str(target.hp) + " HP remaining!")

        else:
            print("Miss!")
            
    def secondarySpecial(self, target):
        #Raging Strikes: Hits multiple times at reduced damage
        print("You strike your foe rapidly!")
        numStrikes = random.randrange(2,6)
        for x in range(numStrikes):
            attackMod = random.randrange(1,11)
            defendMod = random.randrange(1,11)
            if self.dex * attackMod > target.agi * defendMod:
                target.hp -= self.dam / 2
                print("Enemy has " + str(target.hp) + " HP remaining!")

            
class Warden(Entity):
    #Aurora Warden player class.
    def __init__(self,  name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0, fullHealth = 30):
        super(Warden, self).__init__(name, gender, race, playerClass, hp, dam, dex, agi, fullHealth = 30)
        if race == "Angel":
            self.hp = 25
            self.dam = 7
            self.agi = 10
            self.dex = 5
            self.fullHealth = 25
        elif race == "Aasimar":
            self.hp = 30
            self.dam = 6
            self.agi = 5
            self.dex = 8
            self.fullHealth = 30    
        elif race == "Exalted Mortal":
            self.hp = 20
            self.dam = 5
            self.agi = 7
            self.dex = 10
            self.fullHealth = 20
        elif race == "God":
            self.hp = 1000000000000
            self.dam = 1000
            self.agi = 1000
            self.dex = 1000
    def primarySpecial(self, target):
        #Blinding Flash: Reduces enemy chance to hit for 3 rounds
        enemyBlinded = 3
        print("The enemy is blinded!")
    def secondarySpecial(self, target):
        #Blessing: Reduces damage taken for next 3 rounds
        playerBlessed = 3
    def passive(self, target):
        if self.race == "Angel":
            #Radiance: Deals damage each turn
            target.hp -= 3
            print("Radiance burns your foe!")
            print("Enemy has " + str(target.hp) + " remaining!")
        if self.race == "Aasimar":
            self.hp += random.randrange(1,6)
            print("Your divine blood heals your wounds!")
            print("Your health is now:", self.hp)
        if self.race == "Exalted Mortal":
            print("Your blessing makes your strikes hit harder!")

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
        badTerrain = ('#')
        enemyTerrain = ('~')
        bossTerrain = ('@')
        if x == self.size or y == self.size:
            print("Out of bounds!")
            return False
        elif x < 0 or y < 0:
            print("Out of bounds!")
            return False
        elif self.grid[x][y] in badTerrain:
            print("You can't go that way!")
            return False
        elif self.grid[x][y] in enemyTerrain:
            print("An enemy approaches!")
            seed = random.randrange(1, 3)
            #initiate combat
            if seed == 1:
                devil = Entity("Devil", "Male", "Demon", "Cannon Fodder", 5, 2, 10, 4)
                enemy = devil
                combat(player, enemy)
                player.hp = player.fullHealth
                return True
            elif seed == 2:
                lesserFiend = Entity("Lesser Fiend", "Male", "Demon", "Grunt", 15, 4, 5, 2)
                enemy = lesserFiend
                combat(player, enemy)
                player.hp = player.fullHealth
                return True
        elif self.grid[x][y] in bossTerrain:
            fiendLord = Entity("Fiend Lord", "Male", "Demon", "Boss", 30, 8, 6, 1)
            enemy = fiendLord
            print("You have arrived at the temple, and now face the mighty Lord of Fiends!")
            print("Prepare yourself!")
            combat(player, enemy)
            gameEnd()
            return True      
        else:
            return True

    def setTerrain(self, x, y, newTerrain):
        TERRAIN = ('-','~','#','@')
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
        if direction == "4":
            #Move West
            if self.tileCheck(self.charX, self.charY - 1):
                self.grid[self.charX][self.charY] = "-"
                self.charY -= 1
                self.grid[self.charX][self.charY] = "X"
        elif direction == "3":
            #Move East
            if self.tileCheck(self.charX, self.charY + 1):
                self.grid[self.charX][self.charY] = "-"
                self.charY += 1
                self.grid[self.charX][self.charY] = "X"
        elif direction == "2":
            #Move South
            if self.tileCheck(self.charX + 1, self.charY):
                self.grid[self.charX][self.charY] = "-"
                self.charX += 1
                self.grid[self.charX][self.charY] = "X"
        elif direction == "1":
            #Move North
            if self.tileCheck(self.charX - 1, self.charY):
                self.grid[self.charX][self.charY] = "-"
                self.charX -= 1
                self.grid[self.charX][self.charY] = "X"
        else:
            print("You didn't give me a cardinal direction!")

#Returns an Entity object if all steps are confirmed, else returns None.
def createChar():            
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
            finished = False
    finished = False
    while not finished:
        choice = input("Developer hack: Do you need god-mode to clear the game faster?\n [Y/N]")
        if choice.lower() == 'y':
            needJesus = True
            finished = True
        else:
            needJesus = False
            finished = True

            
    print("You've finished telling me about yourself. \nYou are " + charName + ", the " + charGender + " " + charRace + " " + charClass + ".")
    if needJesus:
        print("You're also using the developer cheat.")
    confirm = input("Is all that correct? if it isn't, we have to start all over. [Y/N]")
    if confirm.lower() == "y":
        if charClass == "Solar Knight":
            if needJesus:
                charRace = "God"
                player = Knight(charName, charGender, charRace, charClass)
                return player
            player = Knight(charName, charGender, charRace, charClass)
            return player
        elif charClass == "Ember Monk":
            if needJesus:
                charRace = "God"
                player = Knight(charName, charGender, charRace, charClass)
                return player
            player = Monk(charName, charGender, charRace, charClass)
            return player
        elif charClass =="Aurora Warden":
            if needJesus:
                charRace = "God"
                player = Knight(charName, charGender, charRace, charClass)
                return player
            player = Warden(charName, charGender, charRace, charClass)
            return player
        else:
            print("We will begin again, then.")
            return None

def combat(player, enemy):
    stillFighting = True
    enemyStunned = False
    enemyAblaze = 0
    enemyBlinded = 0
    playerBlessed = 0
    enemyAttacked = False
    playerTurn = True
    while stillFighting:
        #remove stunned status
        enemyStunned = False
        #Player turn begins
        playerTurn = True
        while playerTurn:
            print(actionMenu)
            action = input("\nWhat would you like to do?\n")
            if action == "1":
                player.attack(enemy)
                print("The enemy has " + str(enemy.hp) + " hp remaining!")
                print("You have " + str(player.hp) + " hp remaining!")
                playerTurn = False
            elif action == "2":
                player.primarySpecial(enemy)
                playerTurn = False
            elif action == "3":
                player.secondarySpecial(enemy)
                playerTurn = False
            elif action == "4":
                difficulty = random.randrange(1,10)
                if player.agi * 10 > difficulty * 10:
                    print("You ran away!")
                    print("You have forsaken your cause, and mortals are doomed to the darkness.")
                    print("Game over!")
                    sys.exit(0)
                else:
                    print("You couldn't get away!")
            elif action == "5":
                if player.playerClass == "Solar Knight":
                    print(knightDesc)
                elif player.playerClass == "Ember Monk":
                    print(monkDesc)
                elif player.playerClass == "Aurora Warden":
                    print(wardenDesc)
            else:
                print("That wasn't a valid number.")
                print(actionMenu)
                action = input("What would you like to do?")

        #HP checks for end of combat
        if enemy.hp <= 0:
            print("You defeated the " + enemy.name + "!")
            stillFighting = False
            return True
        elif player.hp <= 0:
            print("You died! Game over.")
            sys.exit(0)

        #Racial passive
        if player.race == "Angel":
            player.passive(enemy)
        elif player.race == "Aasimar":
            player.passive(enemy)
            
        #Enemy status check
        if enemyStunned == True:
            print("The enemy is no longer stunned!")
        elif enemyAblaze > 0:
            enemy.hp -= random.randrange(1,7)
            print("The enemy is burned by the flames!")
            enemy.attack(player)
            enemyAblaze -= 1
        #HP checks for end of combat
            if enemy.hp <= 0:
                print("You defeated the " + enemy.name + "!")
                stillFighting = False
                return True
            elif player.hp <= 0:
                print("You died! Game over.")
                sys.exit(0)
        elif enemyBlinded > 0:
            if playerBlessed > 0:
                enemy.dam /= 2
            enemy.agi /= 2
            enemy.attack(player)
            enemy.agi *= 2
            enemyBlinded -= 1
            enemyAttacked = True
            if playerBlessed > 0:
                playerBlessed -= 1
        #HP checks for end of combat
            if enemy.hp <= 0:
                print("You defeated the " + enemy.name + "!")
                stillFighting = False
                return True
            elif player.hp <= 0:
                print("You died! Game over.")
                sys.exit(0)
        #Player status check
        if not enemyAttacked:
            #Gives enemy attack if enemy not afflicted by Blind
            if playerBlessed > 0:
                print("Your blessing reduces damage taken!")
                enemy.dam /= 2
                enemy.attack(player)
                enemy.dam *=2
                playerBlessed -= 1
                #HP checks for end of combat
                if enemy.hp <= 0:
                    print("You defeated the " + enemy.name + "!")
                    stillFighting = False
                    return True
                elif player.hp <= 0:
                    print("You died! Game over.")
                    sys.exit(0)
            else:
                enemy.attack(player)
                #HP checks for end of combat
                if enemy.hp <= 0:
                    print("You defeated the " + enemy.name + "!")
                    stillFighting = False
                    return True
                elif player.hp <= 0:
                    print("You died! Game over.")
                    sys.exit(0)
                 
def saveGame(player, gameMap):
    saveFile = open('savegame.bin','wb')
    pickle.dump(player, saveFile)
    mapList = gameMap.grid
    mapX = gameMap.charX
    mapY = gameMap.charY
    pickle.dump(mapList, saveFile)
    pickle.dump(mapX, saveFile)
    pickle.dump(mapY, saveFile)
    saveFile.close()
    print("Game saved to savegame.bin!")

def loadGame():
    saveFile = open('savegame.bin', 'rb')
    global player
    player = pickle.load(saveFile)
    loadedMapGrid = pickle.load(saveFile)
    loadedMapX = pickle.load(saveFile)
    loadedMapY = pickle.load(saveFile)
    global gameMap
    gameMap.grid = loadedMapGrid
    gameMap.charX = loadedMapX
    gameMap.charY = loadedMapY
    
    print("Game loaded!")
    print(gameMap)

def menu(player, gameMap):
    onMap = False
    onMenu = True
    gameOn = True

    while gameOn:
    
        while onMenu:
            print("S - Save Game | E - Exit Game | M - Map Travel")
            choice = input("What would you like to do?")
            if choice.upper() == "S":
                saveGame(player, gameMap)
            elif choice.upper() == "E":
                sys.exit(0)
            elif choice.upper() == "M":
                print("Moving to map.")
                onMap = True
                onMenu = False

        while onMap:
            print(gameMap.hideEnemies())
            print("Which way would you like to go?")
            moveChoice = input("1 - North | 2 - South | 3 - East | 4 - West\n")
            if moveChoice == "1":
                gameMap.move(moveChoice)
                print(gameMap.hideEnemies())
                onMap = False
            elif moveChoice == "2":
                gameMap.move(moveChoice)
                print(gameMap.hideEnemies())
                onMap = False
            elif moveChoice == "3":
                gameMap.move(moveChoice)
                print(gameMap.hideEnemies())
                onMap = False    
            elif moveChoice == "4":
                gameMap.move(moveChoice)
                print(gameMap.hideEnemies())
                onMap = False
            else:
                print("That wasn't a valid choice.")
                gameMap.move(choice)

        onMenu = True
    
        
def gameEnd():
    print("You have slain the demon's leader, and the Temple of Sol is now safe.")
    print("You have triumphed! Victory is yours!")
    print("Game over! You win!")
    sys.exit(0)
        
def main():
    gameOn = True
    global gameMap
    gameMap = Map()
    #Set map terrain
    gameMap.setTerrain(3, 4, '@')
    gameMap.setTerrain(3, 2, '~')
    gameMap.setTerrain(2, 2, '~')
    gameMap.setTerrain(0, 4, '~')
    gameMap.setTerrain(1, 3, '~')
    gameMap.setTerrain(1, 0, '~')
    gameMap.setTerrain(1, 2, '~')
    gameMap.setTerrain(0, 3, '#')
    gameMap.setTerrain(3, 3, '#')
    gameMap.setTerrain(2, 0, '#')
    gameMap.setTerrain(3, 0, '#')
    gameMap.setTerrain(4, 0, '#')
    gameMap.setTerrain(4, 1, '#')
    gameMap.setTerrain(4, 2, '#')
    gameMap.setTerrain(4, 3, '#')
    gameMap.setTerrain(4, 4, '#')
    #Generate Player
    global player
    player = None
    while player == None:
        player = createChar()
    print(player)
    
    #Generate enemies
    lesserFiend = Entity("Lesser Fiend", "Male", "Demon", "Grunt", 15, 5, 5, 2)
    fiendLord = Entity("Fiend Lord", "Male", "Demon", "Boss", 30, 7, 6, 1)
    devil = Entity("Devil", "Male", "Demon", "Cannon Fodder", 5, 3, 10, 4)
    
    print("The temple lies to the south, marked by the @ symbol.")
    while gameOn:
        answer = input("Would you like to load the game from a saved file? [Y/N]")
        if answer.upper() == "Y":
            loadGame()

        else:
            print("I'll assume that means no. Onward to the game!")
        menu(player, gameMap)
    
main()
