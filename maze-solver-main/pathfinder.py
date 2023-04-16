from array import *

import sys
import os
import copy
import heapq
from collections import deque
from queue import PriorityQueue
from math import sqrt
import time
from colorama import Fore


map = [ ['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], 
        ['w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'w', 'c', 'w'], 
        ['w', 'c', 'c', 'w', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'w'], 
        ['w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w'], 
        ['w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'w', 'c', 'c', 'w'], 
        ['w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'w'], 
        ['w', 'w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w', 'w'], 
        ['w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'w', 'c', 'c', 'w'], 
        ['w', 'w', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'w'], 
        ['w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w'], 
        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']]

start = (0,1)
end = (10,11)

height = 12
width = 13

class node:
    def __init__(self, parent, pos, cost):
        self.parent = parent
        self.pos = pos
        self.cost = cost

def gotoxy(x,y):
	print ("%c[%d;%df" % (0x1B, y, x), end='')

# Utility function to print the map
def print_array(array):
    for i in range(0, height):
        for j in range(0, width):
            if (j < len(array)):
                print(array[i][j], end = " ")
            else:
                print(array[i][j], end = '')
        print()

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

def sortkey(node):
    return node.cost

#Given a node, get its valid children and their cumilitve cost

#Given a node, get its valid children and their cost including heuristic
def getChildrenAstar(parent, tracker, goal):
    new_children = []
    #Defines the range of movement
    move = [[-1,0], # up
            [1,0], # down
            [0,-1], # left
            [0,1]] # right


    for i in range(0, len(move)):
        new_pos = move[i]

        #Move to next position
        next_pos = (parent.pos[0] + new_pos[0], parent.pos[1] + new_pos[1])

        # Check for valid position
        if(next_pos[0] == -1 or next_pos[1] == -1 or next_pos[0] >= height or next_pos[1] >= width):
            continue
        elif(map[next_pos[0]][next_pos[1]] == 'w'):
            continue
        elif(tracker[next_pos[0]][next_pos[1]] == True):
            continue
        else:

            g =  0 + 1
            

            #Manhattan Heuristic Calculation -> h = |xstart - xdestination| + |ystart - ydestination|
            # if (heuristic == "manhattan"):
            h = abs((next_pos[0] - goal[0])) + abs((next_pos[1] - goal[1]))

            #Euclidean Heuristic Calculation -> h = sqrt((xstart - xdestination)^2 + (ystart - ydestination)^2)
            # if (heuristic == "euclidean"):
            #     h = sqrt(((next_pos[0] - goal[0]) ** 2) + ((next_pos[1] - goal[1]) ** 2))

            f = g + h
            new_cost = f
            new_node = node(parent, next_pos, new_cost)
            new_children.append(new_node)


    return new_children


def astar(start_c, end_c):
    global map

    #Initialize the visited array
    visited = []
    for i in range (0, height):
        templist = []
        for j in range (0, width):
            templist.append(False)
        visited.append(templist)

    start = node("None", start_c, 0)
    current = start
    queue = deque([])
    visited[start.pos[0]][start.pos[1]] = True
    queue.append(start)

    found = False

    while queue:
        #Pop the current node
        current = queue.popleft()

        #Check is current is end
        if(current.pos == end_c):
            found = True
            break

        #Get the children of current
        children = getChildrenAstar(current, visited, end_c)

        #Sort children by cost
        children.sort(key=sortkey)

        #Mark as visited and add to queue
        for i in range(0, len(children)):
            visited[children[i].pos[0]][children[i].pos[1]] = True
            queue.append(children[i])


    # Step back through the map to update the shortest path
    if(found == True):
        while current.parent != "None":
            map[current.pos[0]][current.pos[1]] = '*'
            current = current.parent
        map[current.pos[0]][current.pos[1]] = '*'

        print_array(map)

    else:
        print("null")


print_array(map)
print()
astar((start),(end))

