from deepSearch import *
from heuristicSearch import *
from Maze import *
import os
#To change the default size of maze send height=? and width=?
maze = Maze(height=40, width=60)
os.system('cls')

heuristic = HeuristicSearch(maze)
deep = DeepSearch(maze)
# To se the algorithm in real time send showPath=1
<<<<<<< Updated upstream
deep.solveMaze(1)
heuristic.solveMaze(1)
=======
blind.solveMaze(1)
heuristic.solveMaze()

>>>>>>> Stashed changes
