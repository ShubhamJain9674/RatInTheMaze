import pygame

class Button:

    def __init__(self,text='',pos:(int,int)=(0,0),color=(200,200,200),hovered_color=(200,200,10)):

        self.button_text = text
        self.pos = pos
        self.font = pygame.font.Font(None,36)
        self.normal_surface = self.font.render(self.button_text,True,color)
        self.hovered_surface = self.font.render(self.button_text,True,hovered_color)
        
        self.surface = self.normal_surface
        self.rect = self.surface.get_rect()
        self.rect.x,self.rect.y = self.pos[0],self.pos[1] 

        self.hide = False    

    def is_hovered(self):
        if(self.rect.collidepoint(pygame.mouse.get_pos())):
            return True

        return False
    
    def on_hovered(self,func=None):
        if self.hide:
            return

        if(self.is_hovered()):
            self.surface = self.hovered_surface
            if(func):
                func()
        else:
            self.surface = self.normal_surface


    def on_pressed(self,func,args=None):
        if(self.hide):
            return

        if(self.is_hovered() and pygame.mouse.get_pressed(3)[0]):
            self.surface = self.normal_surface
            if args:
                func(*args)
            else:
                func()

    

    def update(self,dt):
        if self.hide:
            return

    def render(self,surface,dt):
        if(not self.hide):
            surface.blit(self.surface,self.pos)
        # pygame.draw.rect(surface,"red",self.rect)

    def hide_button(self):
        self.hide = True

    def show_button(self):
        self.hide = False