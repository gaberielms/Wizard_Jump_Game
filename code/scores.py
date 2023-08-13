import pygame
from pathlib import Path

def display_score(display, start_time):
    alagard = pygame.font.Font(Path('fonts/alagard.ttf'), 25)
    curr_time = pygame.time.get_ticks() - start_time
    score_sfc = alagard.render(str(curr_time // 1000), False, 'black')
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
