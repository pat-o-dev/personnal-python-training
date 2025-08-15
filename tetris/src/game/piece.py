import pygame
from utils.draw import draw_cell
import numpy as np

class Piece:
    def __init__(self, shape, color, position, bloc_size, border_color, border_width=1, active=True):
        self.shape = np.array(shape)
        self.color = color
        self.position = position # Vector2
        self.border_color = border_color
        self.border_width = border_width
        self.active = active
        self.is_drop = False
        self.is_lock = False
        self.bloc_size = bloc_size
    
    '''
    def is_valid_position(self, grid, movement):
        new_x = self.position[0] + movement[0]
        new_y = self.position[1] + movement[1]
        # controle avec les dimensions de la grille
        if new_x < 0 or new_x + self.current_shape.shape[1] > grid.shape[1]:  # Out of width
            return False
        if new_y + self.current_shape.shape[0] > grid.shape[0]:  # On the floor
            self.on_the_floor = True
            return False

        return True
    '''
    
    def update(self, grid, movement, rotate):
        
        # TODO check avec rotate
        new_position = self.position + movement
        if new_position.x < 0 or (new_position.x + self.shape.shape[1]) > grid.width:
            movement.x = 0
        if new_position.y + self.shape.shape[0] > grid.height:
            movement.y = 0
            if self.is_drop:
                self.is_lock = True
                return False
            self.is_drop = True
        if rotate is True:
            self.shape = np.rot90(self.shape)
        self.position += movement
        #print(f"current position: {self.position}")
    
    def draw(self, screen, offset):
        for y, x in np.ndindex(self.shape.shape):
            if self.shape[y, x] == 1:
                draw_cell(
                    screen, 
                    self.color, 
                    pygame.Vector2(self.position.x + x, self.position.y + y), 
                    self.bloc_size, 
                    self.border_color, 
                    offset, 
                    self.border_width
                )