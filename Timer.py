import time
import pygame

def Timer(T,screen):
    Run=True
    start=time.ctime()
    buffer=start
    counter=T
    pygame.font.init()
    font=pygame.font.SysFont('CopperplatEF Cond',48)
    while Run:
        t=time.ctime()
        if(time.ctime()[17:19]!=buffer[17:19]):
            buffer=time.ctime()
            counter-=1
            print(counter)
            
            suraface=font.render(str(counter),False,(0,0,0))
            screen.blit(surface,(640,50))
        if(counter==0):
            Run=False
            return(True)
print(Timer(10))
#Mon Dec  4 09:51:32 2023
"""
issues when while loop is running other code wont execute
fix:-
call the function every frame and make every variable global 

"""
