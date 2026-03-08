import pygame
import math
import json


class Animation:

    def __init__(self,
            sprite_sheet,
            name,
            flip = (False,False),
            anim_speed = 10
        ):

        self.sprite_sheet = sprite_sheet
        self.name = name
        self.frame_number = -1
        self.frame_time = 0
        self.anim_start = sprite_sheet.get_anim_start(name)
        self.anim_length = sprite_sheet.get_anim_length(name)
        self.flip = flip
        self.anim_speed = anim_speed

    def play(self,dt) -> pygame.Surface:

        self.frame_time = (self.frame_time + (dt * self.anim_speed) ) % self.anim_length
        self.frame_number = math.floor(self.frame_time)

        sprite = self.sprite_sheet.parse_sprite(self.name,str(self.frame_number))
        sprite = pygame.transform.flip(sprite,self.flip[0],self.flip[1])           
        
        return sprite

    def play_once(self,dt)->pygame.Surface:


        if(self.frame_time >= self.anim_length -1 ):
            sprite = self.sprite_sheet.parse_sprite(self.name,str(self.anim_length-1))
        else:
            self.frame_time = (self.frame_time + (dt * self.anim_speed) ) 
            self.frame_number = math.floor(self.frame_time)
            sprite = self.sprite_sheet.parse_sprite(self.name,str(self.frame_number))
        
        sprite = pygame.transform.flip(sprite,self.flip[0],self.flip[1])

        return sprite    


    def stop(self) -> pygame.Surface:
        self.frame_number = -1
        sprite = self.sprite_sheet.parse_sprite(self.name,str(frame_number))
        sprite = pygame.transform.flip(sprite,self.flip[0],self.flip[1])           

        return sprite           


    def get_default(self) -> pygame.Surface:
        
        sprite = self.sprite_sheet.parse_sprite(self.name,str(-1))
        sprite = pygame.transform.flip(sprite,self.flip[0],self.flip[1])           
        
        return sprite
    







class SpriteSheet:

    def __init__(self,filename):
    
        self.filename = filename
        self.fmeta_data = self.filename.replace('png','json')

        self.SpriteSheet = pygame.image.load(filename).convert_alpha()

        with open(self.fmeta_data) as f:
            self.data = json.load(f)

        f.close()

    def get_anim_length(self,name) -> int:
        return len(self.data[name]) - 1

    def get_sprite_height(self,name):
        return self.data[name]["-1"]['h']




    def get_anim_start(self,name):

        sprite = self.data[name]["-1"]
        return (sprite['x'],sprite['y'],sprite['w'],sprite['h'])



    def get_sprite(self,x,y,w,h) -> pygame.Surface:

        sprite_s = pygame.Surface((w,h),pygame.SRCALPHA)
        # sprite_s.set_colorkey((0,0,0))
        sprite_s.blit(self.SpriteSheet,(0,0),(x,y,w,h))
        

        return sprite_s


    def parse_sprite(self,name,frame) -> pygame.Surface:
        
        sprite = self.data[name][frame]
        x,y,w,h = sprite['x'],sprite['y'],sprite['w'],sprite['h']

        image = self.get_sprite(x,y,w,h)

        return image

#look into https://github.com/ChristianD37/YoutubeTutorials/tree/master/spritesheet for more image sprites