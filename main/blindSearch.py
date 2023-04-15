

class blindSearch:
    
    def __init__(self, maze):
        self.maze = maze
        backCounter = 0

    def get_starting_finishing_points(self):
        _start = [i for i in range(len(self.maze[0])) if self.maze[0][i] == 'c']
        _end = [i for i in range(len(self.maze[0])) if self.maze[len(self.maze)-1][i] == 'c']
        return [0, _start[0]], [len(self.maze) - 1, _end[0]]
    
    def search(self):
        current_cell = self.rat_path[len(self.rat_path) - 1]

        if current_cell == self.finish:
            return

        if self.maze[current_cell[0] + 1][current_cell[1]] == 'c':
            self.maze[current_cell[0] + 1][current_cell[1]] = 'p'
            self.rat_path.append([current_cell[0] + 1, current_cell[1]])
            self.search()
        # elif self.maze[current_cell[0]][current_cell[1]] == 'w':
            

        if self.maze[current_cell[0]][current_cell[1] + 1] == 'c':
            self.maze[current_cell[0]][current_cell[1] + 1] = 'p'
            self.rat_path.append([current_cell[0], current_cell[1] + 1])
            self.search()

        if self.maze[current_cell[0] - 1][current_cell[1]] == 'c':
            self.maze[current_cell[0] - 1][current_cell[1]] = 'p'
            self.rat_path.append([current_cell[0] - 1, current_cell[1]])
            self.search()

        if self.maze[current_cell[0]][current_cell[1] - 1] == 'c':
            self.maze[current_cell[0]][current_cell[1] - 1] = 'p'
            self.rat_path.append([current_cell[0], current_cell[1] - 1])
            self.search()

        # If we get here, this means that we made a wrong decision, so we need to
        # backtrack
        current_cell = self.rat_path[len(self.rat_path) - 1]
        if current_cell != self.finish:
            cell_to_remove = self.rat_path[len(self.rat_path) - 1]
            self.rat_path.remove(cell_to_remove)
            self.maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'
            self.backCounter += 1

    def getPath(self):
        return self.rat_path