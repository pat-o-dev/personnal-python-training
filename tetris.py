# creation rapide d un Tetris basique avec pygame
import pygame
import numpy as np
import random

pygame.init()
pygame.font.init()

FPS = 60

# liste des couleurs
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_RED = (255, 0, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_ORANGE = (255, 128, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_PINK = (255, 0, 255)
COLOR_VIOLET = (127, 0, 255)
COLOR_BROWN = (102, 51, 0)

# liste des textes
FONT_SIZE = 30
FONT = pygame.font.SysFont('Arial', FONT_SIZE)
TEXT_PAUSE = FONT.render("Pause", True, COLOR_WHITE, COLOR_GRAY)
TEXT_GAMEOVER = FONT.render("Game Over", True, COLOR_WHITE, COLOR_GRAY)

# taille de la grille
GRID_HEIGHT = 20
GRID_WIDTH = 10
# taille d un bloc en px
BLOC_SIZE = 30
# calcul de la taille de la fenetre
GUI_SIDE = 5
GUI_TOP = 3

WINDOW_HEIGHT = (GRID_HEIGHT + GUI_TOP) * BLOC_SIZE
WINDOW_WIDTH = (GRID_WIDTH + GUI_SIDE) * BLOC_SIZE

# liste des formes, les variantes
SHAPE_L = np.array([
    [COLOR_RED, None],
    [COLOR_RED, None],
    [COLOR_RED, COLOR_RED],
], dtype=object)
SHAPE_LR = np.array([
    [None, COLOR_VIOLET],
    [None, COLOR_VIOLET],
    [COLOR_VIOLET, COLOR_VIOLET],
], dtype=object)
SHAPE_T = np.array([
    [COLOR_BROWN, COLOR_BROWN, COLOR_BROWN],
    [None, COLOR_BROWN, None],
], dtype=object)   
SHAPE_I = np.array([
    [COLOR_CYAN],
    [COLOR_CYAN],
    [COLOR_CYAN],
    [COLOR_CYAN],
], dtype=object)
SHAPE_O = np.array([
    [COLOR_BLUE, COLOR_BLUE],
    [COLOR_BLUE, COLOR_BLUE],
], dtype=object)
SHAPE_S = np.array([
    [None, COLOR_ORANGE, COLOR_ORANGE],
    [COLOR_ORANGE, COLOR_ORANGE, None],
], dtype=object)
SHAPE_SR = np.array([
    [COLOR_PINK, COLOR_PINK, None],
    [None, COLOR_PINK, COLOR_PINK],
], dtype=object)

SHAPES = [SHAPE_L, SHAPE_LR, SHAPE_T, SHAPE_I, SHAPE_O, SHAPE_S, SHAPE_SR]

# position depart nouvelle piece
SPAWN = pygame.Vector2(4, 4)

# liste des touches
CONTROL_PAUSE = [pygame.K_ESCAPE, pygame.K_p]
CONTROL_QUIT = [pygame.K_x, pygame.K_DELETE]
CONTROL_LEFT = [pygame.K_a, pygame.K_LEFT]
CONTROL_RIGHT = [pygame.K_d, pygame.K_RIGHT]
CONTROL_DOWN = [pygame.K_s, pygame.K_DOWN]
CONTROL_ROTATE = [pygame.K_r, pygame.K_UP]
   
class Grid:
    def __init__(self):
        # enregistre la grille None ou Couleur
        self.height, self.width = GRID_HEIGHT, GRID_WIDTH
        self.grid = np.empty((self.height, self.width), dtype=object)
    
    def check(self):
        pass
        '''
        for y in range(self.num_rows): # recherche si une ligne est pleine
            tetris = True
            for x in range(self.num_cols):
                tetris &= (self.grid[y][x] != None)
            if tetris:
                self.grid.pop(y)
                self.grid.insert(0, [None] * self.num_cols)
        '''
        
    def update(self, piece):
        for dx, dy in piece.get_current_shape():
            id_x = int(piece.position.x + dx)
            id_y = int(piece.position.y + dy)
            self.grid[id_y][id_x] = piece.color
    
    def draw(self):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value != None:
                    pygame.draw.rect(
                        screen, 
                        value,
                        (x * BLOC_SIZE, y * BLOC_SIZE, BLOC_SIZE, BLOC_SIZE)
                    )
   
class Piece:
    def __init__(self, shape):
        self.on_the_floor = False
        self.shape = shape
        self.position = pygame.Vector2(SPAWN.x, SPAWN.y)
        self.bloc_size = BLOC_SIZE
    
    def get_current_shape(self):
        return self.shape
    
    def rotate(self):
        self.shape = np.rot90(self.shape)
    
    def is_valid_position(self, grid, movement):
        '''
        for dx, dy in self.shape:
            x = int(self.position.x + dx + movement.x)
            y = int(self.position.y + dy + movement.y)
            if x < 0 or x >= GRID_WIDTH: # largeur
                return False
            elif y >= GRID_HEIGHT: # touche le sol ou une autre piece en axe y, au second tic, on verouille la piece et on envoi une nouvelle
                self.on_the_floor = True
                return False
            elif y > 0 and grid[y][x] != None: # touche un piece de la grille
                self.on_the_floor = True
                return False
        #self.on_the_floor = False # on passe a false en cas de mouvement possible   
        '''
        return True

    def move(self, movement):
        self.position += pygame.Vector2(movement.x, movement.y)
        
    def draw(self):
        for y, x in np.ndindex(self.shape.shape): 
            if self.shape[y, x] is not None:  # affiche un bloc lorsque une couleur de defini
                pygame.draw.rect(
                    screen,
                    self.shape[y, x],  # Use RGB tuple from array
                    (self.position[0] * self.bloc_size + x * self.bloc_size,
                    self.position[1] * self.bloc_size + y * self.bloc_size,
                    self.bloc_size, self.bloc_size,
                    )
                )
                pygame.draw.rect(
                    screen,
                    COLOR_GRAY,
                    (self.position[0] * self.bloc_size + x * self.bloc_size,
                    self.position[1] * self.bloc_size + y * self.bloc_size,
                    self.bloc_size, self.bloc_size),
                    width=1  # 1px border
                )

class Tetris:
    def __init__(self):
        self.running = True
        self.pause = False
        self.gameover = False
        self.grid = Grid()
        shape = random.choice(SHAPES)
        self.piece = Piece(shape)
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
                if key in CONTROL_LEFT:
                    self.piece_movement.x -= 1
                if key in CONTROL_RIGHT:
                    self.piece_movement.x += 1
                if key in CONTROL_DOWN:
                    self.piece_movement.y += 1
                if key in CONTROL_ROTATE:
                    self.rotate = True
    
    def update(self, delta):
        if self.pause == False and self.gameover == False:
            self.move_down_timer += delta # recupere le temps passe - change selon le FPS reel
            if self.move_down_timer > self.move_down_interval:
                self.move_down_timer = 0
                self.piece_movement.y += 1
            if self.piece.on_the_floor: # si la piece est au sol et que un tick ou le control down a ete press, on verouille la piece
                # TODO extremis rotate
                self.grid.update(self.piece) # enregistrement de l emplacement dans la grille
                # check les Tetris
                self.grid.check()
                # check GameOver
                if self.piece.position.y <= 0 and self.piece.is_valid_position(self.grid.grid, self.piece_movement) == False:
                    self.gameover = True
                else:
                    shape = random.choice(SHAPES)
                    self.piece = Piece(shape) # nouvelle piece
            else:
                if self.piece.is_valid_position(self.grid.grid, self.piece_movement):
                    self.piece.move(self.piece_movement)  # mise a jour de la position
                if self.rotate:
                    self.piece.rotate()
        self.piece_movement = pygame.Vector2(0, 0)
        self.rotate = False
    
    def draw(self):
        screen.fill(COLOR_BLACK) # couleur fond
        self.grid.draw()
        self.piece.draw() # affiche la piece             
        if self.pause == True:
            self.draw_pause() # affiche la pause
        if self.gameover:
            self.draw_gameover()
        pygame.display.flip() # mise a jour rendu
        
    def draw_grid(self):
        for grid_x in range(GRID_WIDTH):
            for grid_y in range(GRID_HEIGHT):
                pos_x = grid_x * BLOC_SIZE
                pos_y = grid_y * BLOC_SIZE
                pygame.draw.rect(screen, COLOR_WHITE, (pos_x, pos_y, pos_x + BLOC_SIZE, pos_y + BLOC_SIZE), 1)
                
    def draw_pause(self):
        screen.blit(TEXT_PAUSE, ((WINDOW_WIDTH - TEXT_PAUSE.get_width()) / 2,(WINDOW_HEIGHT - TEXT_PAUSE.get_height()) / 2))

    def draw_gameover(self):
        screen.blit(TEXT_GAMEOVER, ((WINDOW_WIDTH - TEXT_GAMEOVER.get_width()) / 2,(WINDOW_HEIGHT - TEXT_GAMEOVER.get_height()) / 2))

# init window
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# execute la mainloop pygame
if __name__ == "__main__":
    clock = pygame.time.Clock()
    game = Tetris()
    while game.running:
        delta = clock.tick(FPS)
        game.handle_events() # capture des touches
        game.update(delta) # mise a jour des donnees
        game.draw() # affichage
    pygame.quit()