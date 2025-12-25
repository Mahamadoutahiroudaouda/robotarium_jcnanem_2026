import numpy as np

def scientific_atom(n_drones, scale=10):
    """
    Classic Atom model with nucleus and orbiting electrons.
    """
    coords = []
    
    # Nucleus (Dense sphere)
    n_nucleus = int(n_drones * 0.2)
    radius_n = scale * 0.3
    for i in range(n_nucleus):
        u = np.random.uniform(0, 1)
        v = np.random.uniform(0, 1)
        theta = 2 * np.pi * u
        phi = np.arccos(2 * v - 1)
        x = radius_n * np.sin(phi) * np.cos(theta)
        y = radius_n * np.sin(phi) * np.sin(theta)
        z = radius_n * np.cos(phi) + 30
        coords.append([x, y, z])
        
    # Electron shells (Rings)
    # 3 rings at different angles
    remaining = n_drones - len(coords)
    if remaining > 0:
        per_ring = remaining // 3
        radius_ring = scale * 2
        
        # Ring 1: XY plane
        for i in range(per_ring):
            angle = 2 * np.pi * i / per_ring
            coords.append([
                radius_ring * np.cos(angle),
                radius_ring * np.sin(angle),
                30
            ])
            
        # Ring 2: YZ plane (rotated)
        # Actually better to just rotate points mathematically
        for i in range(per_ring):
            angle = 2 * np.pi * i / per_ring
            # Base circle in XY
            x = radius_ring * np.cos(angle)
            y = radius_ring * np.sin(angle)
            z = 0
            # Rotate 60 deg around X
            y_rot = y * np.cos(np.pi/3) - z * np.sin(np.pi/3)
            z_rot = y * np.sin(np.pi/3) + z * np.cos(np.pi/3)
            coords.append([x, y_rot, z_rot + 30])
            
        # Ring 3: -60 deg
        for i in range(per_ring):
            angle = 2 * np.pi * i / per_ring
            x = radius_ring * np.cos(angle)
            y = radius_ring * np.sin(angle)
            z = 0
            # Rotate -60 deg around X
            y_rot = y * np.cos(-np.pi/3) - z * np.sin(-np.pi/3)
            z_rot = y * np.sin(-np.pi/3) + z * np.cos(-np.pi/3)
            coords.append([x, y_rot, z_rot + 30])
            
    # Fill remaining logic...
    while len(coords) < n_drones:
        coords.append([0,0,30])

    return np.array(coords[:n_drones])
