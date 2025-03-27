import pygame
from random import uniform
class Particle:
    def __init__(self,x,y,typ):
        self.x=x
        self.y=y
        self.dx=uniform(-typ,typ)
        self.dy=uniform(-typ,typ)
        self.lifetime=60

    def update(self):
        self.x+=self.dx
        self.y+=self.dy
        self.lifetime-=1

    def draw(self,window,color):
        position=(int(self.x),int(self.y))
        pygame.draw.circle(window,color,position,2)


class ParticleSystem:
    def __init__(self):
        self.particles=[]

    def add_particle(self,x,y,typ):
        self.particles.append(Particle(x,y,typ))

    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.lifetime<=0:
                self.particles.remove(particle)

    def draw(self,window,color):
        for particle in self.particles:
            particle.draw(window,color)
    def clear(self):
        self.particles=[]
        


