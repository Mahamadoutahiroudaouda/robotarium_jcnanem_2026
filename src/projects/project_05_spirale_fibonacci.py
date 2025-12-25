import numpy as np

def fibonacci_spiral(n_drones, spacing=3):
    """
    Arranges drones in a phyllotaxis spiral (sunflower pattern) on a sphere or disk.
    Let's do a 3D spiral (conical or spherical).
    """
    coords = []
    golden_angle = np.pi * (3 - np.sqrt(5))
    
    for i in range(n_drones):
        theta = i * golden_angle
        r = np.sqrt(i) * spacing
        
        # Conical spiral
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        z = i * 0.5 + 10 # Rising up
        
        coords.append([x, y, z])
        
    return np.array(coords)
