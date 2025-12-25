import numpy as np
from src.formations.base_formations import sphere
from src.formations.cultural_formations import niger_map

def heart_shape(n_drones, scale=2):
    """
    3D Heart shape.
    """
    coords = []
    # Parametric equations for a heart
    # x = 16 sin^3 t
    # y = 13 cos t - 5 cos 2t - 2 cos 3t - cos 4t
    # rotated or extruded
    
    # Let's do a simple 2D outline extruded slightly or filled
    t = np.linspace(0, 2*np.pi, n_drones)
    x = 16 * np.sin(t)**3
    z = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    # y is depth
    
    # Normalize and scale
    x = x * scale * 0.5
    z = z * scale * 0.5 + 30 # lift
    
    for i in range(n_drones):
        coords.append([x[i], 0, z[i]])
        
    return np.array(coords)

def grande_parade_sequence(n_drones, step=0):
    """
    7 Tableaux:
    0: Parade (Helix/Spiral moving?) -> We use sphere for abstract start
    1: Storm (Random chaos)
    2: Heart (Final love/thanks)
    """
    if step == 0:
        # Parade loop / Chaos
        return np.random.uniform(-30, 30, (n_drones, 3)) + [0,0,30]
    elif step == 1:
        # Re-form map
        return niger_map(n_drones, scale=3)
    else:
        return heart_shape(n_drones)
