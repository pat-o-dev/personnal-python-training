# creation rapide d un Tetris basique avec pygame
import pygame
import random

pygame.init()

# liste des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# taille de la grille
GRID_WIDTH, GRID_HEIGHT = 10, 20
# taille d un bloc en px
BLOC_SIZE = 30
# calcul de la taille de la fenetre
WINDOW_WIDTH = GRID_WIDTH * BLOC_SIZE

# liste des formes
SHAPE_L = [(0,0), (0,1), (0,2), (1,2)]
SHAPE_LR = [(0,0), (0,1), (0,2), (1,0)]
SHAPE_T = [(0,1), (1,0), (1,1), (1,2)]
SHAPE_I = [(0,0), (1,0), (2,0), (3,0)]
SHAPE_O = [(0,0), (0,1), (1,0), (1,1)]
SHAPE_S = [(0,1), (0,2), (1,0), (1,1)]
SHAPE_SR = [(0,0), (0,1), (1,1), (1,2)]

SHAPES = [SHAPE_L, SHAPE_LR, SHAPE_T, SHAPE_I, SHAPE_O, SHAPE_S, SHAPE_SR]

print("Hello Tetris")

for i in range(10):
    shape = random.choice(SHAPES)
    print(shape)
    
shapes = random.sample(SHAPES, 3)
print(shapes)

