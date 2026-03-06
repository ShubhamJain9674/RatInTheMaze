
from spritesheet import SpriteSheet
import pygame
import os

class Rat(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        image_path = os.path.join(BASE_DIR,"Images","r_spritesheet.png")    

        self.rat_sprite_sheet = SpriteSheet(image_path)
        self.rat = self.rat_sprite_sheet.get_sprite(0,144,16,16)
        self.rat = pygame.transform.scale(self.rat,(50,50))





    def update(self):
        pass

    def render(self,surface):
        surface.blit(self.rat,(300,300))