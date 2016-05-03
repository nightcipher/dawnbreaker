#Pickles large text blocks for clarity in main program.

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

angelDesc = '''
An angel of the Solar Order who helps guard mortals from demons.
Angels are all shrouded in radiant light,
burning dark creatures unfortunate enough to be near.
Passive: Radiance - Deals damage each turn to enemies.
HP: 15
Strength: 7
Agility: 10
Dexterity: 5
'''
aasimarDesc = '''
A direct descendent of the union between an angel and a mortal.
The divine blood in them heals their wounds very swiftly,
even though it is not as pure as an angel's.
Passive: Rejuvenation - Restores HP every few turns.
HP: 20
Strength: 6
Agility: 5
Dexterity: 8
'''
exaltedDesc = '''
A mortal blessed by Sol for their devotion to justice.
They fight with strength beyond what average mortals are capable of,
hitting harder and faster than even some angelic warriors.
Demons fear them for their combat strength.
Passive: Rancor - Critical hits and Counterstrikes deal double damage. 
HP: 10
Strength: 6
Agility: 7
Dexterity: 10
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
knightDesc = '''
A knight of the Solar Order. They have trained with the angels
to learn powerful combat techniques. Nothing can stand in their way. 
Deliverance:  Powerful attack that deals double damage, but might miss.
Divine Smite: Stuns the enemy for one round.
'''
monkDesc = '''
A monk who worships the sacred flames of Sol.
They fight with speed and dexterity, rather than raw strength. 
Raging Strikes: Makes 3-5 weaker strikes at target enemy.
Radiant Flames: Burns the enemy, dealing immediate damage and damage over the next few rounds.
'''
wardenDesc = '''
A warden of Sol. They are driven to protect the innocent,
and specialize in mitigating damage taken.
Blinding Flash: Enemy has increased chance to miss for the next few rounds.
Blessing: Reduces damage taken for the next few rounds.
'''
import pickle
theFile = open('TextBlocks.bin','wb')
pickle.dump(raceMenu, theFile)
pickle.dump(angelDesc, theFile)
pickle.dump(aasimarDesc, theFile)
pickle.dump(exaltedDesc, theFile)
pickle.dump(classMenu, theFile)
pickle.dump(knightDesc, theFile)
pickle.dump(monkDesc, theFile)
pickle.dump(wardenDesc, theFile)
theFile.close()
