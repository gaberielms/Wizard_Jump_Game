import pygame, sys, json
from map import Map
from menu import Menu
from scores import *
from pathlib import Path


def run():
    # setup
    pygame.init()
    icon = pygame.image.load(Path('graphics/icon.png'))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Wizard Jump')

    # loading save
    with open(Path('saving/save_last.txt')) as save_file:
        data = json.load(save_file)
    
    # variable setup
    screen = pygame.display.set_mode((data['screen_width'], data['screen_height']))
    clock = pygame.time.Clock()
    game_active = False
    start_time = 0
    score = data['score']
    
    # game and menu setup
    map = Map(data, screen)
    menu = Menu(screen, 'main', data)
    background_music_1 = pygame.mixer.Sound(str(Path('audio/ambient/MedievalTrack.mp3')))
    background_music_2 = pygame.mixer.Sound(str(Path('audio/ambient/MedievalTrack2.mp3')))
    background_music = [background_music_1, background_music_2]
    for song in background_music:
        song.set_volume(data['volume'] ** 1.5)
    
    
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data = map.save(data)
                data['score'] = score
                with open(Path('saving/save_last.txt'), 'w') as save_file:
                    json.dump(data, save_file)
                pygame.quit()
                sys.exit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                if game_active:
                    game_active = False
                menu = Menu(screen, 'main', data)
        
            if keys[pygame.K_r]:
                reseter(map)
                score = 0
                game_active = True
                start_time = pygame.time.get_ticks()

        # what is displayed in menu
            if not game_active:
                x = menu.run()
                if x == 'Play'or keys[pygame.K_SPACE]:
                    game_active = True
                    start_time = pygame.time.get_ticks() - score
                    score = 0
                if x == 'Restart Game':
                    score = 0
                    data = restart(data)
                    map = Map(data, screen)
                    start_time = pygame.time.get_ticks()
                    game_active = True
                elif menu.sliders:
                    data['volume'] = menu.sliders[0].get_value() / 100
                    data['sounds'] = menu.sliders[1].get_value() / 100
                    for song in background_music:
                        song.set_volume(data['volume'] ** 1.5)
                
                menu = Menu(screen, menu.menu_status, data)

        # what gets displayed in game
        if game_active:
            screen.fill((128,128,128))
            map.run()
            score = display_score(screen, start_time)
            if map.current_y < map.blocks.sprites()[0].rect.top and score < data['high_score']:
                data['high_score'] = score

        
        background_music_1.play(-1)
        pygame.display.update()
        clock.tick(60)
        