import numpy as np

def ocean_waves(n_drones, t=0):
    """
    Dynamic wave simulation.
    Returns coordinates for static frame (t=0) or animation state.
    """
    # Grid base
    side = int(np.ceil(np.sqrt(n_drones)))
    coords = []
    step = 4
    
    for x in range(side):
        for y in range(side):
            if len(coords) < n_drones:
                x_pos = (x * step) - (side * step / 2)
                y_pos = (y * step) - (side * step / 2)
                
                # Wave calculation: sin(d + t)
                d = np.sqrt(x_pos**2 + y_pos**2)
                z_pos = 10 * np.sin(d/10 + t) + 20
                
                coords.append([x_pos, y_pos, z_pos])
    
    return np.array(coords)
