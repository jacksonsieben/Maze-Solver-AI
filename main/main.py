from blindSearch import *
from heuristicSearch import *
from Maze import *
import os
#To change the default size of maze send height=? and width=?
maze = Maze()
os.system('cls')

heuristic = HeuristicSearch(maze)
blind = BlindSearch(maze)
# To se the algorithm in real time send showPath=1
blind.solveMaze()
heuristic.solveMaze()
