import numpy as np

def fireworks_explosion(n_drones, radius=30):
    """
    Explosion pattern - Expanding sphere from center.
    This is static state, animation frames would scale radius.
    """
    # Just a sphere at specific radius
    # Randomly distributed points on sphere surface
    coords = []
    for i in range(n_drones):
        # Random direction
        u = np.random.uniform(0, 1)
        v = np.random.uniform(0, 1)
        theta = 2 * np.pi * u
        phi = np.arccos(2 * v - 1)
        
        x = radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi) + 40 # High altitude
        
        coords.append([x, y, z])
        
    return np.array(coords)
