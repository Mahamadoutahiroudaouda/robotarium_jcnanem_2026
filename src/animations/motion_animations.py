import numpy as np

class MotionBehaviors:
    @staticmethod
    def jitter(drones, intensity=0.1):
        """Adds random noise to positions."""
        for d in drones:
            noise = np.random.uniform(-intensity, intensity, 3)
            d.position += noise
            
    @staticmethod
    def rotate_swarm(drones, angle_rad, axis='z'):
        """Rotates all drones around center (0,0,0)."""
        c, s = np.cos(angle_rad), np.sin(angle_rad)
        
        if axis == 'z':
             R = np.array(((c, -s, 0), (s, c, 0), (0, 0, 1)))
        elif axis == 'y':
             R = np.array(((c, 0, s), (0, 1, 0), (-s, 0, c)))
        
        for d in drones:
            d.position = R.dot(d.position)
