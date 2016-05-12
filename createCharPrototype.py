def createChar():

##    finished = False
##    while not finished:
##        choice = input = ("Developer hack: Do you need god-mode to clear the game faster?\n [Y/N]")
##        if choice.lower() == 'y':
##            needJesus = True
##        else:
##            needJesus = False
            
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

createChar()
