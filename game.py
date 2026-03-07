import pygame
from rat import Rat
from maze import Wall,Cell,WallType,Maze



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
        self.maze = Maze((100,100),5,WallType.WALL3)

        
    
    def handle_input(self):
        
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                running = False
                self.close_game()

        pygame.event.clear()
        
        keys = pygame.key.get_pressed()

        player_moving = False
    
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
        pass
    
    def render(self):
        
        self.canvas.fill("black")
        self.player.render(self.canvas,self.dt)
    
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