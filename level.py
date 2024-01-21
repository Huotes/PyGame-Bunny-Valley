import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        
        #pega a primeira camada do display
        self.display_surface = pygame.display.get_surface()

        #grupo de sprites
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((640,360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()