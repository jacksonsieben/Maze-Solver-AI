from colorama import Fore
import random
import time
from colorama import init
from colorama import Fore, Back, Style
import os

maze = []
height = 12
width = 22
backCounter = 0

def gotoxy(x,y):
	print ("%c[%d;%df" % (0x1B, y, x), end='')

def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells

def generateMaze(heightMaze=11, widthMaze=27):
	global maze, height, width
	## Main code
	# Init variables
	wall = 'w'
	cell = 'c'
	unvisited = 'u'
	height = heightMaze
	width = widthMaze
	maze = []

	# Initialize colorama
	init()

	# Denote all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	# Randomize starting point and set it a cell
	starting_height = int(random.random()*height)
	starting_width = int(random.random()*width)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	maze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	maze[starting_height-1][starting_width] = 'w'
	maze[starting_height][starting_width - 1] = 'w'
	maze[starting_height][starting_width + 1] = 'w'
	maze[starting_height + 1][starting_width] = 'w'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
				# Find the number of surrounding cells
				s_cells = surroundingCells(rand_wall)

				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

				s_cells = surroundingCells(rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'w'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

				s_cells = surroundingCells(rand_wall)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = 'c'

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'w'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'w'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'w'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)
		


	# Mark the remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				maze[i][j] = 'w'

	# Set entrance and exit
	for i in range(0, width):
		if (maze[1][i] == 'c'):
			maze[0][i] = 'c'
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == 'c'):
			maze[height-1][i] = 'c'
			break

	# Print final maze
	return maze

def get_starting_finishing_points():
	_start = [i for i in range(len(maze[0])) if maze[0][i] == 'c']
	_end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'c']
	return [0, _start[0]], [len(maze) - 1, _end[0]]


def printMaze(maze):
	
	for i in range(0, height):
		time.sleep(0.00001)
		for j in range(0, width):
			gotoxy(j+1,i+1)
			if (maze[i][j] == 'p'):
				print(Fore.WHITE + "\u2588", end="")
			elif (maze[i][j] == 'c'):
				print(Fore.GREEN + ' ', end="")
			else:
				print(Fore.RED +  "\u2593", end="")
			
		print()

def maze_solver():
	for i in range(0, height):
		for j in range(0, width):

			if maze[i][j] == 'c':
				print(Fore.GREEN, ' ', end="")
			elif maze[i][j] == 'p':
				print(Fore.BLUE, "\u2588", end="")
			else:
				print(Fore.RED, "\u2593", end="")
		print()


def escape(flag):
	global backCounter
	current_cell = rat_path[len(rat_path) - 1]

	if current_cell == finish and flag == 1:
		flag = 1
		return flag
	else:
		printMaze(maze)

	if maze[current_cell[0] + 1][current_cell[1]] == 'c' and current_cell is not finish and flag != 1:
		maze[current_cell[0] + 1][current_cell[1]] = 'p'
		rat_path.append([current_cell[0] + 1, current_cell[1]])
		flag = escape(flag)

	if maze[current_cell[0]][current_cell[1] + 1] == 'c' and current_cell is not finish and flag != 1:
		maze[current_cell[0]][current_cell[1] + 1] = 'p'
		rat_path.append([current_cell[0], current_cell[1] + 1])
		flag = escape(flag)

	if maze[current_cell[0] - 1][current_cell[1]] == 'c' and current_cell is not finish and flag != 1:
		maze[current_cell[0] - 1][current_cell[1]] = 'p'
		rat_path.append([current_cell[0] - 1, current_cell[1]])
		flag = escape(flag)

	if maze[current_cell[0]][current_cell[1] - 1] == 'c' and current_cell is not finish and flag != 1:
		maze[current_cell[0]][current_cell[1] - 1] = 'p'
		rat_path.append([current_cell[0], current_cell[1] - 1])
		flag = escape(flag)

	# If we get here, this means that we made a wrong decision, so we need to
	# backtrack
	
	current_cell = rat_path[len(rat_path) - 1]
	if current_cell != finish:
		cell_to_remove = rat_path[len(rat_path) - 1]
		rat_path.remove(cell_to_remove)
		maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'
		backCounter += 1

if __name__ == '__main__':
	maze = generateMaze(heightMaze=height, widthMaze=width)
	flag = 0
	start, finish = get_starting_finishing_points()
	maze[start[0]][start[1]] = 'p'

	rat_path = [start]
	os.system("cls")
	escape(flag)
	# maze_solver()
	
	printMaze(maze)
	# gotoxy(0,height+2)
	# print(backCounter)