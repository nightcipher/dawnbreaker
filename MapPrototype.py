#Map Prototype
#Nate Stonecipher

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

        self.grid[charX][charY] = "X"

    def __str__(self):
        result = ""
        for x in range(self.size):
            for y in range(self.size):
                result += self.grid[x][y]
            result += "\n"
        return result

    def tileCheck(self, x, y):
        badTerrain = ('~', '#')
        if self.grid[x][y] in badTerrain:
            return False
        elif x == self.size or y == self.size:
            return False
        else:
            return True

    def setTerrain(self, x, y, newTerrain):
        TERRAIN = ('-','~','#','!')
        if newTerrain in TERRAIN:
            self.grid[x][y] = newTerrain
        else:
            print("Error! That's not valid terrain.")

    def move(self, direction):
        if direction == "west":
            if self.tileCheck(self.charX, self.charY - 1):
                self.grid[self.charX][self.charY] = "-"
                self.charY -= 1
                self.grid[self.charX][self.charY] = "X"
        if direction == "east":
            if self.tileCheck(self.charX, self.charY + 1):
                self.grid[self.charX][self.charY] = "-"
                self.charY += 1
                self.grid[self.charX][self.charY] = "X"
        if direction == "south":
            if self.tileCheck(self.charX + 1, self.charY):
                self.grid[self.charX][self.charY] = "-"
                self.charX += 1
                self.grid[self.charX][self.charY] = "X"
        if direction == "north":
            if self.tileCheck(self.charX - 1, self.charY):
                self.grid[self.charX][self.charY] = "-"
                self.charX -= 1
                self.grid[self.charX][self.charY] = "X"
testMap = Map()
print(testMap)

testMap.move("south")
print(testMap)
    
testMap.move("north")
print(testMap)

testMap.move("east")
print(testMap)

testMap.move("west")
print(testMap)
