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

import pickle
theFile = open('menus.bin','wb')
pickle.dump(raceMenu, theFile)
pickle.dump(classMenu, theFile)
