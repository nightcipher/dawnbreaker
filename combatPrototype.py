import random

actionMenu = '''
|=========================|
|=====Time to  Fight======|
|1) Attack                |
|2) Special 1             |
|3) Special 2             |
|4) Flee                  |
|5) Class Description     |
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
    stillFighting = True
    enemyStunned = False
    enemyAblaze = 0
    enemyBlinded = 0
    playerBlessed = 0
    enemyAttacked = False
    while stillFighting:
        #remove stunned status
        enemyStunned = False
        #Racial passive
        if player.race == "Angel":
            player.passive(enemy)
        elif player.race == "Aasimar":
            player.passive()
        #Player turn begins
        print(actionMenu)
        action = int(input("\nWhat would you like to do?\n"))
        while action not in (1,2,3,4):
            print(actionMenu)
            action = int(input("\nWhat would you like to do?\n"))
        if action == 1:
            player.attack(enemy)
            print("The enemy has " + enemy.hp + " remaining!")
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action ==4:
            difficulty = random.randrange(1,10)
            if player.agi * 10 > difficulty * 10:
                print("You ran away!")
                return 3
            else:
                print("You couldn't get away!")
        elif action == 5:
            if player.playerClass == "Solar Knight":
                print(knightDesc)
            elif player.playerClass == "Ember Monk":
                print(monkDesc)
            elif player.playerClass == "Aurora Warden":
                print(wardenDesc)

        #HP checks for end of combat
        if enemy.hp <= 0:
            print("You defeated the " + enemy.name + "!")
            return 1
        elif player.hp <= 0:
            print("You died! Game over.")
            return 2

        #Enemy status check
        if enemyStunned == True:
            print("The enemy is no longer stunned!")
        elif enemyAblaze > 0:
            enemy.hp -= random.randrange(1,7)
            print("The enemy is burned by the flames!")
            enemy.attack(player)
            enemyAblaze -= 1
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
        #Player status check
        if not enemyAttacked:
            #Gives enemy attack if enemy not afflicted by Blind
            if playerBlessed > 0:
                print("Your blessing reduces damage taken!")
                enemy.dam /= 2
                enemy.attack(player)
                enemy.dam *=2
                playerBlessed -= 1
            else:
                enemy.attack(player)
                  

player = Player("Mark", "Male", "Elf", "Warrior", 20, 10, 10, 10)

enemy = Player("Demon", "Male", "Dark", "Fighter", 20, 10, 10, 10)

combat()

print(enemy)
