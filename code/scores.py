import pygame
from pathlib import Path

def display_score(display, start_time):
    alagard = pygame.font.Font(Path('fonts/alagard.ttf'), 25)
    curr_time = pygame.time.get_ticks() - start_time
    score_sfc = alagard.render(str(curr_time // 1000), False, 'black')
    score_rect = score_sfc.get_rect(center = (50,50))
    display.blit(score_sfc, score_rect)
    return curr_time
