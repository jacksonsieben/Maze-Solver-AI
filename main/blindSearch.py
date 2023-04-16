import os
from colorama import Fore
import time

class blindSearch:
    
    def __init__(self, maze, height=11, width=27):
        self.maze = maze
        self.steps = 0
        self.errorSteps = 0
        self.flag = 0
        self.path = []
        self.height = height
        self.width = width
    
    def gotoxy(self,x,y):
        print ("%c[%d;%df" % (0x1B, y, x), end='')

    def printMaze(self, maze):
        for i in range(0, self.height):
            # time.sleep(0.00001)
            for j in range(0, self.width):
                self.gotoxy(j+1,i+1)
                if (maze[i][j] == 'p'):
                    print(Fore.WHITE + "\u2588", end="")
                elif (maze[i][j] == 'c'):
                    print(Fore.GREEN + ' ', end="")
                else:
                    print(Fore.RED +  "\u2593", end="")
                
            print()
        self.gotoxy(0, self.height+2)
        print("Passos: " + str(self.steps))

    def startFinishPoints(self):
        start = [i for i in range(len(self.maze[0])) if self.maze[0][i] == 'c']
        finish = [i for i in range(len(self.maze[0])) if self.maze[len(self.maze)-1][i] == 'c']
        return [0, start[0]], [len(self.maze) - 1, finish[0]]
    
    def search(self, showPath=0):
        currentPoint = self.path[len(self.path) - 1]
        self.steps += 1
        if self.flag == 1:
            return

        if currentPoint == self.finish:
            self.flag = 1
            return self.flag
        elif showPath == 1:
            self.printMaze(self.maze)

        if self.maze[currentPoint[0] + 1][currentPoint[1]] == 'c' and currentPoint is not self.finish and self.flag != 1:
            self.maze[currentPoint[0] + 1][currentPoint[1]] = 'p'
            self.path.append([currentPoint[0] + 1, currentPoint[1]])
            self.search(showPath)

        if self.maze[currentPoint[0]][currentPoint[1] + 1] == 'c' and currentPoint is not self.finish and self.flag != 1:
            self.maze[currentPoint[0]][currentPoint[1] + 1] = 'p'
            self.path.append([currentPoint[0], currentPoint[1] + 1])
            self.search(showPath)

        if self.maze[currentPoint[0] - 1][currentPoint[1]] == 'c' and currentPoint is not self.finish and self.flag != 1:
            self.maze[currentPoint[0] - 1][currentPoint[1]] = 'p'
            self.path.append([currentPoint[0] - 1, currentPoint[1]])
            self.search(showPath)

        if self.maze[currentPoint[0]][currentPoint[1] - 1] == 'c' and currentPoint is not self.finish and self.flag != 1:
            self.maze[currentPoint[0]][currentPoint[1] - 1] = 'p'
            self.path.append([currentPoint[0], currentPoint[1] - 1])
            self.search(showPath)
        
        currentPoint = self.path[len(self.path) - 1]
        if currentPoint != self.finish:
            pointToRemove = self.path[len(self.path) - 1]
            self.path.remove(pointToRemove)
            self.maze[pointToRemove[0]][pointToRemove[1]] = 'c'
            self.errorSteps += 1
    
    def solveMaze(self):
        self.start, self.finish = self.startFinishPoints()
        self.maze[self.start[0]][self.start[1]] = 'p'

        self.path = [self.start]
        os.system("cls")
        start = time.time()
        self.search()
        end = time.time()
        self.printMaze(self.maze)

        self.gotoxy(0, self.height+3)
        print("Passos errados: " + str(self.errorSteps))
        print("Tempo de resolucao: " + str(end-start) + " segundos")

        