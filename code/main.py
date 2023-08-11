import pygame, sys, json
from pygame import *
from map import Map
from menu import Menu
from particles import Particles

def display_score():
    curr_time = time.get_ticks() - start_time
    score_sfc = alagard.render(str(curr_time // 1000), False, 'black')
    score_rect = score_sfc.get_rect(center = (50,50))
    screen.blit(score_sfc, score_rect)
    return curr_time


# pygame setup
init()

with open('..\saving\save_last.txt') as save_file:
        data = json.load(save_file)

screen = display.set_mode((data['screen_width'], data['screen_height']))
clock = time.Clock()
game_active = False
start_time = 0
score = data['timer']

menu = Menu(screen)
menu.show_main()
map = Map(data, screen)

alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 25)


# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            data = map.save()
            data['timer'] = score
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
                    start_time = time.get_ticks() - score
                    score = 0
                elif menu.option_group.sprites()[1].rect.collidepoint(event.pos):
                    menu.show_settings()
                elif menu.option_group.sprites()[2].rect.collidepoint(event.pos):
                    menu.show_about()
                elif menu.option_group.sprites()[3].rect.collidepoint(event.pos):
                    data = menu.restart()
                    score = 0
                    map = Map(data, screen)
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            if game_active:
                game_active = False
            menu.show_main()
            
    if game_active:
        #display
        screen.fill((128,128,128))
        map.run()
        score = display_score()

    display.update()
    clock.tick(60)
    