import numpy as np

def sphere(n_drones, radius=10):
    """Generates coordinates for specific number of drones on a sphere surface."""
    indices = np.arange(0, n_drones, dtype=float) + 0.5
    phi = np.arccos(1 - 2*indices/n_drones)
    theta = np.pi * (1 + 5**0.5) * indices
    
    x = radius * np.cos(theta) * np.sin(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(phi) + 20 # Lift it up 20m off ground
    
    return np.column_stack((x, y, z))

def cube(n_drones, side_length=20):
    """Generates a filled grid/cube."""
    side_count = int(np.ceil(n_drones**(1/3)))
    step = side_length / side_count
    coords = []
    
    for x in range(side_count):
        for y in range(side_count):
            for z in range(side_count):
                if len(coords) < n_drones:
                    coords.append([
                        x * step - side_length/2,
                        y * step - side_length/2,
                        z * step + 20 # Lift up
                    ])
    return np.array(coords)

def place_drones_on_ground(n_drones, area_size=50):
    """Initial grounded state."""
    side_count = int(np.ceil(np.sqrt(n_drones)))
    step = area_size / side_count
    coords = []
    for x in range(side_count):
        for y in range(side_count):
            if len(coords) < n_drones:
                coords.append([
                    x * step - area_size/2,
                    y * step - area_size/2,
                    0
                ])
    return np.array(coords)
