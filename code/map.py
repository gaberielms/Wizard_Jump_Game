import pygame
from blocks import StaticBlock
from player import Player
from camera import Camera
from importer import *
from particles import Particles

class Map:

    def __init__(self, data, surface):
        # world map setup
        self.display_sfc = surface
        self.start_height = data['map_start']
        self.screen_height = data['screen_height']
        self.screen_width = data['screen_width']
        self.map_setup(data['map_data'], data['player_start_position'], data['player_facing'])
        self.current_x = 0
        self.current_y = 99999999999999
        self.particles = Particles(surface)

    def map_setup(self, layout, player_location, player_facing):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(player_location, player_facing))
        block_layout = import_layout(layout['terrain'])
        self.camera = Camera(self.start_height, self.player)

        for row_index, row in enumerate(block_layout):
            for col_index, place  in enumerate(row):
                if place != '-1':
                    x = col_index * tile_size
                    y = (row_index * tile_size) - self.start_height

                    terrain_blck_lst = import_cut_graphic('..\graphics\map\dungeon_blocks.png')
                    blck_sfc = terrain_blck_lst[int(place)]
                    block = StaticBlock((x,y), tile_size, blck_sfc)
                    self.blocks.add(block)
                    self.camera.blocks.add(block)


    def horizontal_movement(self):
        player = self.player.sprite
        player.collision_rect.x += player.direction.x * player.speed

        if player.collision_rect.left <= tile_size:
            player.collision_rect.left = tile_size
            player.on_left = True
        elif player.collision_rect.right >= (self.screen_width - tile_size):
            player.collision_rect.right = (self.screen_width - tile_size)
            player.on_right = True

        for block in self.blocks.sprites():
            if block.rect.colliderect(player.collision_rect):
                if player.direction.x < 0:
                    player.collision_rect.left = block.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.collision_rect.right = block.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right


    def vertical_movement(self):
        player = self.player.sprite
        player.apply_gravity()
        self.current_y = player.rect.centery

        for block in self.blocks.sprites():
            if block.rect.colliderect(player.collision_rect):
                if player.direction.y > 0:
                    player.collision_rect.bottom = block.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.collision_rect.top = block.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                    
        if player.on_ground and (player.direction.y < 0 or player.direction.y > 1):
            player.on_ground = False

    def particulate(self):
        player = self.player.sprite
        if player.on_ground:
            if player.direction.x != 0:
                if player.facing_right:
                    self.particles.add_particles(player.rect.left - 1, player.rect.bottom, player.direction.x, 5)
                else:
                    self.particles.add_particles(player.rect.right + 1, player.rect.bottom, player.direction.x, 5)

    def run(self):
        self.camera.draw(self.display_sfc)
        self.camera.update()
        self.player.update()
        self.vertical_movement()
        self.horizontal_movement()
        self.particulate()
        self.particles.emit()

    def save(self, data):
        player = self.player.sprite
        data['player_start_position'] = (player.rect.x, player.rect.y)
        data['player_start_direction'] = (player.direction.x, player.direction.y)
        if player.facing_right:
            data['player_facing'] = 'right'
        else:
            data['player_facing'] = 'left'
        data['map_start'] = self.camera.save()
        return data
