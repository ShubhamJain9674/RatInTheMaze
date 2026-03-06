import pygame
from rat import Rat


class Game:

    def __init__(self):
        
        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode((1280,720))
        self.screen.fill("white")
        self.canvas = pygame.Surface((1280,720))
        self.clock = pygame.time.Clock()

        self.player = Rat()


    
    def handle_input(self):
        
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                running = False
                self.close_game()

 
    
    def update(self):
        pass
    
    def render(self):
        
        self.player.render(self.canvas)
        
        
        
        self.screen.blit(self.canvas,(0,0))
        pygame.display.flip()


    def loop(self):
        
        while(self.running):

            self.handle_input()
            self.update()
            self.render()

            self.clock.tick(60)

    def close_game(self):
        pygame.quit()
        exit(0)