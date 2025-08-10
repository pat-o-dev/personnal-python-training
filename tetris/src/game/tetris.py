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
        self.move_down_timer = 0
        self.move_down_interval = 500 #ms
    
    def get_random_piece(self):
        shape_idx = random.choice(list(self.shapes.keys()))
        shape_obj = self.shapes.get(shape_idx)
        shape = shape_obj.get("shape")
        color = self.colors.get(shape_obj.get("color"))
        position = pygame.Vector2(0, 0) + pygame.Vector2((self.grid.width // 2) - 1, 0)
        border_color = self.colors.get(shape_obj.get("border_color"))
        return Piece(shape, color, position, self.bloc_size, border_color)
    
    def next_piece(self):
        self.pieces.pop(0)
        self.pieces.append(self.get_random_piece())
    
    def update(self, actions, delta):
        piece_movement = pygame.Vector2(0, 0)
        if "move_left" in actions:
            piece_movement.x -=1
        if "move_right" in actions:
            piece_movement.x += 1
        if "drop" in actions:
            piece_movement.y += 1
        if "rotate" in actions:
            #todo rotate
            pass
        if "pause" in actions:
            #todo pause
            pass
        if "quit" in actions:
            #todo quit
            pass
        
        self.move_down_timer += delta
        if self.move_down_timer > self.move_down_interval: # drop timer
            self.move_down_timer = 0
            piece_movement.y = 1 # on ne descend jamais de 2 donc pas +=
        self.pieces[0].update(piece_movement) # deplace la piece
    
    def draw(self):
        self.screen.fill(self.colors.get("black"))
        self.grid.draw(self.screen)
        
        # piece active
        self.pieces[0].draw(self.screen, self.grid.offset)
        # pieces a venir
        pieces_preview = pygame.Vector2(self.config.get_pieces_preview_position())
        for i, piece in enumerate(self.pieces[1:], start=1):
            piece.draw(self.screen, pieces_preview * self.bloc_size)
            pieces_preview.y += len(piece.shape) + 1 # decalle preview de la taille de la piece +1

        pygame.display.flip() 