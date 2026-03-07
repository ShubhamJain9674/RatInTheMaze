import pygame
from rat import Rat


class Command:
    def __init__(self):
        pass

    def execute(self,object,dt):
        pass

class MoveCommand(Command):
    def __init__(self,dirn = (0,0)):
        super().__init__()
        self.dirn = dirn

    def execute(self,player,dt):
        player.move(dt,self.dirn)


class PlayerController:
    
    def __init__(self):
        
        self.w_command = MoveCommand((0,-1))
        self.a_command = MoveCommand((-1,0))
        self.s_command = MoveCommand((0,1))
        self.d_command = MoveCommand((1,0))






class Game:

    def __init__(self):
        
        pygame.init()
        pygame.display.init()

        self.running = True
        self.screen = pygame.display.set_mode((1280,720))
       
        self.canvas = pygame.Surface((1280,720))
        self.clock = pygame.time.Clock()

        self.player = Rat()
        self.player_controller = PlayerController() 


    
    def handle_input(self):
        
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                running = False
                self.close_game()

        pygame.event.clear()
        
        keys = pygame.key.get_pressed()
        
        if(keys[pygame.K_w]):
            self.player_controller.w_command.execute(self.player,self.dt)
        if(keys[pygame.K_a]):
            self.player_controller.a_command.execute(self.player,self.dt)
        if(keys[pygame.K_s]):
            self.player_controller.s_command.execute(self.player,self.dt)
        if(keys[pygame.K_d]):
            self.player_controller.d_command.execute(self.player,self.dt)
            




    
    def update(self):
        pass
    
    def render(self):
        
        self.canvas.fill("white")
        self.player.render(self.canvas)
        
        
        
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