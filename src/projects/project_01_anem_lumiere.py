import numpy as np
from src.formations.letter_formations import get_text_coords
from src.formations.base_formations import cube, sphere
from src.formations.cultural_formations import niger_map

# Colors
ORANGE = "#E05206"
WHITE = "#FFFFFF"
GREEN = "#0DB02B"

def hex_2_rgb(curr_hex):
    curr_hex = curr_hex.lstrip('#')
    return tuple(int(curr_hex[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def flag_rain_coords(n_drones):
    """
    Phase 1: Rain of Niger Flag.
    Stratified vertically: Orange (Top), White (Mid), Green (Bottom).
    """
    coords = []
    colors = []
    
    # Define layers
    # Total height approx 60m (from 10m to 70m)
    # Orange: 50-70m
    # White: 30-50m
    # Green: 10-30m
    
    per_layer = n_drones // 3
    
    # Orange Layer
    for i in range(per_layer):
        colors.append(hex_2_rgb(ORANGE))
        coords.append([
            np.random.uniform(-40, 40),
            np.random.uniform(-10, 10), # Thin curtain
            np.random.uniform(50, 70)
        ])
        
    # White Layer (+ Sun if possible, but rain is usually random)
    # Let's add the sun in the center of white layer later or just mix white/orange?
    # Spec says: "White + soleil orange bien centré" even for rain? 
    # Let's do pure white layer for rain simplicity, maybe a dense core of orange in center.
    for i in range(per_layer):
        # Check if point is in "Sun" area (Center)
        x = np.random.uniform(-40, 40)
        z = np.random.uniform(30, 50)
        
        # Sun logic: Central 8m radius sphere/circle in the white band
        dist_from_center = np.sqrt(x**2 + (z-40)**2) 
        if dist_from_center < 6:
             colors.append(hex_2_rgb(ORANGE)) # Sun
        else:
             colors.append(hex_2_rgb(WHITE))
             
        coords.append([x, np.random.uniform(-10, 10), z])
        
    # Green Layer
    remaining = n_drones - len(coords)
    for i in range(remaining):
        colors.append(hex_2_rgb(GREEN))
        coords.append([
            np.random.uniform(-40, 40),
            np.random.uniform(-10, 10),
            np.random.uniform(10, 30)
        ])
        
    return np.array(coords), colors

def thick_text_coords(text, n_drones, spacing=2.5):
    """
    Generates thick/dense text.
    We'll generate the base thin text, then add jittered copies or offsets to thicken it.
    """
    # Base skeleton
    base_coords = get_text_coords(text, spacing=spacing)
    if len(base_coords) == 0:
        return np.array([[0,0,0]]), [hex_2_rgb(WHITE)]
        
    # We need to fill n_drones.
    # Replicate points with small offsets to create "thickness"
    
    final_coords = []
    final_colors = []
    
    # Target color sequence? Or just White? 
    # Usually text is bright white or gold. Let's use White.
    
    base_count = len(base_coords)
    repeats = n_drones // base_count + 1
    
    count = 0
    for i in range(repeats):
        for pt in base_coords:
            if count >= n_drones: break
            
            # Add offset for thickness (Stroke width)
            # Random offset within 1.5m sphere
            offset = np.random.uniform(-1.0, 1.0, 3)
            # Flatten depth (Y) a bit so it's a thick wall not a cloud
            offset[1] *= 0.2
            
            final_coords.append(pt + offset)
            final_colors.append(hex_2_rgb(WHITE))
            count += 1
            
    return np.array(final_coords), final_colors

def waving_flag_coords(n_drones, t=0):
    """
    Phase 4: Floating Niger Flag with wave animation.
    """
    coords = []
    colors = []
    
    # Aspect ratio 3:2 roughly
    # Grid generation
    cols = int(np.sqrt(n_drones * 1.5))
    rows = int(n_drones / cols)
    
    width = 60
    height = 40
    
    x_step = width / cols
    z_step = height / rows
    
    # We assume the flag is in X-Z plane, waving in Y
    
    for r in range(rows):
        for c in range(cols):
            x = c * x_step - width/2
            z_raw = r * z_step # 0 to height
            z = z_raw + 20 # Lift up
            
            # Color logic based on height (z_raw)
            # Top (High Z) -> Orange
            # Mid -> White + Sun
            # Bot -> Green
            
            # Normalized height 0..1
            norm_h = z_raw / height
            
            color = hex_2_rgb(GREEN) # Default bottom
            if norm_h > 0.66:
                color = hex_2_rgb(ORANGE)
            elif norm_h > 0.33:
                # White band
                # Sun logic (Circle in center of flag)
                # Center of flag is x=0, z_raw=height/2
                dist_sun = np.sqrt(x**2 + (z_raw - height/2)**2)
                if dist_sun < 6: # Sun radius
                    color = hex_2_rgb(ORANGE)
                else:
                    color = hex_2_rgb(WHITE)
            
            # Wave animation
            # y = Amplitude * sin(freq * x - speed * t)
            y = 2.0 * np.sin(0.2 * x - 2.0 * t)
            
            coords.append([x, y, z])
            colors.append(color)
            
    # Fill remaining
    current = len(coords)
    if current < n_drones:
         for i in range(n_drones - current):
             coords.append([0,0,0])
             colors.append((0,0,0)) # Hidden
             
    return np.array(coords[:n_drones]), colors[:n_drones]


def anem_lumiere_sequence(n_drones, step=0):
    """
    Returns (coords, colors) tupple for each step.
    """
    # 1. Rain
    if step == 0:
        return flag_rain_coords(n_drones)
        
    # 2. ANEM (Text)
    elif step == 1:
        return thick_text_coords("ANEM", n_drones)
        
    # 3. JCN 2026
    elif step == 2:
        return thick_text_coords("JCN 2026", n_drones)
        
    # 4. FES-MEKNES
    elif step == 3:
        return thick_text_coords("FES-MEKNES", n_drones)
        
    # 5. NIGER (Priority)
    elif step == 4:
        # Extra large, pause long
        return thick_text_coords("NIGER", n_drones, spacing=3.0)
        
    # 6. Floating Flag
    elif step == 5:
        # T=0 static for transition
        return waving_flag_coords(n_drones, t=0)
    
    # 7. Map (With Colors)
    elif step == 6:
        # We need to apply colors to the map
        # Load map coords
        map_coords = niger_map(n_drones, scale=3)
        # Apply flag coloring to map simply by height
        c_list = []
        zs = map_coords[:, 2] # Z coords
        min_z, max_z = min(zs), max(zs)
        h_range = max_z - min_z if max_z != min_z else 1
        
        for z in zs:
            n_z = (z - min_z) / h_range
            if n_z > 0.66: c = hex_2_rgb(ORANGE)
            elif n_z > 0.33: c = hex_2_rgb(WHITE)
            else: c = hex_2_rgb(GREEN)
            c_list.append(c)
        return map_coords, c_list
        
    # 8. Finale (Symbol/Sphere)
    else:
        # Just a bright sun/star
        s_coords = sphere(n_drones, radius=20)
        # All Gold/Orange
        c_list = [hex_2_rgb("#FFD700") for _ in s_coords]
        return s_coords, c_list
