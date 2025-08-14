import pygame

class Controls:
    def __init__(self, config):
        self.key_map = {}
        self.cooldowns = {}  # cooldown restant par touche
        self.delay = 150  # ms entre actions
        self.controller = config.get_controller()
        key_map = config.get_control_map(self.controller)
        for action, keys in key_map.items():
            if isinstance(keys, str):
                keys = [keys]
            self.key_map[action] = [getattr(pygame, k) for k in keys]
            for k in keys:
                self.cooldowns[k] = 0  # initialisation

    def handle_event(self, event, delta):
        actions = []
        # on décrémente tous les cooldowns
        for k in self.cooldowns:
            self.cooldowns[k] = max(0, self.cooldowns[k] - delta)

        if event.type == pygame.KEYDOWN:
            key = event.key
            if self.cooldowns.get(key, 0) == 0:
                for action, keys in self.key_map.items():
                    if key in keys:
                        actions.append(action)
                        self.cooldowns[key] = self.delay  # reset cooldown

        return actions
