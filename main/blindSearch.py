import copy
from colorama import Fore
import time

class BlindSearch:
    
    def __init__(self, Maze):
        self.Maze = copy.deepcopy(Maze)
        self.steps = 0
        self.errorSteps = 0
        self.flag = 0
        self.path = []

    def gotoxy(self,x,y):
        print ("%c[%d;%df" % (0x1B, y+2, x), end='')

    def printMaze(self, finalPath=False):
        if finalPath:
            p = Fore.GREEN
        else: 
            p = Fore.WHITE
        for i in range(0, self.Maze.height):
            for j in range(0, self.Maze.width):
                self.gotoxy(j+1,i+1)
                if (self.Maze.maze[i][j] == 'p'):
                    print(p + "\u2588", end="")
                elif (self.Maze.maze[i][j] == 'c'):
                    print(Fore.GREEN + ' ', end="")
                elif (self.Maze.maze[i][j] == 'e'):
                    print(Fore.WHITE + "\u2588", end="")
                else:
                    print(Fore.RED +  "\u2593", end="")

    def search(self, showPath=0):
        currentPoint = self.path[len(self.path) - 1]
        self.steps += 1
        if self.flag == 1:
            return

        if currentPoint == self.Maze.end:
            self.flag = 1
            return self.flag
        elif showPath == 1:
            self.printMaze()

        if self.Maze.maze[currentPoint[0] + 1][currentPoint[1]] == 'c' and currentPoint is not self.Maze.end and self.flag != 1:
            self.Maze.maze[currentPoint[0] + 1][currentPoint[1]] = 'p'
            self.path.append([currentPoint[0] + 1, currentPoint[1]])
            self.search(showPath)

        if self.Maze.maze[currentPoint[0]][currentPoint[1] + 1] == 'c' and currentPoint is not self.Maze.end and self.flag != 1:
            self.Maze.maze[currentPoint[0]][currentPoint[1] + 1] = 'p'
            self.path.append([currentPoint[0], currentPoint[1] + 1])
            self.search(showPath)

        if self.Maze.maze[currentPoint[0] - 1][currentPoint[1]] == 'c' and currentPoint is not self.Maze.end and self.flag != 1:
            self.Maze.maze[currentPoint[0] - 1][currentPoint[1]] = 'p'
            self.path.append([currentPoint[0] - 1, currentPoint[1]])
            self.search(showPath)

        if self.Maze.maze[currentPoint[0]][currentPoint[1] - 1] == 'c' and currentPoint is not self.Maze.end and self.flag != 1:
            self.Maze.maze[currentPoint[0]][currentPoint[1] - 1] = 'p'
            self.path.append([currentPoint[0], currentPoint[1] - 1])
            self.search(showPath)
        
        currentPoint = self.path[len(self.path) - 1]
        if currentPoint != self.Maze.end:
            pointToRemove = self.path[len(self.path) - 1]
            self.path.remove(pointToRemove)
            self.Maze.maze[pointToRemove[0]][pointToRemove[1]] = 'e'
            self.errorSteps += 1
    
    def solveMaze(self, showPath=0):
        self.Maze.maze[self.Maze.start[0]][self.Maze.start[1]] = 'p'

        self.path = [self.Maze.start]
        self.gotoxy(1, 0)
        print(Fore.WHITE + "DeepSearch Algorithm", end="")
        start = time.time()
        self.search(showPath)
        end = time.time()
        self.printMaze(True)

        self.gotoxy(0, self.Maze.height+2)
        print(Fore.WHITE + "Passos: " + str(self.steps), end="")
        self.gotoxy(0, self.Maze.height+3)
        print(Fore.WHITE + "Passos errados: " + str(self.errorSteps), end="")
        self.gotoxy(0, self.Maze.height+4)
        print(Fore.WHITE + "Tempo de resolucao: ", end="")
        self.gotoxy(0, self.Maze.height+5)
        print(Fore.WHITE + str(end-start) + " segundos", end="")
        

        