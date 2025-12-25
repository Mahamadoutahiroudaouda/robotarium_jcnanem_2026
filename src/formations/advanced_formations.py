import numpy as np

def mobius_strip(n_drones, radius=15):
    """
    Parametric Mobius strip.
    """
    coords = []
    # Parametric:
    # x = (1 + v/2 cos(u/2)) cos u
    # y = (1 + v/2 cos(u/2)) sin u
    # z = v/2 sin(u/2)
    # u in [0, 2pi], v in [-1, 1]
    
    # We map n_drones to grid u,v
    side = int(np.sqrt(n_drones))
    
    u_vals = np.linspace(0, 2*np.pi, side * 2)
    v_vals = np.linspace(-1, 1, int(n_drones / len(u_vals)) + 1)
    
    for u in u_vals:
        for v in v_vals:
            if len(coords) >= n_drones: break
            
            x = radius * (1 + v/2 * np.cos(u/2)) * np.cos(u)
            y = radius * (1 + v/2 * np.cos(u/2)) * np.sin(u)
            z = radius * (v/2 * np.sin(u/2)) + 30
            coords.append([x, y, z])
            
    return np.array(coords[:n_drones])

def double_helix(n_drones, height=40, loops=3, radius=10):
    """
    DNA-like double helix.
    """
    coords = []
    per_strand = n_drones // 2
    
    # Strand 1
    for i in range(per_strand):
        t = i / per_strand * loops * 2 * np.pi
        z = i / per_strand * height + 10
        x = radius * np.cos(t)
        y = radius * np.sin(t)
        coords.append([x, y, z])
        
    # Strand 2 (offset by pi)
    for i in range(per_strand):
        t = i / per_strand * loops * 2 * np.pi + np.pi
        z = i / per_strand * height + 10
        x = radius * np.cos(t)
        y = radius * np.sin(t)
        coords.append([x, y, z])
        
    # Fill remaining
    while len(coords) < n_drones:
        coords.append([0,0,20])
        
    return np.array(coords)
