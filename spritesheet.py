import pygame
import json


class SpriteSheet:

    def __init__(self,filename):
    
        self.filename = filename
        self.fmeta_data = self.filename.replace('png','json')

        self.SpriteSheet = pygame.image.load(filename).convert()

        with open(self.fmeta_data) as f:
            self.data = json.load(f)

        f.close()

    def get_sprite(self,x,y,w,h) -> pygame.Surface:

        sprite_s = pygame.Surface((w,h))
        sprite_s.set_colorkey((0,0,0))
        sprite_s.blit(self.SpriteSheet,(0,0),(x,y,w,h))
        

        return sprite_s


    def parse_sprite(self,name,frame) -> pygame.Surface:
        
        sprite = self.data[name][frame]
        x,y,w,h = sprite['x'],sprite['y'],sprite['w'],sprite['h']

        image = self.get_sprite(x,y,w,h)
        print(x,y,w,h)

        return image

#look into https://github.com/ChristianD37/YoutubeTutorials/tree/master/spritesheet for more image sprites