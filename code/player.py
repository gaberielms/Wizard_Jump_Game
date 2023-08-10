import pygame
from importer import import_folder


class Player(pygame.sprite.Sprite):

    def __init__(self, position, facing):
        super().__init__()
        self.import_player_assets()
        self.frame_index = 0
        self.animation_speed = 0.05
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = position)

        #movement
        self.direction = pygame.Vector2(0,0)
        self.gravity = 0.4
        self.max_gravity = 15
        self.speed = 4
        self.jump_speed = -10
        self.collision_rect = pygame.Rect(((self.rect.topleft[0] + 5), self.rect.topleft[1]),(18,49))

        #status
        self.status = 'idle'
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        if facing == 'right':
            self.facing_right = True
        else:
            self.facing_right = False

    def import_player_assets(self):
        character_path = 'graphics\player\\'
        self.animations = {'idle':[], 'run':[], 'jump':[], 'fall':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
            self.rect.bottomleft = ((self.collision_rect.bottomleft[0] - 5), self.collision_rect.bottomleft[1])
        else:
            flipped_img = pygame.transform.flip(image, True, False)
            self.image = flipped_img
            self.rect.bottomright = ((self.collision_rect.bottomright[0] + 5), self.collision_rect.bottomright[1])

    def inputs(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.direction.x = 1
            self.facing_right = True
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.jump()

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
        
    def apply_gravity(self):
        if self.direction.y <= self.max_gravity:
            self.direction.y += self.gravity
        self.collision_rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
    
    def update(self):
        self.inputs()
        # self.get_status()
        self.animate()
