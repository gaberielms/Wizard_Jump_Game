import pygame, json
from pathlib import Path
from buttons import Button

class Menu:

    def __init__(self, display):
        self.display = display
        self.options = ('Play', 'Settings', 'About', 'Restart Game')
        self.buttons = pygame.sprite.Group()
        self.background = pygame.image.load(Path('graphics/menu/menu.jpg')).convert()
        self.main_font = pygame.font.Font(Path('fonts/alagard.ttf'), 30)
        self.main_menu = True

        for option in self.options:
            loc = (400, (self.options.index(option) * 75) + 240)
            self.buttons.add(Button(loc, option))

    def show_main(self):
        self.main_menu = True
        self.display.blit(self.background, (0,0))

        self.buttons.draw(self.display)
        alagard = self.main_font
        message = alagard.render('Wizard Jump', False, (0, 150, 255))
        message_rect = message.get_rect(center = (400,140))
        message2 = alagard.render('(now speedrunable)', False, (0, 150, 255))
        message2_rect = message2.get_rect(center = (400,175))
        self.display.blit(message, message_rect)
        self.display.blit(message2, message2_rect)

    def show_settings(self):
        self.main_menu = False
        self.display.fill((176,180,255))

        alagard = self.main_font
        message = alagard.render('Settings', False, (50,50,50))
        message_rect = message.get_rect(center = (400,150))
        message2 = alagard.render('There are none...', False, (50,50,50))
        message2_rect = message2.get_rect(center = (400, 250))
        message3 = alagard.render('sorry', False, (50,50,50))
        message3_rect = message3.get_rect(center = (400, 300))
        self.display.blit(message3, message3_rect)
        self.display.blit(message2, message2_rect)
        self.display.blit(message, message_rect)

    def show_about(self, score):
        self.main_menu = False
        self.display.fill((176,180,255))

        alagard = self.main_font
        message = alagard.render('About', False, (50,50,50))
        message_rect = message.get_rect(center = (400,150))
        about = alagard.render('use W, A, D or ^, <, > for moving', False, (50,50,50))
        about_rect = about.get_rect(center = (400, 300))
        about2 = alagard.render('good luck', False, (50,50,50))
        about2_rect = about2.get_rect(center = (400, 350))
        high = alagard.render('best time: ' + str(score / 1000), False, (0,200,0))
        high_rect = high.get_rect(center = (400, 200))
        self.display.blit(about2, about2_rect)
        self.display.blit(message, message_rect)
        self.display.blit(about, about_rect)
        self.display.blit(high, high_rect)

    def restart(self, data):
        data['player_start_position'] = (400,384)
        data['player_start_direction'] = (0,0)
        data['player_facing'] = 'left'
        data['map_start'] = 31400
        data['score'] = 0
        with open(Path('saving/save_last.txt'), 'w') as save_file:
            json.dump(data, save_file)
        
        return data
