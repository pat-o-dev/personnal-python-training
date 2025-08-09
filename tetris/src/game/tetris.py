import pygame
import random
from game.grid import Grid
from game.piece import Piece

class Tetris:
    def __init__(self, screen, config):
        self.running = True
        self.screen = screen
        self.config = config
        self.bloc_size = config.get_bloc_size()
        self.colors = config.get_colors()
        self.grid = Grid(self.config, self.colors.get("black"), self.colors.get("pink"))
        self.shapes = config.get_shapes()
        self.piece = self.get_random_piece()
    
    def get_random_piece(self):
        shape_idx = random.choice(list(self.shapes.keys()))
        shape_obj = self.shapes.get(shape_idx)
        shape = shape_obj.get("shape")
        color = self.colors.get(shape_obj.get("color"))
        position = pygame.Vector2(4, 4)
        border_color = self.colors.get("black")
        return Piece(shape, color, position, self.bloc_size, border_color)
        
    def update(self, delta):
        pass
    
    def draw(self):
        self.screen.fill(self.colors.get("black"))
        self.grid.draw(self.screen)
        self.piece.draw(self.screen, pygame.Vector2(1, 1))
        pygame.display.flip() 