import pygame
from bulletclass import Bullet

class Player:
    def __init__(self, x, y, speed, color) -> None:
        self.x1 = x
        self.y1 = y
        self.color = color
        self.speed = speed

    def controls(self):
        x1_change = 0
        y1_change = 0

        # movementation
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            x1_change = -self.speed
            y1_change = 0
        elif keys[pygame.K_RIGHT]:
            x1_change = self.speed
            y1_change = 0
        elif keys[pygame.K_UP]:
            y1_change = -self.speed
            x1_change = 0
        elif keys[pygame.K_DOWN]:
            y1_change = self.speed
            x1_change = 0
        else:
            x1_change = 0
            y1_change = 0

        window_rect = pygame.Rect(0, 0, 800, 600)
        if not window_rect.collidepoint((self.x1 + x1_change, self.y1 + y1_change)):
            return;

        self.x1 += x1_change
        self.y1 += y1_change
    

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x1, self.y1, 10, 10]) # main block
        pygame.draw.rect(screen, self.color, [self.x1, self.y1+10, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1-10, self.y1+10, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1+10, self.y1+10, 10, 10])

        pygame.draw.rect(screen, self.color, [self.x1, self.y1+20, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1-10, self.y1+20, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1+10, self.y1+20, 10, 10])

        pygame.draw.rect(screen, self.color, [self.x1-20, self.y1+20, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1+20, self.y1+20, 10, 10])

        pygame.draw.rect(screen, self.color, [self.x1, self.y1+30, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1-10, self.y1+30, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x1+10, self.y1+30, 10, 10])


