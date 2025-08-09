import pygame
from config import Config
from game import Tetris


if __name__ == "__main__":
    config = Config() # charge les configurations
    pygame.init()
    screen = pygame.display.set_mode((config.get_display_mode())) # init la fenetre
    pygame.display.set_caption(config.get_caption())
    clock = pygame.time.Clock() # horloge 
    game = Tetris(screen, config)
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        delta = clock.tick(config.get_fps())
        game.update(delta)
        game.draw()
    pygame.quit()