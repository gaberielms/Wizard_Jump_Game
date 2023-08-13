import pygame, sys
from pathlib import Path


class Button(pygame.sprite.Sprite):
    def __init__(self, position, text_input):
        super().__init__()

        font = pygame.font.Font(Path('fonts/alagard.ttf'), 25)
        text_colour = (50,50,50)
        
        self.image = pygame.surface.Surface((175,50))
        self.image.fill('white')
        self.rect = self.image.get_rect(center=(position))
        self.text_input = text_input
        self.text = font.render(self.text_input, False, text_colour)
        self.text_rect = self.text.get_rect(center=(position))
        self.hover = False

    def update(self, display):
        display.blit(self.image, self.rect)
        display.blit(self.text, self.text_rect)
        self.hover = False

    def get_input(self, mouse_pos):
        if (mouse_pos[0] in range(self.rect.left, self.rect.right)) and (mouse_pos[1] in range(self.rect.top, self.rect.bottom)):
            self.hover = True
    
    def set_colour(self, mouse_pos, display):
        if (mouse_pos[0] in range(self.rect.left, self.rect.right)) and (mouse_pos[1] in range(self.rect.top, self.rect.bottom)):
            self.image.fill('red')
            self.update(display)
        else:
            self.image.fill('white')
            self.update(display)    
