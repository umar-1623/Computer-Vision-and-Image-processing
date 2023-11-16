import webcolors
from scipy.spatial import KDTree
from webcolors import hex_to_rgb

# Create a dictionary with color names as keys and hex values as values
color_dict = {name: hex_value for name, hex_value in webcolors.CSS3_HEX_TO_NAMES.items()}

def rgb_to_color_name(rgb):
    css3_db = color_dict
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb)
    return names[index]

# Example RGB values
rgb_values = [
    (97, 105, 103),
    (95, 184, 79),
    (136, 140, 132),
    (21, 99, 22),
    (83, 94, 91),
    (21, 99, 22),
    (83, 94, 91),
    (136, 140, 132),
    (97, 105, 103)
]

# Find the closest color names for each RGB value
for rgb_value in rgb_values:
    color_name = rgb_to_color_name(rgb_value)
    print(f"RGB: {rgb_value} -> Color Name: {color_name}")
