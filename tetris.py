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
SHAPE_L = [
    [(0,0), (0,1), (0,2), (1,2)], # 0 0deg
    [(0,0), (0,1), (1,0), (2,0)], # 1 90deg
    [(0,0), (1,0), (1,1), (1,2)], # 2 180deg
    [(2,0), (0,1), (1,1), (2,1)], # 3 270deg
]
SHAPE_LR = [
    [(1,0), (1,1), (1,2), (0,2)],   # 0
    [(0,0), (0,1), (1,1), (2,1)],   # 90
    [(0,0), (1,0), (0,1), (0,2)],   # 180
    [(0,0), (1,0), (2,0), (2,1)],   # 270
]
SHAPE_T = [
    [(0,1), (1,0), (1,1), (1,2)],   # 0
    [(0,0), (1,0), (1,1), (2,0)],   # 90
    [(1,0), (1,1), (1,2), (2,1)],   # 180
    [(0,1), (1,0), (1,1), (2,1)],   # 270
]
SHAPE_I = [
    [(0,0), (1,0), (2,0), (3,0)],   # 0
    [(1,0), (1,1), (1,2), (1,3)],  # 90
    [(0,1), (1,1), (2,1), (3,1)],   # 180
    [(2,0), (2,1), (2,2), (2,3)],  # 270
]
SHAPE_O = [
    [(0,0), (0,1), (1,0), (1,1)],
]
SHAPE_S = [
    [(0,1), (0,2), (1,0), (1,1)],   # 0
    [(0,0), (1,0), (1,1), (2,1)],   # 90
    [(0,1), (0,2), (1,0), (1,1)],   # 0
    [(0,0), (1,0), (1,1), (2,1)],   # 90
]
SHAPE_SR = [
    [(0,0), (0,1), (1,1), (1,2)],   # 0
    [(0,1), (1,0), (1,1), (2,0)],   # 90
]

SHAPES = [SHAPE_L, SHAPE_LR, SHAPE_T, SHAPE_I, SHAPE_O, SHAPE_S, SHAPE_SR]
SHAPES_COLORS = [RED, BLUE, GREEN]
# position depart nouvelle piece
SPAWN = pygame.Vector2(4, -3)

# liste des touches
CONTROL_PAUSE = [pygame.K_ESCAPE, pygame.K_p]
CONTROL_QUIT = [pygame.K_x, pygame.K_DELETE]
CONTROL_LEFT = [pygame.K_a, pygame.K_LEFT]
CONTROL_RIGHT = [pygame.K_d, pygame.K_RIGHT]
CONTROL_DOWN = [pygame.K_s, pygame.K_DOWN]
CONTROL_ROTATE = [pygame.K_r, pygame.K_UP]
CONTROL_NEW = [pygame.K_n]
   
class Grid:
    def __init__(self):
        # enregistre la grille None ou Code Couleur
        self.grid = []
        rows, cols = (GRID_WIDTH, GRID_HEIGHT)
        for i in range(rows):
            self.grid.append([None]*cols)
    
    def update(self, piece):
        pos_x = piece.position.x
        pos_y = piece.position.y
        for dx, dy in piece.shape[piece.rotation]:
            id_x = int(pos_x + dx)
            id_y = int(pos_y + dy)
            self.grid[id_x][id_y] = piece.color
    
    def draw(self):
        for x, row in enumerate(self.grid):
            for y, value in enumerate(row):
                if value != None:
                    pos_x = x * BLOC_SIZE
                    pos_y = y * BLOC_SIZE
                    pygame.draw.rect(screen, value, (pos_x, pos_y, BLOC_SIZE, BLOC_SIZE))
   
class Piece:
    def __init__(self, force_shape=None):
        self.rotation = 0
        self.on_the_floor = False
        if force_shape == None:
            self.shape = random.choice(SHAPES)
        elif force_shape in SHAPES:
            self.shape = force_shape
        else:
            raise ValueError("Error: Shape not exist.") 
        self.position = pygame.Vector2(SPAWN.x, SPAWN.y)
        self.color = random.choice(SHAPES_COLORS)
    
    def rotate(self):
        self.rotation += 1
        if self.rotation >= len(self.shape):
            self.rotation = 0
    
    def is_valid_position(self, grid, movement):
        for dx, dy in self.shape[self.rotation]:
            x = int(self.position.x + dx + movement.x)
            y = int(self.position.y + dy + movement.y)
            if x < 0 or x >= GRID_WIDTH: # largeur
                return False
            elif y >= GRID_HEIGHT: # touche le sol ou une autre piece en axe y, au second tic, on verouille la piece et on envoi une nouvelle
                self.on_the_floor = True
                return False
            elif y > 0 and grid[x][y] != None:
                self.on_the_floor = True
                return False
            
        return True

    def move(self, movement):
        self.position += pygame.Vector2(movement.x, movement.y)
        
    def draw(self):
        for dx, dy in self.shape[self.rotation]:
            pygame.draw.rect(
                screen,
                self.color,
                ((self.position.x + dx) * BLOC_SIZE, (self.position.y + dy) * BLOC_SIZE, BLOC_SIZE, BLOC_SIZE)
            )

class Tetris:
    def __init__(self):
        self.running = True
        self.pause = False
        self.grid = Grid()
        self.piece = Piece()
        self.piece_movement = pygame.Vector2()
        self.rotate = False
        self.move_down_timer = 0
        self.move_down_interval = 500 #ms
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key in CONTROL_QUIT:# press X or DELETE pour quit
                    self.running = False
                if key in CONTROL_PAUSE:# press ESCAPE pour pause
                    self.pause = not self.pause
                if key in CONTROL_NEW and DEBUG_MODE:# pour debug, charge une nouvelle piece
                    self.piece = Piece()
                if key in CONTROL_LEFT:
                    self.piece_movement.x -= 1
                if key in CONTROL_RIGHT:
                    self.piece_movement.x += 1
                if key in CONTROL_DOWN:
                    self.piece_movement.y += 1
                if key in CONTROL_ROTATE:
                    self.rotate = True
    
    def update(self, delta):
        if self.pause == False:
            self.move_down_timer += delta # recupere le temps passe - change selon le FPS reel
            if self.move_down_timer > self.move_down_interval:
                self.move_down_timer = 0
                self.piece_movement.y += 1
            if self.piece.on_the_floor and self.piece_movement.y > 0: # si la piece est au sol et que un tick ou le control down a ete press, on verouille la piece
                # TODO gestion deplacement extremis, disable on the floor
                # TODO extremis rotate
                self.grid.update(self.piece) # enregistrement de l emplacement dans la grille
                # TODO check les Tetris
                # TODO check GameOver
                self.piece = Piece() # nouvelle piece
            else:
                if self.piece.is_valid_position(self.grid.grid, self.piece_movement):
                    self.piece.move(self.piece_movement)  # mise a jour de la position
                if self.rotate:
                    self.piece.rotate()
        self.piece_movement = pygame.Vector2(0, 0)
        self.rotate = False
    
    def draw(self):
        screen.fill(BLACK) # couleur fond
        self.grid.draw()
        self.piece.draw() # affiche la piece
        if DEBUG_MODE:
            self.draw_grid() # affiche une grille des cases               
        if self.pause == True:
            self.draw_pause() # affiche la pause
        pygame.display.flip() # mise a jour rendu
        
    def draw_grid(self):
        for grid_x in range(GRID_WIDTH):
            for grid_y in range(GRID_HEIGHT):
                pos_x = grid_x * BLOC_SIZE
                pos_y = grid_y * BLOC_SIZE
                pygame.draw.rect(screen, WHITE, (pos_x, pos_y, pos_x + BLOC_SIZE, pos_y + BLOC_SIZE), 1)

    def draw_pause(self):
        screen.blit(TEXT_PAUSE, ((WINDOW_WIDTH - TEXT_PAUSE.get_width()) / 2,(WINDOW_HEIGHT - TEXT_PAUSE.get_height()) / 2))


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