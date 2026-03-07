
from spritesheet import SpriteSheet
import pygame
import os





class Rat(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        image_path = os.path.join(BASE_DIR,"Images","r_spritesheet2.png")    

        self.rat_sprite_sheet = SpriteSheet(image_path)
        self.rat = self.rat_sprite_sheet.get_sprite(0,0,16,16)
        self.rat = pygame.transform.scale(self.rat,(50,50))


        self.posx = 50
        self.posy = 50
        self.speed = 100
        self.can_move = True
        self.is_moving = False
        self.rat_frame = 1

    def move(self,dt,dirn = (0,0)):
        
        if(self.can_move):
            self.is_moving = True
            self.posx = self.posx + self.speed * dirn[0] * dt
            self.posy = self.posy + self.speed * dirn[1] * dt
        
        self.is_moving = True

    def update(self):
        pass

    def render(self,surface):

        sprite_image = self.rat
        
        if(self.is_moving):
            self.rat_frame= (self.rat_frame + 1) % 4
            sprite_image = self.rat_sprite_sheet.parse_sprite("rat1","move" + str(self.rat_frame))
            sprite_image = pygame.transform.scale(sprite_image,(50,50))
        

        surface.blit(sprite_image,(self.posx,self.posy))


    