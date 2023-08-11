import pygame, json
from pygame.sprite import Group

class Menu:

    def __init__(self, display):
        self.display = display
        self.options = ('Play', 'Settings', 'About', 'Restart Game')
        self.option_group = pygame.sprite.Group()
        self.background = pygame.image.load('..\graphics\menu\menu.jpg').convert()

        for option in self.options:
            alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 25)
            msg = alagard.render(option, False, (50,50,50))
            loc = (400, (self.options.index(option) * 75) + 240)
            spr1 = MenuSprite(msg, loc)
            self.option_group.add(spr1)

    def show_main(self):
        self.main_menu = True
        self.display.blit(self.background, (0,0))

        self.option_group.draw(self.display)
        alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 30)
        message = alagard.render('Wizard Jump', False, (0, 150, 255))
        message_rect = message.get_rect(center = (400,140))
        message2 = alagard.render('(now speedrunable)', False, (0, 150, 255))
        message2_rect = message2.get_rect(center = (400,175))
        self.display.blit(message, message_rect)
        self.display.blit(message2, message2_rect)

    def show_settings(self):
        self.main_menu = False
        self.display.fill((176,180,255))

        alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 30)
        message = alagard.render('Settings', False, (50,50,50))
        message_rect = message.get_rect(center = (400,150))
        message2 = alagard.render('YOU CANT CHANGE ANYTHING', False, (50,50,50))
        message2_rect = message2.get_rect(center = (400, 250))
        message3 = alagard.render('lol get fucked', False, (50,50,50))
        message3_rect = message3.get_rect(center = (400, 300))
        self.display.blit(message3, message3_rect)
        self.display.blit(message2, message2_rect)
        self.display.blit(message, message_rect)

    def show_about(self):
        self.main_menu = False
        self.display.fill((176,180,255))

        alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 30)
        message = alagard.render('About', False, (50,50,50))
        message_rect = message.get_rect(center = (400,150))
        about = alagard.render('if the game breaks it is not my fault', False, (50,50,50))
        about_rect = about.get_rect(center = (400, 300))
        about2 = alagard.render('just hit restart button dumbass', False, (50,50,50))
        about2_rect = about2.get_rect(center = (400, 350))
        self.display.blit(about2, about2_rect)
        self.display.blit(message, message_rect)
        self.display.blit(about, about_rect)

    def restart(self):
        data = {}
        data['map_data'] = {"terrain": "..\map_data\map_data.csv"}
        data['screen_width'] = 800
        data['screen_height'] = 600
        data['player_start_position'] = (377,384)
        data['player_start_direction'] = (0,0)
        data['player_facing'] = 'right'
        data['map_start'] = 31400
        data['timer'] = 0

        with open('..\saving\save_last.txt', 'w') as save_file:
            json.dump(data, save_file)
        
        return data

class MenuSprite(pygame.sprite.Sprite):

    def __init__(self, text, location):
        super().__init__()
        self.text = text
        self.image = pygame.surface.Surface((170,60))
        self.set_colour('white')
        
        self.rect = self.image.get_rect(center = location)

    def set_colour(self, colour):
        self.image.fill(colour)
        text_rect = self.text.get_rect(center = (85,30))
        self.image.blit(self.text, text_rect)
