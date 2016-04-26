#Dawnbreaker V 1.0
#By Nate Stonecipher
#Written 4-20-2016

import random

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
        
        
    
class Warrior(player):
	def
        
class Archer(player):
    
