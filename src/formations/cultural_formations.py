import numpy as np

def niger_map(n_drones, scale=2):
    """
    Approximation of Niger's map borders using points.
    We would normally load a GeoJSON or SVG, but here we define a simplified polygon.
    """
    # Simplified vertices of Niger (relative coordinates)
    # Roughly: boxy shape with protrusion on update right
    polygon_points = [
        (-10, 5), (-5, 10), (5, 12), (10, 8), (12, 10), (15, 5), # North/East
        (12, -5), (5, -8), (-5, -8), (-10, -5), (-12, 0) # South/West
    ]
    
    # Interpolate points between vertices to fill the border
    border_coords = []
    points = np.array(polygon_points) * scale
    
    # Number of drones for border
    drones_per_segment = n_drones // len(points)
    
    for i in range(len(points)):
        curr_p = points[i]
        next_p = points[(i+1) % len(points)]
        
        # Linearly interpolate
        for j in range(drones_per_segment):
            alpha = j / drones_per_segment
            p = curr_p + (next_p - curr_p) * alpha
            border_coords.append([p[0], 0, p[1] + 30]) # X, Y=0, Z (lifted)
            
    # If we have extra drones, fill the inside? For now just border.
    # Or just return what we have (might be less than n_drones)
    # Ideally should fill n_drones.
    
    return np.array(border_coords)

def agadez_cross(n_drones, scale=2):
    """
    Points forming the Cross of Agadez.
    """
    # Central ring + arms
    coords = []
    
    # Center circle
    radius = 3 * scale
    n_circle = n_drones // 4
    for i in range(n_circle):
        angle = 2 * np.pi * i / n_circle
        coords.append([
            radius * np.cos(angle),
            0,
            radius * np.sin(angle) + 40
        ])
    
    # Top part (loop)
    # Arms
    # Simple cross shape for demo: | and -
    
    # Vertical bar
    for i in range(n_drones // 4):
        y = (i - (n_drones // 8)) * scale/2
        coords.append([0, 0, y + 40])

    # Horizontal bar
    for i in range(n_drones // 4):
        x = (i - (n_drones // 8)) * scale/2
        coords.append([x, 0, 40])
        
    return np.array(coords)
