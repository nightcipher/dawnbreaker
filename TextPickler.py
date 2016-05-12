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
HP: 25
Strength: 7
Agility: 10
Dexterity: 5
'''
aasimarDesc = '''
A direct descendent of the union between an angel and a mortal.
The divine blood in them heals their wounds very swiftly,
even though it is not as pure as an angel's.
Passive: Rejuvenation - Restores HP every turn.
HP: 30
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
HP: 20
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
Radiant Flames: Deas immediate damage and damage over the next few rounds.
'''
wardenDesc = '''
A warden of Sol. They are driven to protect the innocent,
and specialize in mitigating damage taken.
Blinding Flash: Enemy has increased chance to miss for the next few rounds.
Blessing: Reduces damage taken for the next few rounds.
'''
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
story = '''
The world is in grave danger. Demons under the command
of Rordran Vell, the Dawnbreaker, have invaded and now
threaten all mortals. They seek to complete an ancient,
powerful ritual at the Temple of Sol to destroy the
sun forever, casting the world in to eternal darkness.

You are the chosen warrior of the Solar Order, sworn
enemies of the demons. The rest of the order are
defending the major cities, preventing the demons from
slaughtering the innocent while you end the battle,
once and for all.
'''
title = '''
╔╦╗┌─┐┬ ┬┌┐┌┌┐ ┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
 ║║├─┤││││││├┴┐├┬┘├┤ ├─┤├┴┐├┤ ├┬┘
═╩╝┴ ┴└┴┘┘└┘└─┘┴└─└─┘┴ ┴┴ ┴└─┘┴└─
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
pickle.dump(actionMenu, theFile)
pickle.dump(story, theFile)
pickle.dump(title, theFile)
theFile.close()
