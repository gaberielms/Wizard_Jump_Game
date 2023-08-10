import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = position)
        self.deviation = 0

    def update(self, vert):
        self.rect.y += vert
        self.deviation += vert

    def save(self):
        return self.deviation

class StaticBlock(Block):
    def __init__(self, position, size, surface):
        super().__init__(position, size)
        self.image = surface