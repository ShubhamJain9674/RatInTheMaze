import pygame
import os
from spritesheet import SpriteSheet,Animation

class Wall:

    def __init__(self,pos=(100,100),horizontal=False):

        BASE_DIR = os.path.dirname(__file__)
        IMAGE_PATH = os.path.join(BASE_DIR,"Images","w_spritesheet.png")
        self.sprite_sheet = SpriteSheet(IMAGE_PATH)

        self.w1_animation = Animation(self.sprite_sheet,"wall1")
        self.w2_animation = Animation(self.sprite_sheet,"wall2")
        self.w3_animation = Animation(self.sprite_sheet,"wall3")
        self.w4_animation = Animation(self.sprite_sheet,"wall4")

        self.animation = self.w3_animation



        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.wall = self.animation.get_default()
        if(horizontal):
            self.wall = pygame.transform.rotate(self.wall,90)


        self.rect = self.wall.get_rect() 
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        

    def get_height(self):
        return self.sprite_sheet.get_sprite_height(self.animation.name)
    
    def render(self,surface,dt):
        surface.blit(self.wall,(self.pos_x,self.pos_y))





class Cell:
    def __init__(self,pos=(100,100)):

        self.x = pos[0]
        self.y = pos[1]

        self.l_wall = Wall((self.x+0,self.y+0))
        self.t_wall = Wall((self.x + 0,self.y + 0),True)
        self.b_wall = Wall((self.x + 0,self.y +self.l_wall.get_height()),True)
        self.r_wall = Wall((self.x + self.l_wall.get_height(),self.y + 0))


    def render(self,canvas,dt):
        
        self.l_wall.render(canvas,dt)
        self.t_wall.render(canvas,dt)
        self.b_wall.render(canvas,dt)
        self.r_wall.render(canvas,dt)


    

