# creation rapide d un Tetris basique avec pygame
import pygame
import random

pygame.init()
pygame.font.init()

DEBUG_MODE = True

FPS = 60

# liste des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY_ALPHA = pygame.Color(128, 128, 128, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLORS = [RED, BLUE, GREEN]

# liste des textes
FONT_SIZE = 30
FONT = pygame.font.SysFont('Arial', FONT_SIZE)
TEXT_PAUSE = FONT.render("Pause", True, WHITE, GRAY_ALPHA)

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

# position depart nouvelle piece
SPAWN = pygame.Vector2(4, -3)

# liste des touches
CONTROL_PAUSE = [pygame.K_ESCAPE, pygame.K_p]
CONTROL_QUIT = [pygame.K_x, pygame.K_DELETE]
CONTROL_LEFT = [pygame.K_a, pygame.K_LEFT]
CONTROL_RIGHT = [pygame.K_d, pygame.K_RIGHT]
CONTROL_DOWN = [pygame.K_s, pygame.K_DOWN]
CONTROL_NEW = [pygame.K_n]
   
def draw_grid():
    for grid_x in range(GRID_WIDTH):
        for grid_y in range(GRID_HEIGHT):
            pos_x = grid_x * BLOC_SIZE
            pos_y = grid_y * BLOC_SIZE
            pygame.draw.rect(screen, WHITE, (pos_x, pos_y, pos_x + BLOC_SIZE, pos_y + BLOC_SIZE), 1)

def draw_pause():
    screen.blit(TEXT_PAUSE, ((WINDOW_WIDTH - TEXT_PAUSE.get_width()) / 2,(WINDOW_HEIGHT - TEXT_PAUSE.get_height()) / 2))

class Piece:
    def __init__(self, force_shape=None):
        if force_shape == None:
            self.shape = random.choice(SHAPES)
        elif force_shape in SHAPES:
            self.shape = force_shape
        else:
            raise ValueError("Error: Shape not exist.") 
        self.position = pygame.Vector2(SPAWN.x, SPAWN.y)
        self.color = random.choice(COLORS)
    
    def move(self, movement):
        self.position += pygame.Vector2(movement.x, movement.y)
        
    def draw(self):
        for dx, dy in self.shape:
            pygame.draw.rect(
                screen,
                self.color,
                ((self.position.x + dx) * BLOC_SIZE, (self.position.y + dy) * BLOC_SIZE, BLOC_SIZE, BLOC_SIZE)
            )

class Tetris:
    def __init__(self):
        self.running = True
        self.pause = False
        self.piece = Piece()
        self.piece_movement = pygame.Vector2()
        self.move_down_timer = 0
        self.move_down_interval = 500 #ms
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                # press X or DELETE pour quit
                if key in CONTROL_QUIT:
                    self.running = False
                # press ESCAPE pour pause
                if key in CONTROL_PAUSE:
                    self.pause = not self.pause
                # pour debug, charge une nouvelle piece
                if key in CONTROL_NEW and DEBUG_MODE:
                    self.piece = Piece()
                # deplacement piece
                if key in CONTROL_LEFT:
                    self.piece_movement.x -= 1
                if key in CONTROL_RIGHT:
                    self.piece_movement.x += 1
                if key in CONTROL_DOWN:
                    self.piece_movement.y += 1
    
    def update(self, delta):
        if self.pause == False:
            self.move_down_timer += delta # recupere le temps passe - change selon le FPS reel
            if self.move_down_timer > self.move_down_interval:
                self.move_down_timer = 0
                self.piece_movement.y += 1
            self.piece.move(self.piece_movement)  # mise a jour de la position
        self.piece_movement = pygame.Vector2(0, 0)
    
    def draw(self):
        screen.fill(BLACK) # couleur fond
        self.piece.draw() # affiche la piece
        if DEBUG_MODE:
            draw_grid() # affiche une grille des cases               
        if self.pause == True:
            draw_pause() # affiche la pause
        pygame.display.flip() # mise a jour rendu

def main():
    clock = pygame.time.Clock()
    game = Tetris()
    while game.running:
        delta = clock.tick(FPS)
        game.handle_events() # capture des touches
        game.update(delta) # mise a jour des donnees
        game.draw() # affichage
    pygame.quit()

# init window
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# execute la mainloop pygame
if __name__ == "__main__":
    main()