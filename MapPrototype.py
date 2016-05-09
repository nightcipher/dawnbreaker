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
        badTerrain = ('~', '#')
        if x == self.size or y == self.size:
            print("Out of bounds!")
            return False
        elif x < 0 or y < 0:
            print("Out of bounds!")
            return False
        elif self.grid[x][y] in badTerrain:
            print("You can't go that way!")
            return False
        else:
            return True

    def setTerrain(self, x, y, newTerrain):
        TERRAIN = ('-','~','#','!','@')
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
theMap = Map()
print(theMap)
theMap.move(2)
print(theMap)
