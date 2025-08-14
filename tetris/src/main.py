import pygame
from config import Config
from game import Tetris
from utils import Controls

if __name__ == "__main__":
    config = Config() # charge les configurations
    pygame.init()
    screen = pygame.display.set_mode((config.get_display_mode())) # init la fenetre
    pygame.display.set_caption(config.get_caption())
    clock = pygame.time.Clock() # horloge 
    game = Tetris(screen, config)
    controls = Controls(config)
    fps = config.get_fps()
    while game.running:
        delta = clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            actions = controls.handle_event(event, delta)             
        game.update(actions, delta)
        game.draw()
    pygame.quit()