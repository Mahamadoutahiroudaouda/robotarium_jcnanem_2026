import numpy as np

class Drone:
    def __init__(self, drone_id, position=None, color=None):
        self.id = drone_id
        if position is None:
            self.position = np.array([0.0, 0.0, 0.0])
        else:
            self.position = np.array(position, dtype=float)
        
        self.target_position = np.copy(self.position)
        self.color = color if color else "#FFFFFF"
        self.velocity = np.array([0.0, 0.0, 0.0])

    def update(self, dt=1.0):
        # ROI: Simple proportional controller to move constantly towards target
        # For simulation visualization we might just interpolate, but let's have a basic update
        direction = self.target_position - self.position
        distance = np.linalg.norm(direction)
        
        if distance > 0.01:
            # Move towards target
            speed = 5.0 # m/s, customizable
            step = speed * dt
            if step > distance:
                self.position = np.copy(self.target_position)
            else:
                self.position += (direction / distance) * step
    
    def set_target(self, x, y, z):
        self.target_position = np.array([x, y, z], dtype=float)

    def set_color(self, hex_color):
        self.color = hex_color
