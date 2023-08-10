import json


data = {
    "map_data": {"terrain": "map_data\map_data.csv"},
    "screen_width": 800,
    "screen_height": 600,
    "player_start_position": (300, 265),
    "map_start": 31400
    }

with open('saving\save_last.txt', 'w') as save_file:
    json.dump(data, save_file)