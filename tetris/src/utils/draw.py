import pygame

def draw_cell(screen, color, rect, size, border_color=None, offset=pygame.Vector2(0, 0), border_width=0):
    if color is not None:
        pygame.draw.rect(
            screen,
            color,
            (offset.x + rect.x * size, offset.y + rect.y * size, size, size)
        )
    if border_color is not None:
        pygame.draw.rect(
            screen,
            border_color,
            (offset.x + rect.x * size, offset.y + rect.y * size, size, size),
            border_width
        )