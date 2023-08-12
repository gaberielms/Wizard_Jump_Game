import pygame, sys, json
from map import Map
from menu import Menu
from particles import Particles
from scores import display_score


# setup
pygame.init()

# loading save
with open('..\saving\save_last.txt') as save_file:
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
            with open('..\saving\save_last.txt', 'w') as save_file:
                json.dump(data, save_file)
            pygame.quit()
            sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if game_active:
                game_active = False
            menu.show_main()
    
    # what is displayed in menu
        if not game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu.main_menu:
                    for spr in menu.option_group.sprites():
                        if spr.rect.collidepoint(event.pos):
                            spr.set_colour('red')
                            menu.show_main()
            if event.type == pygame.MOUSEBUTTONUP:
                if menu.main_menu:
                    for spr in menu.option_group.sprites():
                        spr.set_colour('white')
                        menu.show_main()
                    if menu.option_group.sprites()[0].rect.collidepoint(event.pos):
                        game_active = True
                        start_time = pygame.time.get_ticks() - score
                        score = 0
                    elif menu.option_group.sprites()[1].rect.collidepoint(event.pos):
                        menu.show_settings()
                    elif menu.option_group.sprites()[2].rect.collidepoint(event.pos):
                        if map.current_y < map.blocks.sprites()[0].rect.top and score < data['high_score']:
                            data['high_score'] = score
                        menu.show_about(data['high_score'])
                    elif menu.option_group.sprites()[3].rect.collidepoint(event.pos):
                        data = menu.restart(data)
                        score = 0
                        map = Map(data, screen)
                        game_active = True
                        start_time = pygame.time.get_ticks()
            if menu.main_menu and keys[pygame.K_r]:
                data = menu.restart(data)
                score = 0
                map = Map(data, screen)
                game_active = True
                start_time = pygame.time.get_ticks()
    
    # what gets displayed in game
    if game_active:
        screen.fill((128,128,128))
        map.run()
        score = display_score(screen, start_time)

    pygame.display.update()
    clock.tick(60)
    