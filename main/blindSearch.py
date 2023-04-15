import os
from colorama import Fore
import time

class blindSearch:
    
    def __init__(self, maze, height=11, width=27):
        self.maze = maze
        self.steps = 0
        self.errorSteps = 0
        self.flag = 0
        self.rat_path = []
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

    def get_starting_finishing_points(self):
        _start = [i for i in range(len(self.maze[0])) if self.maze[0][i] == 'c']
        _end = [i for i in range(len(self.maze[0])) if self.maze[len(self.maze)-1][i] == 'c']
        return [0, _start[0]], [len(self.maze) - 1, _end[0]]
    
    def search(self, showPath=0):
        current_cell = self.rat_path[len(self.rat_path) - 1]
        self.steps += 1
        if self.flag == 1:
            return

        if current_cell == self.finish:
            self.flag = 1
            return self.flag
        elif showPath == 1:
            self.printMaze(self.maze)

        if self.maze[current_cell[0] + 1][current_cell[1]] == 'c' and current_cell is not self.finish and self.flag != 1:
            self.maze[current_cell[0] + 1][current_cell[1]] = 'p'
            self.rat_path.append([current_cell[0] + 1, current_cell[1]])
            self.search(showPath)

        if self.maze[current_cell[0]][current_cell[1] + 1] == 'c' and current_cell is not self.finish and self.flag != 1:
            self.maze[current_cell[0]][current_cell[1] + 1] = 'p'
            self.rat_path.append([current_cell[0], current_cell[1] + 1])
            self.search(showPath)

        if self.maze[current_cell[0] - 1][current_cell[1]] == 'c' and current_cell is not self.finish and self.flag != 1:
            self.maze[current_cell[0] - 1][current_cell[1]] = 'p'
            self.rat_path.append([current_cell[0] - 1, current_cell[1]])
            self.search(showPath)

        if self.maze[current_cell[0]][current_cell[1] - 1] == 'c' and current_cell is not self.finish and self.flag != 1:
            self.maze[current_cell[0]][current_cell[1] - 1] = 'p'
            self.rat_path.append([current_cell[0], current_cell[1] - 1])
            self.search(showPath)

        # If we get here, this means that we made a wrong decision, so we need to
        # backtrack
        
        current_cell = self.rat_path[len(self.rat_path) - 1]
        if current_cell != self.finish:
            cell_to_remove = self.rat_path[len(self.rat_path) - 1]
            self.rat_path.remove(cell_to_remove)
            self.maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'
            self.errorSteps += 1
    
    def solveMaze(self):
        self.start, self.finish = self.get_starting_finishing_points()
        self.maze[self.start[0]][self.start[1]] = 'p'

        self.rat_path = [self.start]
        os.system("cls")
        start = time.time()
        self.search()
        end = time.time()
        self.printMaze(self.maze)

        self.gotoxy(0, self.height+3)
        print("Passos errados: " + str(self.errorSteps))
        print("Tempo de resolucao: " + str(end-start) + " segundos")

        