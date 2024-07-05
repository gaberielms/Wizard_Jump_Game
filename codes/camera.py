import pygame
from pathlib import Path

class Camera:


    def __init__(self, start_pos, player, display):
        self.player = player
        self.target = player.sprite
        self.blocks = pygame.sprite.Group()
        self.map_pos = start_pos
        self.display = display
        alagard = pygame.font.Font(Path('fonts/alagard.ttf'), 30)
        self.game_name = alagard.render('Wizard Jump', True, (176,180,255))
        self.game_name_rect = self.game_name.get_rect(center = (400,550))

    def update(self):
        target_pos = self.target.collision_rect.centery
        top = 120
        bot = 480
        target_dir = self.target.direction.y
        if (target_pos <= top) and (target_dir < 0):
            self.target.collision_rect.centery = top
            self.blocks.update(-target_dir)
        elif (target_pos >= bot) and (target_dir > 0):
            self.target.collision_rect.centery = bot
            self.blocks.update(-target_dir)
            
    def draw(self):
        self.blocks.draw(self.display)
        self.display.blit(self.game_name, self.game_name_rect)
        self.player.draw(self.display)

    def save(self):
        dev = self.blocks.sprites()[0].deviation
        self.map_pos -= dev
        return self.map_pos
    