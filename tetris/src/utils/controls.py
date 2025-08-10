import pygame

class Controls:
    def __init__(self, config):
        self.key_map = {}
        self.controller = config.get_controller()
        key_map = config.get_control_map(self.controller)
        for action, keys in key_map.items():
            if isinstance(keys, str):
                keys = [keys]
            self.key_map[action] = [getattr(pygame, k) for k in keys]
        print(self.key_map)
    
    def handle_event(self, event):
        actions = []
        if event.type == pygame.KEYDOWN:
            key = event.key
            for action, keys in self.key_map.items():
                if key in keys:
                    actions.append(action)
        
        return actions