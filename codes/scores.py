import pygame, json
from pathlib import Path


def display_score(display, start_time):
    alagard = pygame.font.Font(Path('fonts/alagard.ttf'), 25)
    curr_time = pygame.time.get_ticks() - start_time
    score_sfc = alagard.render(str(curr_time // 1000), True, 'black')
    score_rect = score_sfc.get_rect(center = (50,50))
    display.blit(score_sfc, score_rect)
    return curr_time

def reseter(map):
    player = map.player.sprite
    player.collision_rect.topleft = (400, 384)
    map.current_x = 0
    map.current_y = 9999999999999
    for block in map.blocks.sprites():
        block.update(-block.deviation)
        block.deviation = 0

def restart(data):
    data['player_start_position'] = (400,377)
    data['player_start_direction'] = (0,0)
    data['player_facing'] = 'left'
    data['map_start'] = 31400
    data['score'] = 0
    with open(Path('saving/save_last.txt'), 'w') as save_file:
        json.dump(data, save_file)
    
    return data
