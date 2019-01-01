"""
Clone of 2048 game.
"""

import poc_2048_gui

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    merged_line = list(line)
    
    for rplace in merged_line:
        if rplace == 0:
            merged_line.remove(0)
            merged_line.append(0)

    for mrg in range(len(merged_line)-1):
        if merged_line[mrg] == merged_line[mrg+1]:
            merged_line[mrg] = (merged_line[mrg] * 2)
            merged_line.pop(mrg+1)
            merged_line.append(0)
    
    return merged_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
                
        self.directions = {UP:[[0,direct] for direct in range(self.grid_width)],
                          DOWN:[[self.grid_height - 1, direct] for direct in range(self.grid_height)],
                          LEFT:[[direct,0] for direct in range(self.grid_height)],
                          RIGHT:[[direct, self.grid_width - 1] for direct in range(self.grid_width)]
                         }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]

        for i in [1,2]:
            coordinat_num_x = random.randrange(0,self.grid_width)
            coordinat_num_y = random.randrange(0,self.grid_height)
            self.cells[coordinat_num_y][coordinat_num_x] = random.choice([2,4])

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        for direct in self.directions[direction]:
            coord = list(direct)
            tmp_list = []
            merged_list = []

            for cell in range(self.grid_width):
                tmp_list.append(self.cells[coord[0]][coord[1]])
                merged_list.append([coord[0], coord[1]])
                coord[0] += OFFSETS[direction][0]
                coord[1] += OFFSETS[direction][1]

            before = list(tmp_list)
            tmp_list = merge(tmp_list)

            if before != tmp_list:
                for tmp in range(len(tmp_list)):
                    self.set_tile(merged_list[tmp][0],merged_list[tmp][1],tmp_list[tmp])
        if before != tmp_list:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code

        for col in range(self.grid_height):
            for row in range(self.grid_width):
                if self.cells[col][row] == 0:
                    coordinat_num_x = random.randrange(0,self.grid_width)
                    coordinat_num_y = random.randrange(0,self.grid_height)
                    self.cells[coordinat_num_y][coordinat_num_x] = random.choice([2,4])
                    break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.cells[row][col]

    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
