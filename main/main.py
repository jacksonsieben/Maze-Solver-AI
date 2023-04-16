from blindSearch import *
from heuristicSearch import *
from Maze import *
import os

maze = Maze()
os.system('cls')

aStar = AStar(maze)
blind = blindSearch(maze)

blind.solveMaze()
aStar.solveMaze()
