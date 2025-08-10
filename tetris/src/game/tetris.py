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
        self.pieces = [self.get_random_piece() for _ in range(5)]
    
    def get_random_piece(self):
        shape_idx = random.choice(list(self.shapes.keys()))
        shape_obj = self.shapes.get(shape_idx)
        shape = shape_obj.get("shape")
        color = self.colors.get(shape_obj.get("color"))
        position = pygame.Vector2(4, 4)
        border_color = self.colors.get("black")
        return Piece(shape, color, position, self.bloc_size, border_color)
    
    def next_piece(self):
        self.pieces.pop(0)
        self.pieces.append(self.get_random_piece())
    
    def update(self, delta):
        pass
    
    def draw(self):
        self.screen.fill(self.colors.get("black"))
        self.grid.draw(self.screen)
        
        # piece active
        self.pieces[0].draw(self.screen, self.grid.offset + pygame.Vector2((self.grid.width // 2) - 1, 0) * self.bloc_size)
        # pieces a venir
        pieces_preview = pygame.Vector2(self.config.get_pieces_preview_position())
        for i, piece in enumerate(self.pieces[1:], start=1):
            piece.draw(self.screen, pieces_preview * self.bloc_size)
            pieces_preview.y += len(piece.shape) + 1 # decalle preview de la taille de la piece +1

        pygame.display.flip() 