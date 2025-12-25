import numpy as np
from src.formations.cultural_formations import agadez_cross

def mosque_agadez(n_drones, scale=2):
    """
    Stylized Agadez Mosque (Tall pyramidal minaret with wooden beams).
    """
    coords = []
    
    # Base (Rectangular)
    base_w = 8 * scale
    for x in np.linspace(-base_w/2, base_w/2, 8):
        for y in np.linspace(-base_w/2, base_w/2, 8):
            coords.append([x, y, 0])
            
    # Minaret (Tapering tower)
    height = 25 * scale
    layers = 20
    for i in range(layers):
        h = i * (height / layers)
        w = (base_w/2) * (1 - i/layers) # Linear taper
        
        # Square ring
        for cx in [-w, w]:
            for cy in np.linspace(-w, w, 5):
                coords.append([cx, cy, h])
        for cy in [-w, w]:
            for cx in np.linspace(-w, w, 5):
                coords.append([cx, cy, h])
                
        # "Toron" (Wooden beams) - stick out every few layers
        if i % 4 == 2:
            stick_len = w + 2*scale
            coords.append([stick_len, 0, h])
            coords.append([-stick_len, 0, h])
            coords.append([0, stick_len, h])
            coords.append([0, -stick_len, h])
            
    # Fill
    current = len(coords)
    if current < n_drones:
         # Add Cross of Agadez floating above or next to it?
         # Let's fill the mosque body more purely
         while len(coords) < n_drones:
             z = np.random.uniform(0, height)
             current_w = (base_w/2) * (1 - z/height)
             coords.append([
                 np.random.uniform(-current_w, current_w),
                 np.random.uniform(-current_w, current_w),
                 z
             ])
             
    return np.array(coords[:n_drones])

def monuments_sequence(n_drones, step=0):
    if step == 0:
        return mosque_agadez(n_drones)
    else:
        return agadez_cross(n_drones, scale=3)
