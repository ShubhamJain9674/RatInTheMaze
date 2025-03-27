import pygame
import itertools
class line:
    difficulty="EASY"
    def __init__(self,posx,posy,screen):
        if(line.difficulty=="EASY"):
            self.line=pygame.image.load("Images/LINE.png").convert_alpha()
        elif(line.difficulty=="MEDIUM"):
            self.line=pygame.image.load("Images/LINE3.png").convert_alpha()
        else:
            self.line=pygame.image.load("Images/LINE4.png").convert_alpha()
            
        self.line_rect=self.line.get_rect(midtop=(posx,posy))
        self.psx=posx
        self.psy=posy
        self.screen=screen
    def transform(self,angle):
        self.line=pygame.transform.rotate(self.line,angle)
        self.line_rect=self.line.get_rect(midleft=(self.psx,self.psy))
    def display(self):
        self.screen.blit(self.line,self.line_rect)
        #pygame.draw.rect(self.screen,(255,0,0),self.line_rect,2)
    def rectVal(self):
        return(self.line_rect)

    def collisioncheck(self,mousepos,mouserect):
        pass
    def position(self):
        return (self.psx,self.psy)
        
        


class parallelcell:
    def __init__(self,posx,posy,screen,angle=0):
        if(angle==90):
            self.topline=line(posx,posy,screen)
            self.topline.transform(90)
            self.topline_rect=self.topline.rectVal()
        
            self.bottomline=line(posx,posy+70,screen)
            self.bottomline.transform(90)
            self.bottomline_rect=self.bottomline.rectVal()

        else:
            self.topline=line(posx,posy,screen)
            self.topline_rect=self.topline.rectVal()
        
            self.bottomline=line(posx+70,posy,screen)
            self.bottomline_rect=self.bottomline.rectVal()

    def display(self):
        self.topline.display()
        self.bottomline.display()

    def toplineRectVal(self):
        return self.topline_rect
    def bottomlineRectVal(self):
        return self.bottomline_rect
    def RectVal(self):
        return [self.topline_rect,self.bottomline_rect]
        



class perpendicularcell:
    def __init__(self,posx,posy,screen,angle=0):
        if(angle==90):
            #inverted L in  X
            self.line1=line(posx,posy,screen)
            self.line1_rect=self.line1.rectVal()
            self.line2=line(posx,posy,screen)
            self.line2.transform(90)
            self.line2_rect=self.line2.rectVal()

        elif(angle==180):

            #inverted L in diagonal axis +ve xy axis

            self.line1=line(posx,posy,screen)
            self.line1.transform(90)
            self.line1_rect=self.line1.rectVal()

            self.line2=line(posx+70,posy,screen)
            self.line2_rect=self.line2.rectVal()

        elif(angle==270):
            # inverted L in y axis

            self.line1=line(posx,posy+70,screen)
            self.line1.transform(90)
            self.line1_rect=self.line1.rectVal()
            self.line2=line(posx+70,posy,screen)
            self.line2_rect=self.line2.rectVal()

        else:
            #L
            self.line1=line(posx,posy,screen)
            self.line1_rect=self.line1.rectVal()
            self.line2=line(posx,posy+70,screen)
            self.line2.transform(90)
            self.line2_rect=self.line2.rectVal()
                         
    def display(self):
        self.line1.display()
        self.line2.display()


    def line1RectVal(self):
        return self.line1_rect

    def line2RectVal(self):
        return self.line2_rect

    def RectVal(self):
        return [self.line1_rect,self.line2_rect]


class Ucell:
    def __init__(self,posx,posy,screen,angle=0):
        self.screen=screen
        if(angle==90):

            # c cell
            self.line1=line(posx,posy,screen)
            self.line1.transform(90)
            self.line1_rect=self.line1.rectVal()

            self.line2=line(posx,posy,screen)
            self.line2_rect=self.line2.rectVal()

            self.line3=line(posx,posy+70,screen)
            self.line3.transform(90)
            self.line3_rect=self.line3.rectVal()


        elif(angle==180):

            #inverted u x axis
            self.line1=line(posx,posy,screen)
            self.line1_rect=self.line1.rectVal()

            self.line2=line(posx,posy,screen)
            self.line2.transform(90)
            self.line2_rect=self.line2.rectVal()

            self.line3=line(posx+70,posy,screen)
            self.line3_rect=self.line3.rectVal()

        elif(angle==270):

            #inverted c y axis
            self.line1=line(posx,posy,screen)
            self.line1.transform(90)
            self.line1_rect=self.line1.rectVal()

            self.line2=line(posx+70,posy,screen)
            self.line2_rect=self.line2.rectVal()

            self.line3=line(posx,posy+70,screen)
            self.line3.transform(90)
            self.line3_rect=self.line3.rectVal()

        else:


            #u cell
            self.line1=line(posx,posy,screen)
            self.line1_rect=self.line1.rectVal()

            self.line2=line(posx,posy+70,screen)
            self.line2.transform(90)
            self.line2_rect=self.line2.rectVal()

            self.line3=line(posx+70,posy,screen)
            self.line3_rect=self.line3.rectVal()
            
            
    def display(self):
        self.line1.display()
        self.line2.display()
        self.line3.display()

    def line1RectVal(self):
        return self.line1_rect
    
    def line2RectVal(self):
        return self.line2_rect

    def line3RectVal(self):
        return self.line3_rect
    def RectVal(self):
        return [self.line1_rect,self.line2_rect,self.line3_rect]

        
    
        

        
        

        
        
