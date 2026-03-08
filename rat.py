
from spritesheet import SpriteSheet,Animation
import pygame
import os


class Rat(pygame.sprite.Sprite):

    def __init__(self,pos=(110,110)):

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
        self.rect = self.rat.get_rect()


        self.posx = pos[0]
        self.posy = pos[1]
       

        self.speed = 100
        self.can_move = True
        self.is_moving = False

        self.can_move_left = True
        self.can_move_right = True
        self.can_move_top = True
        self.can_move_bottom = True

        #end state
        self.move_AI = False
        self.time_to_move = 0

    def reset_movement(self):
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_top = True
        self.can_move_bottom = True

    def collide_walls(self,rects):

        PUSH_FACTOR = 0.032
        for r in rects:

            if(self.rect.bottom > r.top and self.rect.top < r.bottom):  #if vertical overlap
                #check for horizontal overlaps
                if( self.rect.right >= r.left and self.rect.left <= r.left ):
                    self.can_move_right = False
                    self.posx = self.posx - self.speed  * PUSH_FACTOR
                if(self.rect.left <= r.right and self.rect.right >= r.right):
                    self.can_move_left = False
                    self.posx = self.posx - self.speed  * (-PUSH_FACTOR)
                
            if(self.rect.right > r.left and self.rect.left < r.right): #if horizontal overlap
                #check for vertical overlap
                if(self.rect.top <= r.bottom and self.rect.bottom >= r.bottom):
                    self.can_move_top = False
                    self.posy = self.posy - self.speed * (-PUSH_FACTOR)
                if(self.rect.bottom >= r.top and self.rect.top <= r.top):
                    self.can_move_bottom = False
                    self.posy = self.posy - self.speed * PUSH_FACTOR
        


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


            if(self.can_move_right and dirn[0] >= 1):
                self.posx = self.posx + self.speed * dirn[0] * dt
                       
            if(self.can_move_left and dirn[0] <= -1):
                self.posx = self.posx + self.speed * dirn[0] * dt
        
            if(self.can_move_top and dirn[1] <= -1):
                self.posy = self.posy + self.speed * dirn[1] * dt

            if(self.can_move_bottom and dirn[1] >= 1):
                self.posy = self.posy + self.speed * dirn[1] * dt
                

            # print(self.can_move_left,self.can_move_right,self.can_move_top,self.can_move_bottom)

            # self.reset_movement()
    


    def stop(self):
        self.is_moving = False

    def move_by_AI(self):
        self.can_move = False

        self.move_AI = True
        
    def update(self,dt):

        if(self.move_AI):
            self.time_to_move += dt
        if(self.time_to_move >= 1.4):
            self.is_moving = True
            self.posx = self.posx + self.speed  * dt

        if(self.is_moving):
            self.rat = self.animation.play(dt)
        else:
            self.rat = self.animation.get_default()


        self.rat = pygame.transform.scale(self.rat,(40,40))
        width = self.rat.get_width() - 4
        height = self.rat.get_height() - 4
        
        self.rect.update(self.posx,self.posy,width,height)


    def render(self,surface):
        
        surface.blit(self.rat,(self.posx,self.posy))
        # pygame.draw.rect(surface,"green",self.rect)


class Cheese(pygame.sprite.Sprite):
    def __init__(self,game_mode,pos):

        self.game_mode = game_mode

        BASE_DIR = os.path.dirname(__file__)
        image_path = os.path.join(BASE_DIR,"Images","s_spritesheet.png")  
        self.cheese_sprite_sheet = SpriteSheet(image_path)
        
        self.cheese_animation = Animation(
        self.cheese_sprite_sheet,
        "cheese"
        )
        self.cheese = self.cheese_animation.get_default()
        self.cheese = pygame.transform.scale(self.cheese,(40,40))

        self.pos = pos
        self.start_playing = False

        self.rect = self.cheese.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self,dt):

        if(self.start_playing):
            self.cheese = self.cheese_animation.play_once(dt)
        self.cheese = pygame.transform.scale(self.cheese,(40,40))

    def render(self,surface):
        
        # pygame.draw.rect(surface,"red",self.rect)
        surface.blit(self.cheese,self.pos)

    def get_rect(self):
        return self.rect

    def handle_collision(self):
        self.start_playing = True
        self.game_mode.end_game()
        