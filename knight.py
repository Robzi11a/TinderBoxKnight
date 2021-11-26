import pygame

from tiles import TILES_HORIZONTAL, TILES_VERTICAL
 

class Knight:
    # Initialise knight to store the knight's starting row and column
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.previous_tile = "d"
        self.next_tile = ""

    # Updates the row and column stored for the knight. Called whenever the knight moves to new position.
    def update_position(self, row, column):
        self.row = row
        self.column = column
    
    def reset_tile_memory(self):
        self.previous_tile = "d"
        self.next_tile = ""

    def return_position(self):
        return self.row, self.column
    
    def move_right(self, level_array):
        if self.column + 1 < TILES_HORIZONTAL:          
            movement_code = self.check_move("right", level_array)
            if movement_code == 0:
                self.next_tile =  level_array[self.row][self.column+1]          
                level_array[self.row][self.column], level_array[self.row][self.column+1] = self.previous_tile, 'kd'   
                self.column += 1
                self.previous_tile = self.next_tile
                return True     
            elif movement_code == 1:
                self.next_tile = level_array[self.row][self.column+1] 
                level_array[self.row][self.column], level_array[self.row][self.column+1] = self.previous_tile, 'kl'
                self.column += 1
                self.previous_tile = self.next_tile
                return True
            elif movement_code == 2:
                level_array[self.row][self.column+1] = 'ls'
                return False       
        return True

    def move_left(self, level_array):
        if self.column - 1 >= 0:
            self.next_tile =  level_array[self.row][self.column-1]
            movement_code = self.check_move("left", level_array) 
            if movement_code == 0:           
                level_array[self.row][self.column], level_array[self.row][self.column-1] = self.previous_tile, 'kd'   
                self.previous_tile = self.next_tile
                self.column -= 1
                return True       
            elif movement_code == 1:
                level_array[self.row][self.column], level_array[self.row][self.column-1] = self.previous_tile, 'kl'
                self.previous_tile = self.next_tile
                self.column -= 1
                return True
            elif movement_code == 2:
                level_array[self.row][self.column-1] = 'ls'
                return False
        return True

    def move_up(self, level_array):
        if self.row - 1 >= 0:
            self.next_tile =  level_array[self.row-1][self.column]
            movement_code = self.check_move("up", level_array) 
            if movement_code == 0:           
                level_array[self.row][self.column], level_array[self.row-1][self.column] = self.previous_tile, 'kd'   
                self.previous_tile = self.next_tile
                self.row -= 1
                return True       
            elif movement_code == 1:
                level_array[self.row][self.column], level_array[self.row-1][self.column] = self.previous_tile, 'kl'
                self.previous_tile = self.next_tile
                self.row -= 1
                return True
            elif movement_code == 2:
                level_array[self.row-1][self.column] = 'ls'
                return False
        return True

    def move_down(self, level_array):
        if self.row + 1 < TILES_VERTICAL:
            self.next_tile =  level_array[self.row+1][self.column]
            movement_code = self.check_move("down", level_array) 
            if movement_code == 0:           
                level_array[self.row][self.column], level_array[self.row+1][self.column] = self.previous_tile, 'kd'   
                self.previous_tile = self.next_tile
                self.row += 1
                return True       
            elif movement_code == 1:
                level_array[self.row][self.column], level_array[self.row+1][self.column] = self.previous_tile, 'kl'
                self.previous_tile = self.next_tile
                self.row += 1
                return True
            elif movement_code == 2:
                level_array[self.row+1][self.column] = 'ls'
                return False
        return True

    # Check that the knight is not moving into an enemy or other barrier. 
    # Return 0 for dark square, 1 for light square, 2 for enemy, and 3 for anything else. 
    def check_move(self, direction, level_array):
        if direction == "right":
            square = level_array[self.row][self.column+1] 
            if square == 'd':
                return 0
            elif square == 'l':
                return 1
            elif self.check_for_enemy(level_array[self.row][self.column+1]): 
                return 2 
            else:
                return 3
        if direction == "up":
            square = level_array[self.row-1][self.column] 
            if square == 'd': 
                return 0
            elif square == 'l':
                return 1
            elif self.check_for_enemy(level_array[self.row-1][self.column]):
                return 2
            else: 
                return 3

        if direction == "left":
            square = level_array[self.row][self.column-1]
            if square == 'd': 
                return 0
            elif square == 'l':
                return 1
            elif self.check_for_enemy(level_array[self.row][self.column-1]):
                return 2
            else:
                return 3

        if direction == "down":
            square = level_array[self.row+1][self.column]
            if square == 'd':
                return 0
            elif square == 'l':
                return 1
            elif self.check_for_enemy(level_array[self.row+1][self.column]):
                return 2 
            else: 
                return 3

    def check_for_enemy(self, square):
        if square == 'hs':
            return True
        return False

    def reset_knight_position(self, level_array):
        if level_array[9][0] == "l":
            level_array[9][0] = "kl"
        else: 
            level_array[9][0] = "kd"
        if level_array[self.row][self.column] == "kd":
            level_array[self.row][self.column] = "d"
        else: 
            level_array[self.row][self.column] = "l"
        self.row, self.column = 9, 0
        self.reset_tile_memory()