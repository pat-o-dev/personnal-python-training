import pygame
from game.grid import Grid

class Tetris:
    def __init__(self, screen, config):
        self.running = True
        self.screen = screen
        self.config = config
        self.colors = config.get_colors()
        self.grid = Grid(self.config)
        
    def update(self, delta):
        pass
    
    def draw(self):
        self.screen.fill(self.colors.get("black"))
        self.grid.draw(self.screen)
        pygame.display.flip() 