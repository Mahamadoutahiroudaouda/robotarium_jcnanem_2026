import numpy as np

def giraffe_shape(n_drones, scale=2):
    """
    Simplified stick-figure giraffe.
    """
    coords = []
    
    # Body (Oval-ish / Box)
    for x in range(-5, 6, 2):
        for y in range(-3, 4, 2):
            coords.append([x*scale, 0, 15 + y*scale])
            
    # Neck (Long vertical rising from front)
    # Front is +x
    neck_x = 4 * scale
    for z in range(int(18 + 3*scale), int(18 + 15*scale), 3):
        coords.append([neck_x, 0, z])
        
    # Head
    head_z = 18 + 15*scale
    coords.append([neck_x, 0, head_z])
    coords.append([neck_x + 2*scale, 0, head_z]) # Snout
    
    # Legs
    # Front Left
    for z in range(0, int(15 - 3*scale), 3):
        coords.append([4*scale, -2*scale, z])
    # Front Right
    for z in range(0, int(15 - 3*scale), 3):
        coords.append([4*scale, 2*scale, z])
    # Back Left
    for z in range(0, int(15 - 3*scale), 3):
        coords.append([-4*scale, -2*scale, z])
    # Back Right
    for z in range(0, int(15 - 3*scale), 3):
        coords.append([-4*scale, 2*scale, z])
        
    # Fill remaining drones randomly around the shape to give volume or just return what we have
    # Repeatedly add the existing points with jitter if needed to match n_drones
    
    current_count = len(coords)
    if current_count < n_drones:
        # Fill extra drones in a ground circle
        radius = 20
        needed = n_drones - current_count
        for i in range(needed):
            angle = 2 * np.pi * i / needed
            coords.append([radius * np.cos(angle), radius * np.sin(angle), 5])
            
    return np.array(coords[:n_drones])
