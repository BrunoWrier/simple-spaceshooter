import pygame


class Enemy:
    
    def __init__(self, x, y) -> None:    
        self.x = x
        self.y = y
        self.color = (255, 255, 255) # (240, 248, 255)

    def update(self):
        self.y += 2

    def draw(self, screen):
        self.rects = [
        pygame.draw.rect(screen, self.color, [self.x, self.y, 10, 10]), # main block
        pygame.draw.rect(screen, self.color, [self.x, self.y+10, 10, 10]),
        pygame.draw.rect(screen, self.color, [self.x-10, self.y+20, 10, 10]),
        pygame.draw.rect(screen, self.color, [self.x+10, self.y+20, 10, 10]),
        pygame.draw.rect(screen, self.color, [self.x-10, self.y-10, 10, 10]),
        pygame.draw.rect(screen, self.color, [self.x+10, self.y-10, 10, 10])
        ]

