from csv import reader
import pygame
from os import walk

tile_size = 32

def import_layout(path):
    terrain_map = []
    with open(path, 'r') as map:
        map_data = reader(map,delimiter=',')
        for row in map_data:
            terrain_map.append(list(row))
        return terrain_map
    
def import_cut_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    surface = pygame.transform.scale(surface, (128,128))
    blockx = surface.get_size()[0] // tile_size
    blocky = surface.get_size()[1] // tile_size
    
    cut_tiles = []
    for row in range(blockx):
        for col in range(blocky):
            x = col * tile_size
            y = row * tile_size
            new_sfc = pygame.Surface((tile_size,tile_size), flags = pygame.SRCALPHA)
            new_sfc.blit(surface, (0,0), pygame.Rect(x,y,tile_size,tile_size))
            cut_tiles.append(new_sfc)

    return cut_tiles

def import_folder(path):
    sfc_lst = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path / image
            img_sfc = pygame.image.load(full_path).convert_alpha()
            img_sfc = pygame.transform.scale(img_sfc, (34,56))
            sfc_lst.append(img_sfc)
    
    return sfc_lst