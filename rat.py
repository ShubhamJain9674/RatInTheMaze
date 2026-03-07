
from spritesheet import SpriteSheet,Animation
import pygame
import os




class Rat(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        BASE_DIR = os.path.dirname(__file__)
        image_path = os.path.join(BASE_DIR,"Images","r_spritesheet2.png")    

        self.rat_sprite_sheet = SpriteSheet(image_path)
        
        self.r_animation = Animation(
            self.rat_sprite_sheet,
            "rat1_r"
        )
        self.f_animation = Animation(
            self.rat_sprite_sheet,
            "rat1_f"
        )
        self.b_animation = Animation(
            self.rat_sprite_sheet,
            "rat1_b"
        )
        self.l_animation = Animation(
            self.rat_sprite_sheet,
            "rat1_r",
            (True,False)
        )


        self.animation = self.f_animation



        self.rat = self.animation.get_default()



        self.posx = 50
        self.posy = 50
        self.speed = 100
        self.can_move = True
        self.is_moving = False



    def move(self,dt,dirn = (0,0)):
        
        if(self.can_move):
            self.is_moving = True

            if(dirn[1] >= 1):
                self.animation = self.f_animation
            if(dirn[1] <= -1):
                self.animation = self.b_animation
            if(dirn[0] >= 1):
                self.animation = self.r_animation
            if(dirn[0] <= -1):
                self.animation = self.l_animation
             


            self.posx = self.posx + self.speed * dirn[0] * dt
            self.posy = self.posy + self.speed * dirn[1] * dt

        
        self.is_moving = True

    def stop(self):
        self.is_moving = False

    def update(self):
        pass

    def render(self,surface,dt):
        
        if(self.is_moving):
            sprite_image = self.animation.play(dt)
        else:
            sprite_image = self.animation.get_default()


        sprite_image = pygame.transform.scale(sprite_image,(50,50))
        surface.blit(sprite_image,(self.posx,self.posy))


    