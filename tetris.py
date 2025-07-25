# creation rapide d un Tetris basique avec pygame
import pygame
import random

pygame.init()
pygame.font.init()

# liste des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# liste des textes
FONT_SIZE = 30
FONT = pygame.font.SysFont('Arial', FONT_SIZE)
TEXT_PAUSE = FONT.render("Pause", True, WHITE)

# taille de la grille
GRID_WIDTH, GRID_HEIGHT = 10, 20
# taille d un bloc en px
BLOC_SIZE = 30
# calcul de la taille de la fenetre
WINDOW_WIDTH = GRID_WIDTH * BLOC_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOC_SIZE

# liste des formes
SHAPE_L = [(0,0), (0,1), (0,2), (1,2)]
SHAPE_LR = [(0,0), (0,1), (0,2), (1,0)]
SHAPE_T = [(0,1), (1,0), (1,1), (1,2)]
SHAPE_I = [(0,0), (1,0), (2,0), (3,0)]
SHAPE_O = [(0,0), (0,1), (1,0), (1,1)]
SHAPE_S = [(0,1), (0,2), (1,0), (1,1)]
SHAPE_SR = [(0,0), (0,1), (1,1), (1,2)]

SHAPES = [SHAPE_L, SHAPE_LR, SHAPE_T, SHAPE_I, SHAPE_O, SHAPE_S, SHAPE_SR]

SPAWN_X, SPAWN_Y = 3, 3

def main():
    clock = pygame.time.Clock()
    running = True
    pause = False
    shape = random.choice(SHAPES)
    shape_position = pygame.Vector2(SPAWN_X, SPAWN_Y)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # press X or DELETE pour quit
                if event.key in (pygame.K_x, pygame.K_DELETE):
                    running = False
                # press ESCAPE pour pause
                if event.key in (pygame.K_ESCAPE, pygame.K_p):
                    pause = not pause
                if event.key == pygame.K_s:
                    shape = random.choice(SHAPES)
                    shape_position = pygame.Vector2(SPAWN_X, SPAWN_Y)
                if event.key in (pygame.K_a, pygame.K_LEFT):
                    shape_position.x -= 1
                if event.key in (pygame.K_d, pygame.K_RIGHT):
                    shape_position.x += 1
                if event.key in (pygame.K_s, pygame.K_DOWN):
                    shape_position.y += 1
                
        # couleur fond
        screen.fill(BLACK)
        
        # passe la game en pause
        if pause == True:
            screen.blit(TEXT_PAUSE, ((WINDOW_WIDTH - TEXT_PAUSE.get_width()) / 2,(WINDOW_HEIGHT - TEXT_PAUSE.get_height()) / 2))
        
        # affiche une grille des cases    
        pygame.draw.rect(screen, WHITE, (0,0,BLOC_SIZE, BLOC_SIZE), 1)
        
        for dx, dy in shape:
            pygame.draw.rect(
                screen,
                RED,
                ((shape_position.x + dx) * BLOC_SIZE, (shape_position.y + dy) * BLOC_SIZE, BLOC_SIZE, BLOC_SIZE)
            )
        
        # mise a jour rendu
        pygame.display.flip()
        # 60 fps
        clock.tick(60)
    
    pygame.quit()

# init window
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# execute la mainloop pygame
if __name__ == "__main__":
    main()