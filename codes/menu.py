import pygame, buttons
from pathlib import Path


class Menu:


    def __init__(self, display, menu_status, data) -> None:
        self.display = display
        self.menu_status = menu_status
        self.high_score = data['high_score']
        self.data = data
        self.title = ''
        self.messages = []
        self.title_font = pygame.font.Font(Path('fonts/alagard.ttf'), 30)
        self.font = pygame.font.Font(Path('fonts/alagard.ttf'), 25)
        self.info = self.update()
        self.bg = self.info[0]
        options = self.info[1]
        self.sliders = self.info[2]

        self.buttons = []
        for option in options:
            loc = (400, (options.index(option) * 75) + 240)
            self.buttons.append(buttons.Button(loc, option))

    def run(self):
        self.display.blit(self.bg, (0,0))
        self.display.blit(self.title, self.title_rect)
        for message, message_rect in self.messages:
            self.display.blit(message, message_rect)
        

        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for slider in self.sliders:
            if slider.container_rect.collidepoint(mouse_pos):
                if mouse[0]:
                    slider.grabbed = True
            if not mouse[0]:
                slider.grabbed = False
            if slider.button_rect.collidepoint(mouse_pos):  
                slider.hover = True
            if slider.grabbed:
                slider.move_slider(mouse_pos)
                slider.hover = True
                slider.display_value(self.display)
            else:
                slider.hover = False
            slider.update(self.display)

        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                if mouse[0]:
                    button.pressed = True
                button.hover = True
            else:
                button.hover = False
            if button.pressed:
                if not button.text_input == 'Play' and not button.text_input == 'Restart Game':
                    self.menu_status = button.text_input
                return button.text_input
            button.update(self.display)

    def update(self):
        options = []
        sliders = []
        background = pygame.surface.Surface((800,600))
        background.fill((176,180,255))

        if self.menu_status == 'main':
            self.title = self.title_font.render('Wizard Jump', True, (0, 150, 255))
            self.title_rect = self.title.get_rect(center = (400,140))
            message = self.title_font.render('(no longer speedrunable)', True, (0, 150, 255))
            message_rect = message.get_rect(center = (400,175))

            background = pygame.image.load(Path('graphics/menu/menu.jpg')).convert_alpha()
            options = ['Play', 'Settings', 'About', 'Restart Game']

        elif self.menu_status == 'Settings':
            self.title = self.title_font.render('Settings', True, (50,50,50))
            self.title_rect = self.title.get_rect(center = (400,100))
            volume = self.font.render('Music', True, (50,50,50))
            volume_rect = volume.get_rect(center = (400,400))
            volume_rect.right = 350
            other = self.font.render('Sounds', True, (50,50,50))
            other_rect = other.get_rect(center = (400, 350))
            other_rect.right = 350

            sliders.append(buttons.Slider((450, volume_rect.centery), (175, 25), self.data['volume'], 0, 100))
            sliders.append(buttons.Slider((450, other_rect.centery), (175, 25), self.data['sounds'], 0, 100))
            self.messages.append((volume, volume_rect))
            self.messages.append((other, other_rect))
        
        elif self.menu_status == 'About':
            self.title = self.title_font.render('About', True, (50,50,50))
            self.title_rect = self.title.get_rect(center = (400,100))
            message = self.font.render('use W, A, D or ^, <, > for moving', False, (50,50,50))
            message_rect = message.get_rect(center = (400, 300))
            high = self.title_font.render('best time: ' + str(self.high_score / 1000), False, (0,200,0))
            high_rect = high.get_rect(center = (400,200))

            self.messages.append((message, message_rect))
            self.messages.append((high, high_rect))

        return [background, options, sliders]
    