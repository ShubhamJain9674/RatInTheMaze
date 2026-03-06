import pygame



class Game:

    def __init__(self):
        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
        self.screen.fill("white")
        self.clock = pygame.time.Clock()




    
    def handle_input(self):
        
        for event in pygame.event.get():

            if(event.type == pygame.QUIT):
                running = False
                self.close_game()

 
    
    def update(self):
        pass
    
    def render(self):
        
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