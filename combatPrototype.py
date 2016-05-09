import random

actionMenu = '''
|=========================|
|=====Time to  Fight======|
|1) Attack                |
|2) Special 1             |
|3) Special 2             |
|4) Flee                  |
|=========================|
|=========================|
Enter a number.
'''

class Player(object):
    def __init__(self, name, gender, race, playerClass, hp = 1, dam = 0, dex = 0, agi = 0):
        self.name = name
        self.gender = gender
        self.race = race
        self.playerClass = playerClass
        self.hp = hp
        self.dam = dam
        self.dex = dex
        self.agi = agi
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
                  

player = Player("Mark", "Male", "Elf", "Warrior", 20, 10, 10, 10)

enemy = Player("Demon", "Male", "Dark", "Fighter", 20, 10, 10, 10)

combat()

print(enemy)
