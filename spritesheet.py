import pygame


class SpriteSheet:

    def __init__(self,filename):
    
        self.filename = filename
        self.SpriteSheet = pygame.image.load(filename).convert()

    def get_sprite(self,x,y,w,h) -> pygame.Surface:

        sprite_s = pygame.Surface((w,h))
        sprite_s.set_colorkey((0,0,0))
        sprite_s.blit(self.SpriteSheet,(0,0),(x,y,w,h))
        
        return sprite_s

#look into https://github.com/ChristianD37/YoutubeTutorials/tree/master/spritesheet for more image sprites