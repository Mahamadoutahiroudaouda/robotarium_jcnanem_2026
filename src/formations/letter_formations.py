import numpy as np

# Simple 5x5 font dictionary (1 = point, 0 = empty)
# This is a very basic font definition.
ALPHABET = {
    'A': [
        [0,0,1,0,0],
        [0,1,0,1,0],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,1]
    ],
    'N': [
        [1,0,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,1]
    ],
    'E': [
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,0,0],
        [1,0,0,0,0],
        [1,1,1,1,1]
    ],
    'M': [
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1]
    ],
    'I': [
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
    ],
    'G': [
        [0,1,1,1,1],
        [1,0,0,0,0],
        [1,0,1,1,1],
        [1,0,0,0,1],
        [0,1,1,1,0]
    ],
    'R': [
        [1,1,1,1,0],
        [1,0,0,0,1],
        [1,1,1,1,0],
        [1,0,0,1,0],
        [1,0,0,0,1]
    ]
}

def get_text_coords(text, spacing=3, start_pos=(0,0,20)):
    """
    Generates 3D coordinates for a string of text.
    spacing: distance between points
    start_pos: (x, z, y) center reference? No, let's say (x_start, z_depth, y_height)
    Wait, usually text is vertical in the sky.
    Let's align it on X-Z plane (vertical wall facing audience). Y is depth? 
    Standard: Z is Up. Y is Depth. X is Left/Right.
    We want text on X-Z plane at Y=0.
    """
    coords = []
    x_cursor = start_pos[0]
    y_pos = start_pos[1]
    z_start = start_pos[2]
    
    letter_height = 5 * spacing
    
    full_width = len(text) * (6 * spacing) # 5 width + 1 visual space
    x_cursor -= full_width / 2 # Center the text
    
    for char in text.upper():
        if char in ALPHABET:
            grid = ALPHABET[char]
            # Grid is top-down (row 0 is top), so we map to Z
            # row 0 -> Z highest
            for row_idx, row in enumerate(grid):
                z = z_start + (4 - row_idx) * spacing # flip so row 0 is at top
                for col_idx, val in enumerate(row):
                    if val == 1:
                        x = x_cursor + col_idx * spacing
                        coords.append([x, y_pos, z])
        
        x_cursor += 6 * spacing # 5 width + 1 space
        
    return np.array(coords)
