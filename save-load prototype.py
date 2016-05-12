import pickle
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
        print(direction)
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
            def passive(self, target):
                #Radiance: Deals damage each turn
                target.hp -= 3
                print("Radiance burns your foe!")
        #Static racial ability code goes here
        elif race == "Aasimar":
            self.hp = 30
            self.dam = 6
            self.agi = 5
            self.dex = 8
            self.fullHealth = 30
            def passive(self):
                self.hp += random.randrange(1,6)
                print("Your divine blood heals your wounds!")
                print("Your health is now:", self.hp)
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





saveFile = open('savegame.bin', 'rb')
player = pickle.load(saveFile)
theMap = pickle.load(saveFile)

print(theMap)
