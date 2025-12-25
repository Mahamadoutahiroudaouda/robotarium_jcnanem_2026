import numpy as np

def hex_to_rgb(hex_color):
    """Converts hex string (e.g. #FFFFFF) to normalized RGB tuple (1.0, 1.0, 1.0)."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def calculate_distance(pos1, pos2):
    return np.linalg.norm(np.array(pos1) - np.array(pos2))

def generate_grid_coordinates(n_drones):
    """Generates a list of coordinates for a 3D grid."""
    # Approximate cube root to get side length
    side = int(np.ceil(n_drones**(1/3)))
    coords = []
    for x in range(side):
        for y in range(side):
            for z in range(side):
                if len(coords) < n_drones:
                    coords.append([x*2.0, y*2.0, z*2.0]) # Spacing of 2m
    return np.array(coords)
