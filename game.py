#!/usr/bin/env python3
import getch, locations, math, random, sys
class Game:
    def __init__(self):
        self.mapX = 50
        self.mapY = 15
        self.gameSprites = {'town': '⌂', 'rock': 'O', 'player': '^', 'block': '#', 'cave': 'C', 'bg': '░', 'wild': 'W', 'zombie': 'Z'}
        self.playerCords = [5, 5]
        self.previousCords = list(self.playerCords)
        self.blocks = []
        self.places = locations.Locations()
        self.location = 'wild'
        self.gameTime = 0.0
        self.enemies = [] # Current spawned enemies
    
    def clear(self):
        print('\033c')

    def inspect(self):
        facing = self.gameSprites['player']
        inspectCords = (0,0)
        inspectResult = ''
        if facing == '^':
            inspectCords = (self.playerCords[0], (self.playerCords[1] - 1))
        elif facing == '<':
            inspectCords = ((self.playerCords[0] - 1), self.playerCords[1])
        elif facing == '>':
            inspectCords = ((self.playerCords[0] + 1), self.playerCords[1])
        elif facing == 'v':
            inspectCords = (self.playerCords[0], (self.playerCords[1] + 1))
        for thing in self.places.gameMaps[self.location]:
            if inspectCords[0] == self.places.gameMaps[self.location][thing][0] and inspectCords[1] == self.places.gameMaps[self.location][thing][1]:
                inspectResult = thing
        try:
            self.places.mapETC[self.location]
        except KeyError:
            pass
        else:
            for thing in range(len(self.places.mapETC[self.location])):
                if inspectCords[0] == self.places.mapETC[self.location][thing][0][0] and inspectCords[1] == self.places.mapETC[self.location][thing][0][1]:
                    inspectResult = self.places.mapETC[self.location][thing][1]
        if inspectResult != '':
            print('Inspect: That is a', inspectResult)
        else:
            print('Inspect: I see nothing there.')
        getch.getch()
    
    def incrementTime(self, amount=0.01):
        self.gameTime += amount
        if self.gameTime > 24.0:
            self.gameTime = 0 + (self.gameTime - 24.0)
        self.gameTime = float(format(self.gameTime, '.2f'))
    
    def locationChange(self, oldLocation):
        self.enemies.clear()
        if self.location == 'cave':
            self.playerCords = [0,0]
        elif self.location == 'wild':
            if oldLocation == 'cave':
                self.playerCords = [3,3]
            elif oldLocation == 'town':
                self.playerCords = [10,10]
        elif self.location == 'town':
            self.playerCords = [10,0]
    
    def detectCollide(self):
        for block in self.blocks:
            if block[0] == self.playerCords[0] and block[1] == self.playerCords[1]:
                self.playerCords = list(self.previousCords)
                sys.stdout.write('\a')
        for item in self.places.gameMaps[self.location]:
            if item in self.places.gameMaps:
                try:
                    if self.playerCords[0] == self.places.gameMaps[self.location][item][0] and self.playerCords[1] == self.places.gameMaps[self.location][item][1]:
                        oldLocation = self.location
                        self.location = item
                        self.locationChange(oldLocation)
                        break
                except KeyError:
                    self.playerCords = list(self.previousCords)
                    sys.stdout.write('\a')
            else:
                if item in self.places.gameMaps[self.location]:
                    if self.playerCords[0] == self.places.gameMaps[self.location][item][0] and self.playerCords[1] == self.places.gameMaps[self.location][item][1]:
                        self.playerCords = list(self.previousCords)
                        sys.stdout.write('\a')
        else:
            try:
                self.places.mapETC[self.location]
            except KeyError:
                pass
            else:
                for thing in range(len(self.places.mapETC[self.location])):
                    if self.playerCords[0] == self.places.mapETC[self.location][thing][0][0] and self.playerCords[1] == self.places.mapETC[self.location][thing][0][1]:
                        self.playerCords = list(self.previousCords)
    
    def enemyHandler(self):
        if len(self.enemies) == 0:
            if self.location == 'wild':
                self.enemies.append(('zombie', (0, 0)))
        else:
            for i in range(len(self.enemies)):
                oldCords = self.enemies[i][1]
                newCords = ((oldCords[0] + random.randint(0, 2)), (oldCords[1] + random.randint(0, 2)))
                self.enemies[i] = ('zombie', newCords)
                

    def printMap(self):
        for yCount in range(self.mapY):
            for xCount in range(self.mapX):
                char = self.gameSprites['bg']
                if xCount == self.playerCords[0] and yCount == self.playerCords[1]:
                    char = self.gameSprites['player']
                for thing in self.places.gameMaps[self.location]:
                    if xCount == self.places.gameMaps[self.location][thing][0] and yCount == self.places.gameMaps[self.location][thing][1]:
                        char = self.gameSprites[thing]
                for enemy in self.enemies:
                    if xCount == enemy[1][1] and yCount == enemy[1][1]:
                        char = self.gameSprites[enemy[0]]
                try:
                    self.places.mapETC[self.location]
                except KeyError:
                    pass
                else:
                    for thing in range(len(self.places.mapETC[self.location])):
                        if xCount == self.places.mapETC[self.location][thing][0][0] and yCount == self.places.mapETC[self.location][thing][0][1]:
                            char = self.gameSprites[self.places.mapETC[self.location][thing][1]]
                    for block in self.blocks:
                        if xCount == block[0] and yCount == block[1]:
                            char = self.gameSprites['block']
                print(char, end='')
            print('')

game = Game()

while True:
    game.clear()
    game.printMap()
    game.incrementTime()
    print(game.location.upper() + ':', game.playerCords)
    print('Time:', game.gameTime)
    c = getch.getch()
    game.previousCords = list(game.playerCords)
    if c == 'w' and game.playerCords[1] != 0:
        game.playerCords[1] -= 1
        game.gameSprites['player'] = '^'
    elif c == 'a' and game.playerCords[0] != 0:
        game.playerCords[0] -= 1
        game.gameSprites['player'] = '<'
    elif c == 's' and game.playerCords[1] != game.mapY - 1:
        game.playerCords[1] += 1
        game.gameSprites['player'] = 'v'
    elif c == 'd' and game.playerCords[0] != game.mapX - 1:
        game.playerCords[0] += 1
        game.gameSprites['player'] = '>'
    elif c == 'b':
        for block in game.blocks:
            if game.playerCords[0] == block[0] and game.playerCords[1] == block[1]:
                break
        for thing in game.places.gameMaps[game.location]:
            if game.places.gameMaps[game.location][thing][0] == game.playerCords[0] and game.places.gameMaps[game.location][thing][1] == game.playerCords[1]:
                break
        else:
            game.blocks.append((game.playerCords[0], game.playerCords[1]))
    elif c == ' ':
        game.inspect()
    game.enemyHandler()
    game.detectCollide()