import pygame
from utils import draw_cell
import numpy as np

class Grid:
    def __init__(self, config):
        self.width, self.height = config.get_grid_size()
        self.bloc_size = config.get_bloc_size()
        self.grid = np.empty((self.height, self.width), dtype=object)# on inverse abs et ord plus simple pour trouver les tetris
        self.offset = pygame.Vector2(config.get_grid_offset())
        
    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                print(f"value {value}")
                draw_cell(screen, (255,0,0), pygame.Vector2(x, y), self.bloc_size, (0,255,0), self.offset, 1)