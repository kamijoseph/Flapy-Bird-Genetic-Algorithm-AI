import random
import pygame
import config

class Player:
    def __init__(self):
        
        # bird
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.flap = False
        self.alive = True

        # artificial intelligence
        self.decision = None

    # draw method
    def draw(self, window):
        pygame.draw.rect(
            window,
            self.color,
            self.rect
        )
    
    # ground collision
    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)
    
    # sky colllision
    def sky_collision(self):
        return bool(self.rect.y < 30)
    
    # pipe collision
    def pipe_collision(self):
        for pipe in config.pipes:
            return pygame.Rect.colliderect(self.rect, pipe.top_rect) or \
                pygame.Rect.colliderect(self.rect, pipe.bottom_rect)
        
    def update(self, ground):
        if not (self.ground_collision(ground) or self.pipe_collision()):
            # gravity
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5:
                self.vel = 5
            else:
                self.alive = False
                self.flap = False
                self.vel = 0
    
    # bird flapping and flight
    def bird_flap(self):
        if not self.flap and not self.sky_collision():
            self.flap = True
            self.vel = -5
        if self.vel >= 3:
            self.flap = False

    # artificial intelligence related functions
    def think(self):
        self.decision = random.uniform(0, 1)
        if self.decision > 0.73:
            self.bird_flap()