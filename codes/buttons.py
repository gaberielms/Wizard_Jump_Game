import pygame
from pathlib import Path

UNSELECTED = 'white'
SELECTED = 'red'
BUTTONSTATES = {
    True: SELECTED,
    False: UNSELECTED
}


class Button():

    
    def __init__(self, position, text_input):
        self.size = (175,50)
        self.pos = position
        self.hover = False
        self.pressed = False
        
        self.left = self.pos[0] - (self.size[0] // 2)
        self.top = self.pos[1] - (self.size[1] // 2)
        self.rect = pygame.rect.Rect(self.left, self.top, self.size[0], self.size[1])

        font = pygame.font.Font(Path('fonts/alagard.ttf'), 25)
        text_colour = (50,50,50)
        self.text_input = text_input
        self.text = font.render(self.text_input, False, text_colour)
        self.text_rect = self.text.get_rect(center=(position))

    def update(self, display):
        pygame.draw.rect(display, BUTTONSTATES[self.hover], self.rect)
        display.blit(self.text, self.text_rect)


class Slider():
    
    
    def __init__(self, pos, size, initial_val, min, max):
        self.pos = pos
        self.size = size
        self.hover = False
        self.grabbed = False

        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)
        self.slider_bot_pos = self.pos[1] + (size[1] // 2)

        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.container_rect = pygame.rect.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.rect.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos, 10, self.size[1])
        
        self.font = pygame.font.Font(Path('fonts/alagard.ttf'), 15)
        text_colour = (50,50,50)
        self.text = self.font.render(str(int(self.get_value())), True, text_colour)
        self.label_rect = self.text.get_rect(center = (self.pos[0], self.slider_bot_pos + 10))

    def move_slider(self, mouse_pos):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos

    def update(self, display):
        if self.button_rect.right > self.slider_right_pos:
            self.button_rect.right = self.slider_right_pos
        pygame.draw.rect(display, 'darkgray', self.container_rect)
        pygame.draw.rect(display, BUTTONSTATES[self.hover], self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val/val_range) * (self.max - self.min) + self.min
    
    def display_value(self, display):
        self.text = self.font.render(str(int(self.get_value())), True, 'white')
        display.blit(self.text, self.label_rect)
