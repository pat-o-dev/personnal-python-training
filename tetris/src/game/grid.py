import pygame
from utils import draw_cell
import numpy as np

class Grid:
    def __init__(self, config, color, border_color):
        self.width, self.height = config.get_grid_size()
        self.bloc_size = config.get_bloc_size()
        self.grid = np.empty((self.height, self.width), dtype=object)# on inverse abs et ord plus simple pour trouver les tetris
        self.offset = pygame.Vector2(config.get_grid_offset())
        self.color = color
        self.border_color = border_color
        self.border_width = 1
        
    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                color = value if value is not None else self.color
                draw_cell(screen, color, pygame.Vector2(x, y), self.bloc_size, self.border_color, self.offset, self.border_width)