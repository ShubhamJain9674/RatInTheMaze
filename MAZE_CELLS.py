import pygame
import itertools
from MAZE_GENERATION import *
import random
"""
cells naming convention :-
1,2,3 1,2,3 1,2,3
4,5,6 4,5,6 4,5,6         1   2   3
7,8,9 7,8,9 7,8,9

1,2,3 1,2,3 1,2,3
4,5,6 4,5,6 4,5,6         4   5   6
7,8,9 7,8,9 7,8,9

1,2,3 1,2,3 1,2,3
4,5,6 4,5,6 4,5,6         7   8   9
7,8,9 7,8,9 7,8,9


eg-class CELLbiggridNo_SMALLGRIDNOL/R/D/UE_SLNO

L=LEFT
R=RIGHT
D=DOWN
U=UP
"""

'''
class startCell_A_9DE_1:
    def __init__(self,posx,posy,screen):
        self.screen=screen
        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        self.cell5=parallelcell(posx+70,posy+140,screen,90)
        self.cell6=perpendicularcell(posx,posy+140,screen)
        self.line=line(posx+210,posy+140,screen)
        self.line2=line(posx,posy+70,screen)


        self.l7=self.line.rectVal()
        self.l8=self.line2.rectVal()


        

    def display(self):
        self.cell1.display()
        self.cell2.display()
        self.cell3.display()
        self.cell4.display()
        
        
        self.cell5.display()
        self.cell6.display()

        
        self.line.display()
        self.line2.display()

    def RectVal(self):
        l1=self.cell1.RectVal()
        l2=self.cell2.RectVal()
        l3=self.cell3.RectVal()
        l4=self.cell4.RectVal()
        l5=self.cell5.RectVal()
        l6=self.cell6.RectVal()

        l=list(itertools.chain(l1,l2,l3,l4,l5,l6))

        l.append(self.l7)
        l.append(self.l8)

        return(l)
'''
class mazecell:
    def __init__(self,posx,posy,screen,components,lineComp):
        self.screen=screen
        self.complist=components
        self.lineComp=lineComp

        
    def display(self):
        for components in self.complist:
            components.display()
        for lines in self.lineComp:
            lines.display()

            
    def RectVal(self):
        l1=[]
        for components in self.complist:
            l=components.RectVal()
            for i in l:
                l1.append(i)

        for lines in self.lineComp:
            l1.append(lines.rectVal())

        return l1
        




class CELL1_1TE_3RE_1:
    def __init__(self,posx,posy,screen):
        
        self.cell1=Ucell(posx+70,posy,screen,270)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=perpendicularcell(posx+140,posy+140,screen,270)

        self.line1=line(posx,posy,screen)        
        self.line2=line(posx+140,posy,screen)
        self.line2.transform(90)        
        self.line3=line(posx+70,posy+140,screen)
        self.line3.transform(90)        
        self.line4=line(posx+210,posy+70,screen)
        
        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]
        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_3RE_2:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+70,posy+140,screen,90)
        self.cell4=parallelcell(posx+140,posy,screen,90)
        
        
        


        self.line1=line(posx,posy+140,screen)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)
        self.line4=line(posx+140,posy+210,screen)
        self.line4.transform(90)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]
        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()





class CELL1_1TE_3RE_3:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+140,screen)
        self.cell3=parallelcell(posx+140,posy,screen,90)
        

        
        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+140,screen)
        self.line3.transform(90)
        self.line4=line(posx+210,posy+70,screen)
        self.line5=line(posx+140,posy+210,screen)
        self.line5.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4,self.line5]
        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_6RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=parallelcell(posx,posy+140,screen)
        self.cell3=Ucell(posx+140,posy,screen,90)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)
    


        self.line1=line(posx,posy,screen)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+140,screen)
        self.line3.transform(90)
        
        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_6RE_2:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=perpendicularcell(posx+140,posy+70,screen)
        
        
        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+210,screen)
        self.line4.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_6RE_3:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx+70,posy+140,screen,270)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        
        



        self.line1=line(posx,posy+140,screen)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+140,screen)
        self.line4=line(posx+140,posy+70,screen)
        

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        self.cell5=parallelcell(posx+140,posy+70,screen)
        self.cell6=perpendicularcell(posx+140,posy+140,screen)


        self.line1=line(posx,posy,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_9RE_2:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=perpendicularcell(posx+70,posy,screen,180)
        self.cell3=perpendicularcell(posx+70,posy+70,screen,270)
        

        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx,posy+140,screen)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+210,screen)
        self.line4.transform(90)
        self.line5=line(posx+210,posy+70,screen)
        self.line6=line(posx+140,posy,screen)
        self.line6.transform(90)


        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4,self.line5,self.line6]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL1_1TE_9RE_3:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=perpendicularcell(posx+140,posy+140,screen)
        


        self.line1=line(posx,posy,screen)
        self.line2=line(posx+70,posy+140,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy,screen)
        self.line3.transform(90)
        self.line4=line(posx+210,posy+70,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL1_1TE_9DE_1:
    def __init__(self,posx,posy,screen):
        self.screen=screen
        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        self.cell5=parallelcell(posx+70,posy+140,screen,90)
        self.cell6=perpendicularcell(posx,posy+140,screen)
        self.line=line(posx+210,posy+140,screen)
        self.line2=line(posx,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[self.line,self.line2]
        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        


class CELL1_1TE_9DE_2:

    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=perpendicularcell(posx+70,posy+140,screen)
        self.cell5=perpendicularcell(posx+140,posy+140,screen,180)



        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx,posy+140,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL1_1TE_9DE_3:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=perpendicularcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=perpendicularcell(posx+70,posy+140,screen,270)
        
    
        self.line1=line(posx,posy+140,screen)
        self.line2=line(posx+140,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)
        self.line4=line(posx+210,posy+140,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL1_1TE_8DE_1:
    def __init__(self,posx,posy,screen):
        
        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy+70,screen,270)
        self.cell4=perpendicularcell(posx,posy+70,screen)
        self.cell5=parallelcell(posx,posy+140,screen)
        
        
        self.line1=line(posx+140,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL1_1TE_7DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=Ucell(posx+70,posy+140,screen,270)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=parallelcell(posx+140,posy,screen,90)


        self.line1=line(posx,posy,screen)
        self.line2=line(posx,posy+140,screen)
        self.line3=line(posx+210,posy+70,screen)
        self.line4=line(posx+210,posy+140,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        

class CELL2_1LE_3RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,180)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+70,posy+140,screen,90)
        self.cell4=perpendicularcell(posx+140,posy+70,screen,270)
        

        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx,posy+140,screen)
        self.line3=line(posx+140,posy,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+210,screen)
        self.line4.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL2_1LE_6RE_1:
    def __init__(self,posx,posy,screen):
        
        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=Ucell(posx+70,posy+70,screen)
        self.cell5=perpendicularcell(posx+140,posy,screen,180)
        self.cell6=perpendicularcell(posx+140,posy+140,screen,270)
        
    
        self.line1=line(posx,posy,screen)
        self.line1.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL2_1LE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,180)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=perpendicularcell(posx+70,posy+140,screen,270)
        
        
        self.line1=line(posx,posy+140,screen)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+70,screen)
        self.line4=line(posx+210,posy+70,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_1LE_9DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,180)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+140,posy,screen,90)
        
        

        self.line1=line(posx,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+70,screen)
        self.line5=line(posx+210,posy+140,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4,self.line5]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_1LE_8DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+140,posy+70,screen,90)
        self.cell4=perpendicularcell(posx+140,posy+140,screen,270)



        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy,screen)
        self.line3.transform(90)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_1LE_7DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+70,posy+140,screen,90)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        self.cell5=perpendicularcell(posx+140,posy+140,screen,270)
        
        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx,posy+140,screen)
        self.line3=line(posx+210,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_4LE_3RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx+70,posy,screen,180)
        self.cell3=perpendicularcell(posx,posy+140,screen,180)
        self.cell4=Ucell(posx+140,posy+140,screen,90)

        self.line1=line(posx+140,posy,screen)
        self.line1.transform(90)        
        self.line2=line(posx+210,posy+70,screen)
        


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_4LE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy,screen,270)
        self.cell2=Ucell(posx+140,posy,screen,90)
        self.cell3=parallelcell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_4LE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx,posy+70,screen,270)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        self.cell5=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx,posy+210,screen)
        self.line1.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_4LE_9DE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=parallelcell(posx+140,posy,screen,90)
        self.cell4=parallelcell(posx+70,posy+140,screen,90)
        
        self.line1=line(posx+70,posy+70,screen)
        self.line2=line(posx+210,posy+140,screen)
        self.line3=line(posx,posy+140,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_4LE_8DE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy,screen,180)
        self.cell2=parallelcell(posx+140,posy,screen,90)
        self.cell3=parallelcell(posx,posy+140,screen,90)
        self.cell4=parallelcell(posx+140,posy+140,screen)



        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+210,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_4LE_7DE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=perpendicularcell(posx+140,posy+140,screen,270)

        self.line1=line(posx+140,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+140,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        
        

class CELL2_7LE_3RE_1:
    def __init__(self,posx,posy,screen):
    
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=parallelcell(posx+140,posy+70,screen)
        self.cell4=perpendicularcell(posx+70,posy+140,screen,270)

        self.line1=line(posx,posy+140,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_7LE_6RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx,posy+140,screen,270)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        self.cell5=perpendicularcell(posx+140,posy+140,screen,90)


        self.line1=line(posx,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL2_7LE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy+70,screen)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=parallelcell(posx+140,posy,screen,90)
        self.cell4=perpendicularcell(posx+140,posy+140,screen)



        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_7LE_9DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+70,posy+70,screen)
        self.cell4=Ucell(posx+70,posy+140,screen)
        


        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+210,posy+70,screen)
        self.line3=line(posx+210,posy+140,screen)
        self.line4=line(posx+140,posy,screen)
        self.line4.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_7LE_8DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx+140,posy,screen)
        self.cell4=perpendicularcell(posx+70,posy+140,screen,180)
        


        self.line1=line(posx,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+210,posy+140,screen)
        self.line3=line(posx+70,posy,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy,screen)
        self.line4.transform(90)
        

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL2_7LE_7DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        self.cell5=perpendicularcell(posx+140,posy+70,screen,270)
        

        self.line1=line(posx+70,posy+140,screen)
        self.line2=line(posx+140,posy+140,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL3_1LE_9DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=Ucell(posx+70,posy+70,screen,270)
        self.cell2=perpendicularcell(posx+140,posy,screen,180)
        


        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx,posy+70,screen)
        self.line3=line(posx,posy+140,screen)
        self.line4=line(posx+70,posy,screen)
        self.line4.transform(90)
        self.line5=line(posx+70,posy+210,screen)
        self.line5.transform(90)
        self.line6=line(posx+210,posy+70,screen)
        self.line7=line(posx+210,posy+140,screen)


        cellcomponents=[self.cell1,self.cell2]
        linelist=[self.line1,self.line2,self.line3,self.line4,self.line5,self.line6,self.line7]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL3_1LE_8DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy+70,screen,90)
        self.cell2=perpendicularcell(posx,posy+140,screen,270)
        self.cell3=Ucell(posx+140,posy,screen,270)
        self.cell4=Ucell(posx+140,posy+140,screen)


        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        


class CELL3_1LE_7DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx+70,posy,screen,90)
        self.cell2=perpendicularcell(posx+140,posy,screen,180)
        self.cell3=perpendicularcell(posx,posy+140,screen,90)
        self.cell4=perpendicularcell(posx+70,posy+140,screen,270)
        


        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+70,screen)
        self.line3=line(posx+210,posy+70,screen)
        self.line4=line(posx+210,posy+140,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL3_4LE_9DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx,posy+140,screen,180)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        self.cell5=parallelcell(posx+140,posy+70,screen)
        self.cell6=parallelcell(posx+140,posy+140,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL3_4LE_8DE_1:

    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx+140,posy,screen,180)
        self.cell3=Ucell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        self.cell5=parallelcell(posx+140,posy+140,screen)


        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+70,screen)



        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL3_4LE_7DE_1:

    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        self.cell5=parallelcell(posx+140,posy+140,screen)


        self.line1=line(posx,posy+140,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL3_7LE_9DE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx+140,posy,screen,180)
        self.cell3=Ucell(posx+140,posy+70,screen)
        self.cell4=perpendicularcell(posx+70,posy+140,screen)
        


        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+70,screen)
        self.line3=line(posx+210,posy+140,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL3_7LE_8DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx+70,posy,screen,90)
        self.cell2=perpendicularcell(posx+140,posy,screen,180)
        self.cell3=perpendicularcell(posx+140,posy+70,screen,270)
        



        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx,posy+70,screen)
        self.line3=line(posx,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+70,posy+140,screen)
        self.line4.transform(90)
        self.line5=line(posx+210,posy+140,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4,self.line5]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL3_7LE_7DE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        self.cell5=parallelcell(posx+140,posy+140,screen)
        self.cell6=perpendicularcell(posx,posy+140,screen,180)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL4_1TE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=perpendicularcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+140,posy,screen,90)
        self.cell5=perpendicularcell(posx+140,posy+140,screen,270)        


        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+70,screen)
        

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

        
class CELL4_1TE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=perpendicularcell(posx+140,posy,screen,270)
        self.cell5=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL4_1TE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=parallelcell(posx+140,posy+70,screen)        


        self.line1=line(posx,posy,screen)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+210,screen)
        self.line4.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL4_2TE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+70,posy+140,screen,90)
        self.cell5=perpendicularcell(posx+140,posy,screen,90)
        self.cell6=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx+210,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL4_2TE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx+70,posy,screen,270)
        self.cell3=perpendicularcell(posx+70,posy+70,screen,270)
        self.cell4=parallelcell(posx+140,posy,screen,90)
        self.cell5=perpendicularcell(posx,posy+140,screen)
        

        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL4_2TE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx+70,posy,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=parallelcell(posx+70,posy+140,screen,90)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)
        

        self.line1=line(posx,posy,screen)
        self.line2=line(posx,posy+70,screen)
        self.line3=line(posx+210,posy,screen)
        self.line4=line(posx+210,posy+70,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL4_3TE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=Ucell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=Ucell(posx+140,posy+70,screen,90)

        
        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)
        
        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL4_3TE_6RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+70,posy+140,screen,90)
        self.cell5=parallelcell(posx+140,posy+140,screen,90)
        self.cell6=perpendicularcell(posx+140,posy,screen,270)

        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        
class CELL4_3TE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+70,posy+140,screen,90)
        self.cell5=perpendicularcell(posx+140,posy,screen,270)

        self.line1=line(posx+210,posy+70,screen)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        
class CELL5_1LE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy+140,screen,270)
        self.cell2=perpendicularcell(posx+70,posy+140,screen,270)
        self.cell3=perpendicularcell(posx+140,posy+140,screen,270)

        self.line1=line(posx,posy+70,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+70,screen)
        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL5_1LE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy,screen,180)
        self.cell3=perpendicularcell(posx,posy+140,screen)
        self.cell4=parallelcell(posx+70,posy+140,screen,90)
        self.cell5=perpendicularcell(posx+140,posy+140,screen,270)
        self.cell6=parallelcell(posx+140,posy,screen,90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5,self.cell6]
        linelist=[]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_1LE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx+140,posy+70,screen,90)



        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+70,posy+210,screen)
        self.line4.transform(90)
        self.line5=line(posx+140,posy+210,screen)
        self.line5.transform(90)
        self.line6=line(posx+210,posy,screen)

        cellcomponents=[self.cell1,self.cell2]
        linelist=[self.line1,self.line2,self.line3,self.line4,self.line5,self.line6]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

    
class CELL5_4LE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,90)
        self.cell4=perpendicularcell(posx+140,posy+70,screen,270)

        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_4LE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy+140,screen,90)
        self.cell2=Ucell(posx+70,posy,screen,270)
        self.cell3=perpendicularcell(posx+140,posy+140,screen,270)
        



        self.line1=line(posx,posy,screen)
        self.line2=line(posx+140,posy+70,screen)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+210,posy,screen)
        
        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_4LE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy+140,screen)
        self.cell2=Ucell(posx+70,posy,screen,270)
        self.cell3=parallelcell(posx+70,posy+140,screen,90)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx,posy+70,screen)
        self.line1.transform(90)
        self.line2=line(posx+210,posy+70,screen)
        self.line2=line(posx+140,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)


        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()



class CELL5_7LE_3RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=parallelcell(posx+140,posy,screen,90)
        self.cell4=perpendicularcell(posx+140,posy+140,screen,270)


        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_7LE_6RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        
        
class CELL5_7LE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,180)
        self.cell2=parallelcell(posx,posy+70,screen)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=parallelcell(posx+140,posy,screen,90)
        self.cell5=perpendicularcell(posx+70,posy+140,screen,270)
        


        self.line1=line(posx+210,posy+70,screen)
        self.line2=line(posx,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_1TE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=perpendicularcell(posx+140,posy+70,screen,180)
        self.cell3=Ucell(posx,posy+140,screen,90)
        self.cell4=parallelcell(posx+70,posy+140,screen,90)
        self.cell5=parallelcell(posx+140,posy+140,screen,90)



        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_1TE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy+140,screen,270)
        self.cell2=perpendicularcell(posx+70,posy,screen,270)
        self.cell3=Ucell(posx+140,posy+140,screen,90)
        
        self.line1=line(posx,posy,screen)
        self.line2=line(posx,posy+70,screen)        
        self.line3=line(posx+210,posy,screen)
        self.line4=line(posx+70,posy+210,screen)
        self.line4.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        
class CELL5_1TE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+70,posy,screen,180)
        self.cell4=parallelcell(posx+70,posy+70,screen)
        
        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy,screen)
        self.line3.transform(90)
        self.line4=line(posx+210,posy+70,screen)
        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_2TE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+70,posy,screen,270)


        self.line1=line(posx+70,posy+70,screen)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_2TE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy,screen,180)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=perpendicularcell(posx+70,posy+70,screen,270)
        self.cell4=perpendicularcell(posx+140,posy,screen,270)

        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_2TE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=perpendicularcell(posx,posy+70,screen)
        self.cell2=perpendicularcell(posx,posy+140,screen,270)
        self.cell3=perpendicularcell(posx+70,posy,screen,270)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)
        



        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        
        
        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_3TE_3RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,90)
        self.cell2=perpendicularcell(posx,posy+70,screen,270)
        self.cell3=Ucell(posx+140,posy+70,screen,90)
        self.cell4=perpendicularcell(posx+140,posy+140,screen)

        self.line1=line(posx,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()
        
class CELL5_3TE_6RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy+70,screen,270)
        self.cell2=perpendicularcell(posx+70,posy,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,270)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)

        self.line1=line(posx,posy,screen)
        self.line2=line(posx,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL5_3TE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen,180)
        self.cell2=perpendicularcell(posx,posy+140,screen)
        self.cell3=parallelcell(posx+70,posy+140,screen,90)
        self.cell4=parallelcell(posx+140,posy+140,screen,90)
        self.cell5=perpendicularcell(posx+140,posy,screen,270)
        

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL6_1LE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy+70,screen,270)
        self.cell2=Ucell(posx+140,posy,screen,180)
        self.cell3=parallelcell(posx+140,posy+70,screen)     

        self.line1=line(posx,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+70,posy+210,screen)
        self.line3.transform(90)
        self.line4=line(posx+140,posy+210,screen)
        self.line4.transform(90)
    
        
        cellcomponents=[self.cell1,self.cell2,self.cell3]
        linelist=[self.line1,self.line2,self.line3,self.line4]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL6_4LE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=Ucell(posx,posy,screen,270)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=parallelcell(posx+70,posy,screen,90)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        
        
        self.line1=line(posx+210,posy,screen)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL6_7LE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx,posy,screen)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=perpendicularcell(posx+140,posy,screen,180)
        self.cell4=parallelcell(posx+140,posy+70,screen)
        self.cell5=perpendicularcell(posx+140,posy+140,screen)
        
        self.line1=line(posx+70,posy,screen)
        self.line1.transform(90)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4,self.cell5]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL6_1TE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=perpendicularcell(posx+70,posy,screen)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=parallelcell(posx+70,posy+140,screen,90)
        self.cell4=perpendicularcell(posx+140,posy,screen,180)
        
        

        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+210,posy+70,screen)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()


class CELL6_2TE_9RE_1:
    def __init__(self,posx,posy,screen):
        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=parallelcell(posx+140,posy,screen)
        self.cell4=parallelcell(posx+140,posy+70,screen)


        self.line1=line(posx+70,posy+210,screen)
        self.line1.transform(90)
        self.line2=line(posx+140,posy+210,screen)
        self.line2.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

class CELL6_3TE_9RE_1:
    def __init__(self,posx,posy,screen):

        self.cell1=parallelcell(posx,posy,screen,90)
        self.cell2=parallelcell(posx,posy+140,screen,90)
        self.cell3=parallelcell(posx+140,posy,screen)
        self.cell4=perpendicularcell(posx+140,posy+70,screen,270)
        


        self.line1=line(posx,posy+70,screen)
        self.line2=line(posx+70,posy+210,screen)
        self.line2.transform(90)
        self.line3=line(posx+140,posy+210,screen)
        self.line3.transform(90)

        cellcomponents=[self.cell1,self.cell2,self.cell3,self.cell4]
        linelist=[self.line1,self.line2,self.line3]

        self.maze=mazecell(posx,posy,screen,cellcomponents,linelist)

    def display(self):
        self.maze.display()
    def RectVal(self):
        return self.maze.RectVal()

MAZE1=(CELL1_1TE_3RE_1,CELL1_1TE_3RE_2,CELL1_1TE_3RE_3,CELL1_1TE_6RE_1,CELL1_1TE_6RE_2,CELL1_1TE_6RE_3,CELL1_1TE_9RE_1,CELL1_1TE_9RE_2,CELL1_1TE_9RE_3,CELL1_1TE_9DE_1,CELL1_1TE_8DE_1,CELL1_1TE_7DE_1)
def RandomMaze(posx,posy,screen):
    cells=[]
    cell1=random.choice(MAZE1)(posx,posy,screen)
    print(type(cell1).__name__)
    cells.append(cell1)

    #for cell2:-
    if(type(cell1).__name__[11:13]=="RE"):
        if(type(cell1).__name__[10:11]=="3"):
            cell2=random.choice((CELL2_1LE_3RE_1,CELL2_1LE_6RE_1,CELL2_1LE_9RE_1,CELL2_1LE_9DE_1,CELL2_1LE_8DE_1,CELL2_1LE_7DE_1))(posx+210,posy,screen)
            cells.append(cell2)
            print(type(cell2).__name__)
        elif(type(cell1).__name__[10:11]=="6"):
            cell2=random.choice((CELL2_4LE_3RE_1,CELL2_4LE_6RE_1,CELL2_4LE_9RE_1,CELL2_4LE_9DE_1,CELL2_4LE_8DE_1,CELL2_4LE_7DE_1))(posx+210,posy,screen)
            cells.append(cell2)
            print(type(cell2).__name__)
        elif(type(cell1).__name__[10:11]=="9"):
            cell2=random.choice((CELL2_7LE_3RE_1,CELL2_7LE_6RE_1,CELL2_7LE_9RE_1,CELL2_7LE_9DE_1,CELL2_7LE_8DE_1,CELL2_7LE_7DE_1))(posx+210,posy,screen)
            cells.append(cell2)
            print(type(cell2).__name__)
    else:
        cell2=random.choice((CELL2_1LE_3RE_1,CELL2_1LE_6RE_1,CELL2_1LE_9RE_1,CELL2_1LE_9DE_1,CELL2_1LE_8DE_1,CELL2_1LE_7DE_1,CELL2_4LE_3RE_1,CELL2_4LE_6RE_1,CELL2_4LE_9RE_1,CELL2_4LE_9DE_1,CELL2_4LE_8DE_1,CELL2_4LE_7DE_1,CELL2_7LE_3RE_1,CELL2_7LE_6RE_1,CELL2_7LE_9RE_1,CELL2_7LE_9DE_1,CELL2_7LE_8DE_1,CELL2_7LE_7DE_1))(posx+210,posy,screen)
        cells.append(cell2)
        print(type(cell2).__name__)




    #for cell3:-
    if(type(cell2).__name__[11:13]=="RE"):
        if(type(cell2).__name__[10:11]=="3"):
            cell3=random.choice((CELL2_1LE_3RE_1,CELL2_1LE_6RE_1,CELL2_1LE_9RE_1,CELL2_1LE_9DE_1,CELL2_1LE_8DE_1,CELL2_1LE_7DE_1))(posx+420,posy,screen)
            cells.append(cell3)
            print(type(cell3).__name__)
        elif(type(cell2).__name__[10:11]=="6"):
            cell3=random.choice((CELL2_4LE_3RE_1,CELL2_4LE_6RE_1,CELL2_4LE_9RE_1,CELL2_4LE_9DE_1,CELL2_4LE_8DE_1,CELL2_4LE_7DE_1))(posx+420,posy,screen)
            cells.append(cell3)
            print(type(cell3).__name__)
        elif(type(cell2).__name__[10:11]=="9"):
            cell3=random.choice((CELL2_7LE_3RE_1,CELL2_7LE_6RE_1,CELL2_7LE_9RE_1,CELL2_7LE_9DE_1,CELL2_7LE_8DE_1,CELL2_7LE_7DE_1))(posx+420,posy,screen)
            cells.append(cell3)
            print(type(cell3).__name__)
    else:
        cell3=random.choice((CELL2_1LE_3RE_1,CELL2_1LE_6RE_1,CELL2_1LE_9RE_1,CELL2_1LE_9DE_1,CELL2_1LE_8DE_1,CELL2_1LE_7DE_1,CELL2_4LE_3RE_1,CELL2_4LE_6RE_1,CELL2_4LE_9RE_1,CELL2_4LE_9DE_1,CELL2_4LE_8DE_1,CELL2_4LE_7DE_1,CELL2_7LE_3RE_1,CELL2_7LE_6RE_1,CELL2_7LE_9RE_1,CELL2_7LE_9DE_1,CELL2_7LE_8DE_1,CELL2_7LE_7DE_1))(posx+420,posy,screen)
        cells.append(cell3)
        print(type(cell3).__name__)
    #for cell4:-
    if(type(cell3).__name__[11:13]=="RE" and type(cell2).__name__[11:13]=="RE" and type(cell1).__name__[11:13]=="RE"):
        if(type(cell3).__name__[10:11]=="3"):
            cell4=random.choice((CELL2_1LE_3RE_1,CELL2_1LE_6RE_1,CELL2_1LE_9RE_1,CELL2_1LE_9DE_1,CELL2_1LE_8DE_1,CELL2_1LE_7DE_1))(posx+630,posy,screen)
            cells.append(cell4)
            print(type(cell4).__name__)
        elif(type(cell3).__name__[10:11]=="6"):
            cell4=random.choice((CELL2_4LE_3RE_1,CELL2_4LE_6RE_1,CELL2_4LE_9RE_1,CELL2_4LE_9DE_1,CELL2_4LE_8DE_1,CELL2_4LE_7DE_1))(posx+630,posy,screen)
            cells.append(cell4)
            print(type(cell4).__name__)
        elif(type(cell3).__name__[10:11]=="9"):
            cell4=random.choice((CELL2_7LE_3RE_1,CELL2_7LE_6RE_1,CELL2_7LE_9RE_1,CELL2_7LE_9DE_1,CELL2_7LE_8DE_1,CELL2_7LE_7DE_1))(posx+630,posy,screen)
            cells.append(cell4)
            print(type(cell4).__name__)
    else:
        cell4=random.choice((CELL2_1LE_3RE_1,CELL2_1LE_6RE_1,CELL2_1LE_9RE_1,CELL2_1LE_9DE_1,CELL2_1LE_8DE_1,CELL2_1LE_7DE_1,CELL2_4LE_3RE_1,CELL2_4LE_6RE_1,CELL2_4LE_9RE_1,CELL2_4LE_9DE_1,CELL2_4LE_8DE_1,CELL2_4LE_7DE_1,CELL2_7LE_3RE_1,CELL2_7LE_6RE_1,CELL2_7LE_9RE_1,CELL2_7LE_9DE_1,CELL2_7LE_8DE_1,CELL2_7LE_7DE_1))(posx+630,posy,screen)
        cells.append(cell4)
        print(type(cell4).__name__)
    

    #for cell5:-
    if(type(cell4).__name__[11:13]=="RE"):
        if(type(cell4).__name__[10:11]=="3"):
            cell5=random.choice((CELL3_1LE_9DE_1,CELL3_1LE_8DE_1,CELL3_1LE_7DE_1))(posx+840,posy,screen)
            cells.append(cell5)
            print(type(cell5).__name__)
        elif(type(cell4).__name__[10:11]=="6"):
            cell5=random.choice((CELL3_4LE_9DE_1,CELL3_4LE_8DE_1,CELL3_4LE_7DE_1))(posx+840,posy,screen)
            cells.append(cell5)
            print(type(cell5).__name__)
        elif(type(cell4).__name__[10:11]=="9"):
            cell5=random.choice((CELL3_7LE_9DE_1,CELL3_7LE_8DE_1,CELL3_7LE_7DE_1))(posx+840,posy,screen)
            cells.append(cell5)
            print(type(cell5).__name__)
    else:
        cell5=random.choice((CELL3_1LE_9DE_1,CELL3_1LE_8DE_1,CELL3_1LE_7DE_1,CELL3_4LE_9DE_1,CELL3_4LE_8DE_1,CELL3_4LE_7DE_1,CELL3_7LE_9DE_1,CELL3_7LE_8DE_1,CELL3_7LE_7DE_1))(posx+840,posy,screen)
        cells.append(cell5)
        print(type(cell5).__name__)

        
        
    #for cell6:-
    if(type(cell1).__name__[11:13]=="DE"):
        if(type(cell1).__name__[10:11]=="7"):
            cell6=random.choice((CELL4_1TE_3RE_1,CELL4_1TE_6RE_1,CELL4_1TE_9RE_1))(posx,posy+210,screen)
            cells.append(cell6)
            print(type(cell6).__name__)
        if(type(cell1).__name__[10:11]=="8"):
            cell6=random.choice((CELL4_2TE_3RE_1,CELL4_2TE_6RE_1,CELL4_2TE_9RE_1))(posx,posy+210,screen)
            cells.append(cell6)
            print(type(cell6).__name__)
        if(type(cell1).__name__[10:11]=="9"):
            cell6=random.choice((CELL4_3TE_3RE_1,CELL4_3TE_6RE_1,CELL4_3TE_9RE_1))(posx,posy+210,screen)
            cells.append(cell6)
            print(type(cell6).__name__)
    else:
        cell6=random.choice((CELL4_1TE_3RE_1,CELL4_1TE_6RE_1,CELL4_1TE_9RE_1,CELL4_2TE_3RE_1,CELL4_2TE_6RE_1,CELL4_2TE_9RE_1,CELL4_3TE_3RE_1,CELL4_3TE_6RE_1,CELL4_3TE_9RE_1))(posx,posy+210,screen)
        cells.append(cell6)
        print(type(cell6).__name__)

    #for cell7:-
    if(type(cell2).__name__[11:13]=="DE" and type(cell1).__name__[11:13]!="DE"):
        if(type(cell2).__name__[10:11]=="7"):
            cell7=random.choice((CELL5_1TE_3RE_1,CELL5_1TE_6RE_1,CELL5_1TE_9RE_1))(posx+210,posy+210,screen)
            cells.append(cell7)
            print(type(cell7).__name__)
        if(type(cell2).__name__[10:11]=="8"):
            cell7=random.choice((CELL5_2TE_3RE_1,CELL5_2TE_6RE_1,CELL5_2TE_9RE_1))(posx+210,posy+210,screen)
            cells.append(cell7)
            print(type(cell7).__name__)
        if(type(cell2).__name__[10:11]=="9"):
            cell7=random.choice((CELL5_3TE_3RE_1,CELL5_3TE_6RE_1,CELL5_3TE_9RE_1))(posx+210,posy+210,screen)
            cells.append(cell7)
            print(type(cell7).__name__)
    elif(type(cell6).__name__[11:13]=="RE"):
        if(type(cell6).__name__[10:11]=="3"):
            cell7=random.choice((CELL5_1LE_3RE_1,CELL5_1LE_6RE_1,CELL5_1LE_9RE_1))(posx+210,posy+210,screen)
            cells.append(cell7)
            print(type(cell7).__name__)
        if(type(cell6).__name__[10:11]=="6"):
            cell7=random.choice((CELL5_4LE_3RE_1,CELL5_4LE_6RE_1,CELL5_4LE_9RE_1))(posx+210,posy+210,screen)
            cells.append(cell7)
            print(type(cell7).__name__)
        if(type(cell6).__name__[10:11]=="9"):
            cell7=random.choice((CELL5_7LE_3RE_1,CELL5_7LE_6RE_1,CELL5_7LE_9RE_1))(posx+210,posy+210,screen)
            cells.append(cell7)
            print(type(cell7).__name__)
    else:
        cell7=random.choice(CELL5_1TE_3RE_1,CELL5_1TE_6RE_1,CELL5_1TE_9RE_1,CELL5_2TE_3RE_1,CELL5_2TE_6RE_1,CELL5_2TE_9RE_1,CELL5_3TE_3RE_1,CELL5_3TE_6RE_1,CELL5_3TE_9RE_1)(posx+210,posy+210,screen)
        cells.append(cell7)
        print(type(cell7).__name__)
    
    #for cell8:-
    if(type(cell3).__name__[11:13]=="DE" and type(cell1).__name__[11:13]!="DE" and type(cell2).__name__[11:13]!="DE" ):
        if(type(cell3).__name__[10:11]=="7"):
            cell8=random.choice((CELL5_1TE_3RE_1,CELL5_1TE_6RE_1,CELL5_1TE_9RE_1))(posx+420,posy+210,screen)
            cells.append(cell8)
            print(type(cell8).__name__)
        if(type(cell3).__name__[10:11]=="8"):
            cell8=random.choice((CELL5_2TE_3RE_1,CELL5_2TE_6RE_1,CELL5_2TE_9RE_1))(posx+420,posy+210,screen)
            cells.append(cell8)
            print(type(cell8).__name__)
        if(type(cell3).__name__[10:11]=="9"):
            cell8=random.choice((CELL5_3TE_3RE_1,CELL5_3TE_6RE_1,CELL5_3TE_9RE_1))(posx+420,posy+210,screen)
            cells.append(cell8)
            print(type(cell8).__name__)
    elif(type(cell7).__name__[11:13]=="RE"):
        if(type(cell7).__name__[10:11]=="3"):
            cell8=random.choice((CELL5_1LE_3RE_1,CELL5_1LE_6RE_1,CELL5_1LE_9RE_1))(posx+420,posy+210,screen)
            cells.append(cell8)
            print(type(cell8).__name__)
        if(type(cell7).__name__[10:11]=="6"):
            cell8=random.choice((CELL5_4LE_3RE_1,CELL5_4LE_6RE_1,CELL5_4LE_9RE_1))(posx+420,posy+210,screen)
            cells.append(cell8)
            print(type(cell8).__name__)
        if(type(cell7).__name__[10:11]=="9"):
            cell8=random.choice((CELL5_7LE_3RE_1,CELL5_7LE_6RE_1,CELL5_7LE_9RE_1))(posx+420,posy+210,screen)
            cells.append(cell8)
            print(type(cell8).__name__)
    else:
        cell8=random.choice(CELL5_1TE_3RE_1,CELL5_1TE_6RE_1,CELL5_1TE_9RE_1,CELL5_2TE_3RE_1,CELL5_2TE_6RE_1,CELL5_2TE_9RE_1,CELL5_3TE_3RE_1,CELL5_3TE_6RE_1,CELL5_3TE_9RE_1)(posx+420,posy+210,screen)
        cells.append(cell8)
        print(type(cell8).__name__)
            
    #for cell9:-
    if(type(cell4).__name__[11:13]=="DE" and type(cell1).__name__[11:13]!="DE" and  type(cell2).__name__[11:13]!="DE" and  type(cell3).__name__[11:13]!="DE" ):
        if(type(cell4).__name__[10:11]=="7"):
            cell9=random.choice((CELL5_1TE_3RE_1,CELL5_1TE_6RE_1,CELL5_1TE_9RE_1))(posx+630,posy+210,screen)
            cells.append(cell9)
            print(type(cell9).__name__)
        if(type(cell4).__name__[10:11]=="8"):
            cell9=random.choice((CELL5_2TE_3RE_1,CELL5_2TE_6RE_1,CELL5_2TE_9RE_1))(posx+630,posy+210,screen)
            cells.append(cell9)
            print(type(cell9).__name__)
        if(type(cell4).__name__[10:11]=="9"):
            cell9=random.choice((CELL5_3TE_3RE_1,CELL5_3TE_6RE_1,CELL5_3TE_9RE_1))(posx+630,posy+210,screen)
            cells.append(cell9)
            print(type(cell9).__name__)
    elif(type(cell8).__name__[11:13]=="RE"):
        if(type(cell8).__name__[10:11]=="3"):
            cell9=random.choice((CELL5_1LE_3RE_1,CELL5_1LE_6RE_1,CELL5_1LE_9RE_1))(posx+630,posy+210,screen)
            cells.append(cell9)
            print(type(cell9).__name__)
        if(type(cell8).__name__[10:11]=="6"):
            cell9=random.choice((CELL5_4LE_3RE_1,CELL5_4LE_6RE_1,CELL5_4LE_9RE_1))(posx+630,posy+210,screen)
            cells.append(cell9)
            print(type(cell9).__name__)
        if(type(cell8).__name__[10:11]=="9"):
            cell9=random.choice((CELL5_7LE_3RE_1,CELL5_7LE_6RE_1,CELL5_7LE_9RE_1))(posx+630,posy+210,screen)
            cells.append(cell9)
            print(type(cell9).__name__)
    else:
        cell9=random.choice(CELL5_1TE_3RE_1,CELL5_1TE_6RE_1,CELL5_1TE_9RE_1,CELL5_2TE_3RE_1,CELL5_2TE_6RE_1,CELL5_2TE_9RE_1,CELL5_3TE_3RE_1,CELL5_3TE_6RE_1,CELL5_3TE_9RE_1)(posx+630,posy+210,screen)
        cells.append(cell9)
        print(type(cell9).__name__)

    #for cell10:-
    if((type(cell1).__name__[11:13]=="RE") and (type(cell2).__name__[11:13]=="RE") and (type(cell3).__name__[11:13]=="RE") and (type(cell4).__name__[11:13]=="RE") ):
        if(type(cell5).__name__[10:11]=="7"):
            cell10=CELL6_1TE_9RE_1(posx+840,posy+210,screen)
            cells.append(cell10)
            print(type(cell10).__name__)
        elif(type(cell5).__name__[10:11]=="8"):
            cell10=CELL6_2TE_9RE_1(posx+840,posy+210,screen)
            cells.append(cell10)
            print(type(cell10).__name__)
        elif(type(cell5).__name__[10:11]=="9"):
            cell10=CELL6_3TE_9RE_1(posx+840,posy+210,screen)
            cells.append(cell10)
            print(type(cell10).__name__)
    else:
        if(type(cell9).__name__[10:11]=="3"):
            cell10=CELL6_1LE_9RE_1(posx+840,posy+210,screen)
            cells.append(cell10)
            print(type(cell10).__name__)
        elif(type(cell9).__name__[10:11]=="6"):
            cell10=CELL6_4LE_9RE_1(posx+840,posy+210,screen)
            cells.append(cell10)
            print(type(cell10).__name__)
        elif(type(cell9).__name__[10:11]=="9"):
            cell10=CELL6_7LE_9RE_1(posx+840,posy+210,screen)
            cells.append(cell10)
            print(type(cell10).__name__)
  
                

    return(cells)
    
    
