import numpy as np
from Node import *
from colorama import Fore
import copy
import time

class AStar:    

    def __init__(self, Maze):
        self.Maze = copy.deepcopy(Maze)
        self.cost = 1
        self.steps = 0
        self.errorSteps = 0

    def gotoxy(self,x,y):
        print ("%c[%d;%df" % (0x1B, y+2, x+30), end='')

    def getPath(self, currentNode):
        path = []

        current = currentNode
        while current is not None:
            path.append(current.position)
            current = current.parent
        
        path = path[::-1]
        self.steps = len(path)
        return path

    def search(self, start, end, showPath=0):
        startNode = Node(None, tuple(start))
        startNode.g = startNode.h = startNode.f = 0
        endNode = Node(None, tuple(end))
        endNode.g = endNode.h = endNode.f = 0

        toVisit = []  
        
        visited = [] 

        toVisit.append(startNode)

        maxIterations = (len(self.Maze.maze) // 2) ** 10

        move  = [[-1, 0 ], 
                 [ 0, -1], 
                 [ 1, 0 ], 
                 [ 0, 1 ]] 

        while len(toVisit) > 0: 
            self.errorSteps += 1    

            currentNode = toVisit[0]
            current_index = 0
            for index, item in enumerate(toVisit):
                if item.f < currentNode.f:
                    currentNode = item
                    current_index = index
            if(showPath != 0):
                self.addPathToMaze(self.getPath(currentNode))
                self.printMazeXY()         
            
            if self.errorSteps > maxIterations:
                print ("Maximo de iteracoes exedido!")
                return self.getPath(currentNode,self.Maze.maze)

            toVisit.pop(current_index)
            visited.append(currentNode)

            if currentNode == endNode:
                return self.getPath(currentNode)

            children = []

            for newPos in move: 

                nodePos = (currentNode.position[0] + newPos[0], currentNode.position[1] + newPos[1])

                if (nodePos[0] > (self.Maze.height - 1) or 
                    nodePos[0] < 0 or 
                    nodePos[1] > (self.Maze.width -1) or 
                    nodePos[1] < 0):
                    continue

                if self.Maze.maze[nodePos[0]][nodePos[1]] != 'c':
                    continue

                newNode = Node(currentNode, nodePos)

                children.append(newNode)

            for child in children:
                
                if len([visitedChild for visitedChild in visited if visitedChild == child]) > 0:
                    continue

                child.g = currentNode.g + self.cost
                
                child.h = (((child.position[0] - endNode.position[0]) ** 2) + 
                        ((child.position[1] - endNode.position[1]) ** 2)) 

                child.f = child.g + child.h

                if len([i for i in toVisit if child == i and child.g > i.g]) > 0:
                    continue

                toVisit.append(child)
                

    def printMazeXY(self):
        # os.system("cls")
        for i in range(0, self.Maze.height):
            for j in range(0, self.Maze.width):
                        self.gotoxy(j+1,i+1)
                        if (self.Maze.maze[i][j] == 'p'):
                            print(Fore.WHITE + "\u2588", end="")
                        elif (self.Maze.maze[i][j] == 'f'):
                            print(Fore.GREEN + "\u2588", end="")
                        elif (self.Maze.maze[i][j] == 'c'):
                            print(Fore.GREEN + ' ', end="")
                        else:
                            print(Fore.RED +  "\u2593", end="")

    def addPathToMaze(self, path, symbol='p'):
        newMaze = self.Maze.maze
        lenPath = len(path)
        for i in range(lenPath):
            x,y = path[i]
            newMaze[x][y]=symbol
        return newMaze

    # def startFinishPoints(self):
    #     start = [i for i in range(len(self.Maze.maze[0])) if self.Maze.maze[0][i] == 'c']
    #     finish = [i for i in range(len(self.Maze.maze[0])) if self.Maze.maze[len(self.Maze.maze)-1][i] == 'c']
    #     return [0, start[0]], [len(self.Maze.maze) - 1, finish[0]]
    
    def solveMaze(self, showPath=0):
        # start, end = self.startFinishPoints()
        self.gotoxy(1, 0)
        print(Fore.WHITE + "A* Algorithm", end="")
        startTime = time.time()
        self.addPathToMaze(self.search(self.Maze.start, self.Maze.end, showPath), 'f')
        endTime = time.time()
        self.printMazeXY()
        self.gotoxy(1, self.Maze.height+2)
        print(Fore.WHITE + "Passos: " + str(self.errorSteps), end="")
        self.gotoxy(1, self.Maze.height+3)
        print(Fore.WHITE + "Passos errados: " + str(self.errorSteps-self.steps), end="")
        self.gotoxy(1, self.Maze.height+4)
        print(Fore.WHITE + "Tempo de resolucao: ", end="")
        self.gotoxy(1, self.Maze.height+5)
        print(Fore.WHITE + str(endTime-startTime) + " segundos", end="")

