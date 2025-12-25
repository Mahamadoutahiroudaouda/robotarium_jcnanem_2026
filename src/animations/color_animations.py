import numpy as np

def rainbow_wave(drones, t, speed=1.0):
    """
    Assigns colors based on position and time.
    Returns list of colors.
    """
    colors = []
    for d in drones:
        # Hue based on x position + time
        # Simple RGB implementation without importing colorsys for perf
        # Let's just oscillate R, G, B
        phase = (d.position[0] / 50.0) + (t * speed)
        r = (np.sin(phase) + 1) / 2
        g = (np.sin(phase + 2*np.pi/3) + 1) / 2
        b = (np.sin(phase + 4*np.pi/3) + 1) / 2
        colors.append((r, g, b))
    return colors

def niger_flag_colors(drones):
    """
    Orange, White, Green based on height or region.
    Usage: Top third Orange, Mid White, Bottom Green.
    """
    colors = []
    
    # Analyze bounds
    zs = [d.position[2] for d in drones]
    min_z, max_z = min(zs), max(zs)
    h_range = max_z - min_z if max_z != min_z else 1
    
    for d in drones:
        rel_h = (d.position[2] - min_z) / h_range
        
        if rel_h > 0.66:
            # Orange (approx RGB: 1.0, 0.5, 0.0)
            colors.append((1.0, 0.5, 0.0))
        elif rel_h > 0.33:
            # White (with orange circle in center?) 
            # Simplified: White
            colors.append((1.0, 1.0, 1.0))
        else:
            # Green
            colors.append((0.0, 0.8, 0.0))
            
    return colors
