import numpy as np

def arabic_salaam(n_drones, scale=3):
    """
    Stylized Arabic script for 'Salaam'.
    """
    coords = []
    
    # Simple stroke-based generation
    # Right to Left
    
    # Seen (teeth)
    # x approx 10 to 5
    for i in range(5):
        coords.append([10*scale - i*scale, 0, 30]) # Horizontal stroke
    coords.append([10*scale, 0, 32]) # Tooth 1
    coords.append([8*scale, 0, 32])  # Tooth 2
    coords.append([6*scale, 0, 32])  # Tooth 3
    
    # Lam-Alif
    # Vertical Lam
    for z in range(20, 40, 2):
        coords.append([4*scale, 0, z])
        
    # Loop for Mim (Circle at end)
    # Left side
    center_mim = [-5*scale, 0, 25]
    radius = 2*scale
    for i in range(8):
        angle = 2*np.pi * i / 8
        coords.append([
            center_mim[0] + radius*np.cos(angle),
            0,
            center_mim[2] + radius*np.sin(angle)
        ])
        
    # Fill rest as a decorative frame
    current_count = len(coords)
    if current_count < n_drones:
        # Frame
        frame_w = 20 * scale
        frame_h = 15 * scale
        needed = n_drones - current_count
        # Simple rectangle border
        per_side = needed // 4
        # Top
        for i in range(per_side): coords.append([(i-per_side/2)*2, 0, 45])
        # Bottom
        for i in range(per_side): coords.append([(i-per_side/2)*2, 0, 15])
        
        # Fill rest randomly
        while len(coords) < n_drones:
             coords.append([np.random.uniform(-20, 20), 0, np.random.uniform(15, 45)])

    return np.array(coords[:n_drones])
