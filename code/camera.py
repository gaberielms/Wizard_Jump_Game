import pygame


class Camera:

    def __init__(self, start_pos, player):
        self.player = player
        self.target = player.sprite
        self.blocks = pygame.sprite.Group()
        self.map_pos = start_pos
        alagard = pygame.font.Font('..\\fonts\\alagard.ttf', 30)
        self.game_name = alagard.render('Wizard Jump', False, (176,180,255))
        self.game_name_rect = self.game_name.get_rect(center = (400,500))

    def update(self):
        target_pos = self.target.collision_rect.centery
        top = 120
        bot = 480
        if (target_pos <= top) and (self.target.direction.y < 0):
            self.target.collision_rect.centery = top
            self.blocks.update(-self.target.direction.y)
        elif (target_pos >= bot) and (self.target.direction.y > 0):
            self.target.collision_rect.centery = bot
            self.blocks.update(-self.target.direction.y)
            
    def draw(self, display):
        self.blocks.draw(display)
        display.blit(self.game_name, self.game_name_rect)
        self.player.draw(display)

    def save(self):
        dev = self.blocks.sprites()[0].deviation
        self.map_pos -= dev
        return self.map_pos
