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
        self.bloc_size = bloc_size
    
    def update(self, movement):
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