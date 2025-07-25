# creation rapide d un Tetris basique avec pygame
import pygame
import random

pygame.init()
pygame.font.init()

DEBUG_MODE = True

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

SPAWN = pygame.Vector2(4, -3)

CONTROL_PAUSE = [pygame.K_ESCAPE, pygame.K_p]
CONTROL_QUIT = [pygame.K_x, pygame.K_DELETE]
CONTROL_LEFT = [pygame.K_a, pygame.K_LEFT]
CONTROL_RIGHT = [pygame.K_d, pygame.K_RIGHT]
CONTROL_DOWN = [pygame.K_s, pygame.K_DOWN]
CONTROL_NEW = [pygame.K_n]

def get_shape():
    return random.choice(SHAPES), pygame.Vector2(SPAWN.x, SPAWN.y)
        
def main():
    clock = pygame.time.Clock()
    running = True
    pause = False
    # init de la piece
    shape, shape_position = get_shape()
    # timer descente piece 
    move_down_timer = 0
    move_down_interval = 500
    while running:
        shape_movement = pygame.Vector2(0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                # press X or DELETE pour quit
                if key in CONTROL_PAUSE:
                    running = False
                # press ESCAPE pour pause
                if key in CONTROL_QUIT:
                    pause = not pause
                # pour debug, charge une nouvelle piece
                if key in CONTROL_NEW and DEBUG_MODE:
                    shape, shape_position = get_shape()
                # deplacement piece
                if key in CONTROL_LEFT:
                    shape_movement.x -= 1
                if key in CONTROL_RIGHT:
                    shape_movement.x += 1
                if key in CONTROL_DOWN:
                    shape_movement.y += 1
                
        # couleur fond
        screen.fill(BLACK)
        
        # passe la game en pause
        if pause == True:
            screen.blit(TEXT_PAUSE, ((WINDOW_WIDTH - TEXT_PAUSE.get_width()) / 2,(WINDOW_HEIGHT - TEXT_PAUSE.get_height()) / 2))
        
        # affiche une grille des cases 
        for grid_x in range(GRID_WIDTH):
            for grid_y in range(GRID_HEIGHT):
                pos_x = grid_x * BLOC_SIZE
                pos_y = grid_y * BLOC_SIZE
                pygame.draw.rect(screen, WHITE, (pos_x, pos_y, pos_x + BLOC_SIZE, pos_y + BLOC_SIZE), 1)
        
        # recupere le temps passe - change selon le FPS reel
        # mise a jour de la position
        if pause == False:
            # todo modifier calcul timer en tenant compte de la pause
            move_down_timer += clock.get_time()
            if move_down_timer > move_down_interval:
                move_down_timer = 0
                shape_movement.y += 1
        
            shape_position += shape_movement
            
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