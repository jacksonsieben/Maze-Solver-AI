from Maze import *
from aStar import *

maze = Maze()
mazeGrid = maze.generateMaze()

aStar = AStar(mazeGrid)
aStar.solveMaze()