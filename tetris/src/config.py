'''
    Chargement des configurations de l application
'''
import json
import os


class Config:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "config.json")
        self._data = {}
        self.load(path)
        
    def load(self, path):
        try:
            with open(path, 'r') as f:
                self._data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found : {path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid config file: {e}")
    
    def get_data(self):
        return self._data
    
    def get_section(self, name):
        return self._data.get(name, {})
    
    def get_colors(self):
        return self.get_section("colors")
    
    def get_caption(self):
        game = self.get_section("game")
        return (f"{game.get("title")} {game.get("revision")}")
    
    def get_fps(self):
        graphics = self.get_section("graphics")
        return graphics.get("fps", 30)
    
    def get_display_mode(self):
        graphics = self.get_section("graphics")
        return [graphics.get("window_width", 800), graphics.get("window_height", 600)]