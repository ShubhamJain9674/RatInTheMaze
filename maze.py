import pygame
import os
import random
from spritesheet import SpriteSheet,Animation
from enum import Enum

class WallLocation(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3 

class WallType(Enum):
    WALL0 = 0
    WALL1 = 1
    WALL2 = 2
    WALL3 = 3



class Wall(pygame.sprite.Sprite):

    def __init__(self,pos=(100,100),horizontal=False,type: WallType = WallType.WALL2):

        BASE_DIR = os.path.dirname(__file__)
        IMAGE_PATH = os.path.join(BASE_DIR,"Images","w_spritesheet.png")
        self.sprite_sheet = SpriteSheet(IMAGE_PATH)

        self.w0_animation = Animation(self.sprite_sheet,"wall0")
        self.w1_animation = Animation(self.sprite_sheet,"wall1")
        self.w2_animation = Animation(self.sprite_sheet,"wall2")
        self.w3_animation = Animation(self.sprite_sheet,"wall3")

        
        match type:
            case WallType.WALL0:
                self.animation = self.w0_animation
            case WallType.WALL1:
                self.animation = self.w1_animation
            case WallType.WALL2:
                self.animation = self.w2_animation
            case WallType.WALL3:
                self.animation = self.w3_animation
            case _:
                self.animation = self.w1_animation

    

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
    def __init__(self,pos=(100,100),w_type:WallType = WallType.WALL2):

        self.x = pos[0]
        self.y = pos[1]


        self.l_wall = Wall((self.x+0,self.y+0),False,w_type)
        
        self.width = self.l_wall.get_height()

        self.t_wall = Wall((self.x + 0,self.y + 0),True,w_type)
        self.b_wall = Wall((self.x + 0,self.y +self.width),True,w_type)
        self.r_wall = Wall((self.x + self.width,self.y + 0),False,w_type)


        self.adj_cell_r = None  
        self.adj_cell_l = None  
        self.adj_cell_t = None  
        self.adj_cell_b = None

        self.visited = False

    def get_wall_list(self):
        lst = []
        for i in (self.l_wall,self.t_wall,self.b_wall,self.r_wall):
            if(i):
                lst.append(i)
        return lst

    def render(self,canvas,dt):
        
        for wall in [self.l_wall,self.t_wall,self.b_wall,self.r_wall]:
            if wall:
                wall.render(canvas,dt)
        
        
    def print_adjacent(self):

        print("current : "+str(self),end="")

        print(" right : " + str(self.adj_cell_r),end="")
        print(" ,left : " + str(self.adj_cell_l),end="")
        print(" ,top : " + str(self.adj_cell_t),end="")
        print(" ,bottom : " + str(self.adj_cell_b))

        


    def set_adjacent_cell(
        self,
        left : Cell = None,
        right : Cell = None,
        top : Cell = None,
        bottom : Cell = None
        ):
        if(left):
            self.adj_cell_l = left      
        if(right):
            self.adj_cell_r = right   
        if(top):
            self.adj_cell_t = top       
        if(bottom):
            self.adj_cell_b = bottom   


    def get_adjacent_cells(self):

        req_cells = []
        
        for adj_cell in (
            self.adj_cell_l,
            self.adj_cell_r,
            self.adj_cell_t,
            self.adj_cell_b
        ):
            if(adj_cell):
                req_cells.append(adj_cell)
        
        return req_cells
        


    def delete_wall(self,location: WallLocation):
        
        match location:
            case WallLocation.TOP:
                self.t_wall = None
            case WallLocation.BOTTOM:
                self.b_wall = None
            case WallLocation.LEFT:
                self.l_wall = None
            case WallLocation.RIGHT:
                self.r_wall = None
        


    def get_cell_width(self):
        return self.width

    def get_visited(self)->bool:
        return self.visited

    def set_visited(self):
        self.visited = True

        

class Maze:

    def __init__(self,pos = (100,100),size = (3,3),w_type: WallType = WallType.WALL2):

        self.type = w_type
        if(size[0] < 3 or size[1] < 3):
            self.size = (3,3)
        else:
            self.size = size #(r,c)
             
        self.pos_x = pos[0]
        self.pos_y = pos[1]

        self.cells = []
        
        self.create_grid(pos)
        self.create_maze_pattern()

    
    def create_row(self,pos=(0,0),remove_bottom = False):

        cell_row = []

        start_cell = Cell((pos[0],pos[1]),self.type)
        cell_row.append(start_cell)
        
        width = start_cell.get_cell_width()
        x = start_cell.x 
        y = start_cell.y
        if(remove_bottom):
            start_cell.delete_wall(WallLocation.BOTTOM)

        prev = start_cell #prev pointer
         
        for i in range(0,self.size[1]-1):
            x = x + width

            new_cell = Cell((x,y),self.type)
            new_cell.delete_wall(WallLocation.LEFT)


            if(remove_bottom):
                new_cell.delete_wall(WallLocation.BOTTOM)

            new_cell.set_adjacent_cell(left = prev)
            prev.set_adjacent_cell(right = new_cell)

            cell_row.append(new_cell)
            prev = new_cell
    
        return cell_row

    def link_row(self,top_row,bottom_row):

        for i in range(0,len(top_row)):
            top_row[i].set_adjacent_cell(bottom = bottom_row[i])
            bottom_row[i].set_adjacent_cell(top = top_row[i])



    def create_grid(self,pos = (0,0)):

        x = pos[0]
        y = pos[1]
        
        first_row = self.create_row((x,y),True)
        self.cells.append(first_row)
        height = first_row[0].get_cell_width()

        for i in range(0,self.size[0]-2):
            y = y + height
            cell_row = self.create_row((x,y),True)
            self.link_row(self.cells[-1],cell_row)
            self.cells.append(cell_row)


        y = y + height
        last_row = self.create_row(((x,y)),False)
        self.link_row(self.cells[-1],last_row)
        self.cells.append(last_row)

    
    def debug_pointers(self):

        for rows in self.cells:
            for cell in rows :

                cell.print_adjacent()


    def render(self,canvas,dt):
        
        # self.iterate_maze_pattern_steps()
        for rows in self.cells:
            for cell in rows :

                cell.render(canvas,dt)

    
    
    def get_random_cell(self) -> Cell:

        i = random.randint(0,len(self.cells)-1) #get random row
        j = random.randint(0,len(self.cells[i])-1) # get random cell

        return self.cells[i][j]

    def get_random_adj_cells(self,cells)->Cell:

        cell_list = cells
        while(len(cell_list) > 0):
            cell = cell_list[random.randint(0,len(cell_list)-1)]
            if(not cell.get_visited()):
                return cell
            else:
                cell_list.remove(cell)

        return None


    def create_path(self,new_cell,old_cell):

        if(new_cell.adj_cell_l == old_cell):
            old_cell.delete_wall(WallLocation.RIGHT)

        elif(new_cell.adj_cell_r == old_cell):
            new_cell.delete_wall(WallLocation.RIGHT)

        elif(new_cell.adj_cell_t == old_cell):
            new_cell.delete_wall(WallLocation.TOP)
        else:
            old_cell.delete_wall(WallLocation.TOP)



    def create_maze_pattern(self):

        
        selected_cell = self.get_random_cell() #1) choose random cell
        selected_cell.set_visited() #2) mark as visited
        path = []
        path.append(selected_cell) #3) push to stack

        #while stack is not empty
        while (len(path)>0):

            curr = path[-1] #top of the stack

            adjacent_cells = curr.get_adjacent_cells() #get unvisited neighbours
             

            random_adj_cell = self.get_random_adj_cells(adjacent_cells)
            #if no adjacent cells that are unvisited

            if(random_adj_cell == None):
                    path.pop(-1) #pop stack back track
            else:
                self.create_path(random_adj_cell,curr)
                random_adj_cell.set_visited()
                path.append(random_adj_cell) #push to the stack



        # self.cells[0][0].delete_wall(WallLocation.TOP)
        self.cells[-1][-1].delete_wall(WallLocation.RIGHT)

    def get_wall_list(self):
        lst = []
        for rows in self.cells:
            for cell in rows:
                for i in cell.get_wall_list():
                    lst.append(i)

        return lst


        


