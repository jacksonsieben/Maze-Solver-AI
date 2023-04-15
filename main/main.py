from blindSearch import *
from Maze import *

maze = Maze()
blind = blindSearch(maze.generateMaze())

blind.solveMaze()
