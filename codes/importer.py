from csv import reader
import pygame
from os import walk

TILESIZE = 32


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
    blockx = surface.get_size()[0] // TILESIZE
    blocky = surface.get_size()[1] // TILESIZE
    
    cut_tiles = []
    for row in range(blockx):
        for col in range(blocky):
            x = col * TILESIZE
            y = row * TILESIZE
            new_sfc = pygame.Surface((TILESIZE,TILESIZE), flags = pygame.SRCALPHA)
            new_sfc.blit(surface, (0,0), pygame.Rect(x,y,TILESIZE,TILESIZE))
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

def import_background(path):
    sfc_lst = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path / image
            img_sfc = pygame.image.load(full_path).convert()
            img_sfc = pygame.transform.scale(img_sfc, (800, 8000))
            sfc_lst.append(img_sfc)
            
    return sfc_lst

