import pygame

black = (0, 0, 0)
red = (255, 0, 0)

class Bullet:

    def __init__(self, x, y, radius, color) -> None:
        print('fire!')
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def update(self):
        self.y -= self.vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
    

