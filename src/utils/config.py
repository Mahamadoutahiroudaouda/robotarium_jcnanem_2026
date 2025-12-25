import yaml
import os

class Config:
    def __init__(self, config_path="config.yaml"):
        self.config = self._load_config(config_path)

    def _load_config(self, path):
        if not os.path.exists(path):
            # Fallback or error, for now let's assume it exists or return default
            return {}
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    @property
    def drone_count(self):
        return self.config.get('simulation', {}).get('drone_count', 100)

    @property
    def arena_size(self):
        return self.config.get('simulation', {}).get('arena_size', [100, 100, 100])

    @property
    def fps(self):
        return self.config.get('simulation', {}).get('fps', 30)

    @property
    def drone_size(self):
        return self.config.get('visual', {}).get('drone_size', 5)

    @property
    def default_color(self):
        return self.config.get('visual', {}).get('default_color', '#FFFFFF')

    @property
    def background_color(self):
        return self.config.get('visual', {}).get('background_color', '#000000')

# Global instance
GLOBAL_CONFIG = Config()
