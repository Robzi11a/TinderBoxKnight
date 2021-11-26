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
                level_array[self.row][self.column], level_array[self.row][self.column+1] = "d", 'kl'
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
                level_array[self.row][self.column], level_array[self.row+1][self.column] = "d", 'kl'
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

        

# not sure what this code is doing - left it in just in case        

"""        
        self.id = id
        self.x, self.y = int(x+6), int(y)
        self.myinc = .05
        self.knight_image = ""
        if knight_kind == "k":
            self.knight_image = floor.KNIGHT_DARK_BACKGROUND
        else:
            s = "unrecognized format: {}".format(knight_kind)
            raise ValueError(s)
        
        image_path = os.path.join("levels", "images")
        self.image = pygame.image.load(os.path.join(image_path, self.knight_image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

    def move(self, x, y):
        if not utils.in_range(self.x, x, .05):
            if self.x < x:
                self.x += self.myinc
            elif self.x > x:
                self.x -= self.myinc
            else:
                self.x = x

        if not utils.in_range(self.y, y, .05):
            if self.y < y:
                self.y += self.myinc
            elif self.y > y:
                self.y -= self.myinc
            else:
                self.y = y
        

    def debug_print(self):
        s = "id: {}, x: {}, y: {}".format(self.id, self.x, self.y)
        print(s)
"""
