import numpy as np

def hausa_architecture(n_drones, scale=2):
    """
    Stylized Hausa gate or hut shape.
    """
    coords = []
    
    # Base (Square/Rect)
    width = 10 * scale
    height = 8 * scale
    depth = 8 * scale
    
    # Walls
    for x in np.linspace(-width/2, width/2, 10):
        for z in np.linspace(0, height, 8):
            coords.append([x, -depth/2, z]) # Front wall
            coords.append([x, depth/2, z])  # Back wall
            
    # Roof (Pyramidal or Dome-ish)
    # Traditional Hausa can be flat with pinnacles or dome
    # Let's do a simple dome roof
    center_roof = [0, 0, height]
    roof_radius = width / 2
    
    steps = 10
    for i in range(steps):
        r = roof_radius * (1 - i/steps)
        z = height + i * scale
        n_ring = int(r * 3) + 1
        for j in range(n_ring):
            angle = 2 * np.pi * j / n_ring
            coords.append([r * np.cos(angle), r * np.sin(angle), z])
            
    # Emphasize "Zanko" (Pinnacles) - typical of Hausa architecture
    # Four corners + center
    pinnacles = [
        (-width/2, -depth/2), (width/2, -depth/2),
        (-width/2, depth/2), (width/2, depth/2)
    ]
    for px, py in pinnacles:
        for k in range(3):
            coords.append([px, py, height + k*scale])
            
    # Fill remaining
    while len(coords) < n_drones:
         coords.append([np.random.uniform(-width, width), np.random.uniform(-depth, depth), 0])
         
    return np.array(coords[:n_drones])
