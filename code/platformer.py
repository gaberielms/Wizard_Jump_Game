import pygame, sys, json
from map import Map
from menu import Menu
from particles import Particles
from scores import display_score, reseter
from pathlib import Path

def main():
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
    menu = Menu(screen)
    menu.show_main()
    map = Map(data, screen)
    
    
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
                menu.show_main()
        
            if keys[pygame.K_r]:
                reseter(map)
                score = 0
                game_active = True
                start_time = pygame.time.get_ticks()

        # what is displayed in menu
            if not game_active and menu.main_menu:
                for button in menu.buttons.sprites():
                    button.set_colour(pygame.mouse.get_pos(), screen)
                    button.get_input(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    buttons = menu.buttons.sprites()
                    if buttons[0].hover:
                        game_active = True
                        start_time = pygame.time.get_ticks() - score
                        score = 0
                    elif buttons[1].hover:
                        menu.show_settings()
                    elif buttons[2].hover:
                        menu.show_about(data['high_score'])
                    elif buttons[3].hover:
                        data = menu.restart(data)
                        map = Map(data, screen)
                        start_time = pygame.time.get_ticks()
    
        # what gets displayed in game
        if game_active:
            screen.fill((128,128,128))
            map.run()
            score = display_score(screen, start_time)
            if map.current_y < map.blocks.sprites()[0].rect.top and score < data['high_score']:
                data['high_score'] = score
    
        pygame.display.update()
        clock.tick(60)
        