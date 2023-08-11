import pygame, sys, json
from pygame import *
from map import Map
from menu import Menu
from particles import Particles


# pygame setup
init()

with open('..\saving\save_last.txt') as save_file:
        data = json.load(save_file)

screen = display.set_mode((data['screen_width'], data['screen_height']))
clock = time.Clock()
game_active = False

menu = Menu(screen)
menu.show_main()
map = Map(data, screen)

alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 25)


# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            data = map.save()
            with open('..\saving\save_last.txt', 'w') as save_file:
                json.dump(data, save_file)
            quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if not game_active and menu.main_menu:
                for spr in menu.option_group.sprites():
                    if spr.rect.collidepoint(event.pos):
                        spr.set_colour('red')
                        menu.show_main()
        if event.type == MOUSEBUTTONUP:
            if not game_active and menu.main_menu:
                for spr in menu.option_group.sprites():
                    spr.set_colour('white')
                    menu.show_main()
                if menu.option_group.sprites()[0].rect.collidepoint(event.pos):
                    game_active = True
                elif menu.option_group.sprites()[1].rect.collidepoint(event.pos):
                    menu.show_settings()
                elif menu.option_group.sprites()[2].rect.collidepoint(event.pos):
                    menu.show_about()
                elif menu.option_group.sprites()[3].rect.collidepoint(event.pos):
                    data = menu.restart()
                    map = Map(data, screen)
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            if game_active:
                game_active = False
            menu.show_main()
            
    if game_active:
        #display
        screen.fill((128,128,128))
        map.run()

    display.update()
    clock.tick(60)
    