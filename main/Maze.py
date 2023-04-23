from colorama import Fore, init
import random
import os

class Maze:
    def __init__(self, height=12, width=22):
        self.a = 0
        self.maze = []
        self.height = height
        self.width = width
        self.backCounter = 0
                
        self.generateMaze()

        self.start, self.end = self.startFinishPos()
    
    def startFinishPos(self):
        start = [i for i in range(len(self.maze[0])) if self.maze[0][i] == 'c']
        finish = [i for i in range(len(self.maze[0])) if self.maze[len(self.maze)-1][i] == 'c']
        return [0, start[0]], [len(self.maze) - 1, finish[0]]

    def gotoxy(self,x,y):
        print ("%c[%d;%df" % (0x1B, y, x+30), end='')

    def aroundCells(self, randWall):
        aCells = 0
        if (self.maze[randWall[0]-1][randWall[1]] == 'c'):
            aCells += 1
        if (self.maze[randWall[0]+1][randWall[1]] == 'c'):
            aCells += 1
        if (self.maze[randWall[0]][randWall[1]-1] == 'c'):
            aCells +=1
        if (self.maze[randWall[0]][randWall[1]+1] == 'c'):
            aCells += 1
        
        return aCells

    def generateMaze(self):

        init()
        
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                line.append('u')
            self.maze.append(line)
        
        startH = int(random.random()*self.height)
        startW = int(random.random()*self.width)
        if (startH == 0):
            startH += 1
        if (startH == self.height-1):
            startH -= 1
        if (startW == 0):
            startW += 1
        if (startW == self.width-1):
            startW -= 1

        self.maze[startH][startW] = 'c'
        walls = []
        walls.append([startH - 1, startW])
        walls.append([startH, startW - 1])
        walls.append([startH, startW + 1])
        walls.append([startH + 1, startW])

        self.maze[startH-1][startW] = 'w'
        self.maze[startH][startW - 1] = 'w'
        self.maze[startH][startW + 1] = 'w'
        self.maze[startH + 1][startW] = 'w'

        while (walls):
            
            randWall = walls[int(random.random()*len(walls))-1]
            
            if (randWall[1] != 0):
                if (self.maze[randWall[0]][randWall[1]-1] == 'u' and self.maze[randWall[0]][randWall[1]+1] == 'c'):
                    
                    aCells = self.aroundCells(randWall)

                    if (aCells < 2):
                        
                        self.maze[randWall[0]][randWall[1]] = 'c'
                        
                        if (randWall[0] != 0):
                            if (self.maze[randWall[0]-1][randWall[1]] != 'c'):
                                self.maze[randWall[0]-1][randWall[1]] = 'w'
                            if ([randWall[0]-1, randWall[1]] not in walls):
                                walls.append([randWall[0]-1, randWall[1]])

                        if (randWall[0] != self.height-1):
                            if (self.maze[randWall[0]+1][randWall[1]] != 'c'):
                                self.maze[randWall[0]+1][randWall[1]] = 'w'
                            if ([randWall[0]+1, randWall[1]] not in walls):
                                walls.append([randWall[0]+1, randWall[1]])
                        
                        if (randWall[1] != 0):	
                            if (self.maze[randWall[0]][randWall[1]-1] != 'c'):
                                self.maze[randWall[0]][randWall[1]-1] = 'w'
                            if ([randWall[0], randWall[1]-1] not in walls):
                                walls.append([randWall[0], randWall[1]-1])
                    
                    for wall in walls:
                        if (wall[0] == randWall[0] and wall[1] == randWall[1]):
                            walls.remove(wall)

                    continue

            if (randWall[0] != 0):
                if (self.maze[randWall[0]-1][randWall[1]] == 'u' and self.maze[randWall[0]+1][randWall[1]] == 'c'):

                    aCells = self.aroundCells(randWall)
                    if (aCells < 2):
                        
                        self.maze[randWall[0]][randWall[1]] = 'c'

                        if (randWall[0] != 0):
                            if (self.maze[randWall[0]-1][randWall[1]] != 'c'):
                                self.maze[randWall[0]-1][randWall[1]] = 'w'
                            if ([randWall[0]-1, randWall[1]] not in walls):
                                walls.append([randWall[0]-1, randWall[1]])

                        if (randWall[1] != 0):
                            if (self.maze[randWall[0]][randWall[1]-1] != 'c'):
                                self.maze[randWall[0]][randWall[1]-1] = 'w'
                            if ([randWall[0], randWall[1]-1] not in walls):
                                walls.append([randWall[0], randWall[1]-1])

                        
                        if (randWall[1] != self.width-1):
                            if (self.maze[randWall[0]][randWall[1]+1] != 'c'):
                                self.maze[randWall[0]][randWall[1]+1] = 'w'
                            if ([randWall[0], randWall[1]+1] not in walls):
                                walls.append([randWall[0], randWall[1]+1])

                    for wall in walls:
                        if (wall[0] == randWall[0] and wall[1] == randWall[1]):
                            walls.remove(wall)

                    continue

            if (randWall[0] != self.height-1):
                if (self.maze[randWall[0]+1][randWall[1]] == 'u' and self.maze[randWall[0]-1][randWall[1]] == 'c'):

                    aCells = self.aroundCells(randWall)
                    if (aCells < 2):
                        
                        self.maze[randWall[0]][randWall[1]] = 'c'

                        if (randWall[0] != self.height-1):
                            if (self.maze[randWall[0]+1][randWall[1]] != 'c'):
                                self.maze[randWall[0]+1][randWall[1]] = 'w'
                            if ([randWall[0]+1, randWall[1]] not in walls):
                                walls.append([randWall[0]+1, randWall[1]])
                        if (randWall[1] != 0):
                            if (self.maze[randWall[0]][randWall[1]-1] != 'c'):
                                self.maze[randWall[0]][randWall[1]-1] = 'w'
                            if ([randWall[0], randWall[1]-1] not in walls):
                                walls.append([randWall[0], randWall[1]-1])
                        if (randWall[1] != self.width-1):
                            if (self.maze[randWall[0]][randWall[1]+1] != 'c'):
                                self.maze[randWall[0]][randWall[1]+1] = 'w'
                            if ([randWall[0], randWall[1]+1] not in walls):
                                walls.append([randWall[0], randWall[1]+1])

                    for wall in walls:
                        if (wall[0] == randWall[0] and wall[1] == randWall[1]):
                            walls.remove(wall)

                    continue

            if (randWall[1] != self.width-1):
                if (self.maze[randWall[0]][randWall[1]+1] == 'u' and self.maze[randWall[0]][randWall[1]-1] == 'c'):

                    aCells = self.aroundCells(randWall)
                    if (aCells < 2):
                        
                        self.maze[randWall[0]][randWall[1]] = 'c'

                        if (randWall[1] != self.width-1):
                            if (self.maze[randWall[0]][randWall[1]+1] != 'c'):
                                self.maze[randWall[0]][randWall[1]+1] = 'w'
                            if ([randWall[0], randWall[1]+1] not in walls):
                                walls.append([randWall[0], randWall[1]+1])
                        if (randWall[0] != self.height-1):
                            if (self.maze[randWall[0]+1][randWall[1]] != 'c'):
                                self.maze[randWall[0]+1][randWall[1]] = 'w'
                            if ([randWall[0]+1, randWall[1]] not in walls):
                                walls.append([randWall[0]+1, randWall[1]])
                        if (randWall[0] != 0):	
                            if (self.maze[randWall[0]-1][randWall[1]] != 'c'):
                                self.maze[randWall[0]-1][randWall[1]] = 'w'
                            if ([randWall[0]-1, randWall[1]] not in walls):
                                walls.append([randWall[0]-1, randWall[1]])

                    for wall in walls:
                        if (wall[0] == randWall[0] and wall[1] == randWall[1]):
                            walls.remove(wall)

                    continue
            
            for wall in walls:
                if (wall[0] == randWall[0] and wall[1] == randWall[1]):
                    walls.remove(wall)
        
        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = 'w'

        for i in range(0, self.width):
            if (self.maze[1][i] == 'c'):
                self.maze[0][i] = 'c'
                break

        for i in range(self.width-1, 0, -1):
            if (self.maze[self.height-2][i] == 'c'):
                self.maze[self.height-1][i] = 'c'
                break
    
    def printMazeXY(self):
        os.system("cls")
        for i in range(0, self.height):
            for j in range(0, self.width):
                        self.gotoxy(j+1,i+1)
                        
                        if (self.maze[i][j] == 'p'):
                            print(Fore.WHITE + "\u2588", end="")
                        elif (self.maze[i][j] == 'c'):
                            print(Fore.GREEN + ' ', end="")
                        else:
                            print(Fore.RED +  "\u2593", end="")

    