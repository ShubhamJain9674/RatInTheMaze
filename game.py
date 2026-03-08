import pygame
from rat import Rat
from maze import Wall,Cell,WallType,Maze



class CollisionManager:
    def __init__(self,player,walls:pygame.sprite.Sprite=[],objects:pygame.sprite.Sprite=[]):
    
        self.player = player
        self.walls = walls
        
        self.wall_collision_list=[False for i in self.walls]

    def check_wall_collisions(self)->bool:

        rects = []
        collision = False
        for i in range(0,len(self.walls)):
            if(self.player.rect.colliderect(self.walls[i].rect)):
                self.wall_collision_list[i] = True
                rects.append(self.walls[i].rect)
                collision = True
            else:
                self.wall_collision_list[i] = False

        self.player.collide_walls(rects)
        
        return collision







class Command:
    def __init__(self):
        pass

    def execute(self,object,dt):
        pass

class MoveCommand(Command):

    def __init__(self,character=None,dirn = (0,0)):
        super().__init__()
        self.dirn = dirn
        self.character = character

    def execute(self,dt,player=None):
        if(player):
            player.move(dt,self.dirn)
        elif(self.character):
            self.character.move(dt,self.dirn)
        else:
            print("No character to move")


class PlayerController:
    
    def __init__(self,player):
        self.player = player
        
        self.w_command = MoveCommand(player,(0,-1))
        self.a_command = MoveCommand(player,(-1,0))
        self.s_command = MoveCommand(player,(0,1))
        self.d_command = MoveCommand(player,(1,0))

    def stop_player(self):
        self.player.stop()


class Game:

    def __init__(self):
        
        pygame.init()
        pygame.display.init()

        self.running = True
        self.screen = pygame.display.set_mode((1280,720))
       
        self.canvas = pygame.Surface((1280,720))
        self.clock = pygame.time.Clock()

        self.player = Rat()
        self.player_controller = PlayerController(self.player) 
        self.dt = 0


        #debug
        self.maze = Maze((100,100),(8,15),WallType.WALL2)
        self.wall_list = self.maze.get_wall_list()
       
        
        self.collision_manager = CollisionManager(self.player,self.wall_list)
    
    def handle_input(self):
        
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                running = False
                self.close_game()

        pygame.event.clear()
        
        keys = pygame.key.get_pressed()

        player_moving = False

        if(not self.collision_manager.check_wall_collisions()):
            self.player.reset_movement()
    
        if(keys[pygame.K_w]):
            self.player_controller.w_command.execute(self.dt)
            player_moving = True
        if(keys[pygame.K_a]):
            self.player_controller.a_command.execute(self.dt)
            player_moving = True
        if(keys[pygame.K_s]):
            self.player_controller.s_command.execute(self.dt)
            player_moving = True
        if(keys[pygame.K_d]):
            self.player_controller.d_command.execute(self.dt)
            player_moving = True

        if(not player_moving):
            self.player_controller.stop_player()
        
            




    
    def update(self):
        self.player.update(self.dt)
        

    
    def render(self):
        
        self.canvas.fill("black")
        self.player.render(self.canvas)
    
        self.maze.render(self.canvas,self.dt)    

        self.screen.blit(self.canvas,(0,0))

        pygame.display.flip()


    def loop(self):
        
        while(self.running):

            self.handle_input()
            self.update()
            self.render()

            self.dt = self.clock.tick(60) / 1000
            

    def close_game(self):
        pygame.quit()
        exit(0)