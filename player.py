import random
import pygame
import config
import brain

class Player:
    def __init__(self):
        
        # bird
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.flap = False
        self.alive = True
        self.lifespan = 0

        # artificial intelligence
        self.decision = None
        self.vision = [0.5, 1, 0.5]
        self.fitness = 0
        self.inputs = 3
        self.brain = brain.Brain(self.inputs)
        self.brain.generate_net()

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
            return pygame.Rect.colliderect(self.rect, pipe.top_rect) or pygame.Rect.colliderect(self.rect, pipe.bottom_rect)
        
    def update(self, ground):
        if not (self.ground_collision(ground) or self.pipe_collision()):
            # gravity
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5:
                self.vel = 5
            # lifespan increment
            self.lifespan += 1
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

    # closest pipe
    @staticmethod
    def closest_pipe():
        for pipe in config.pipes:
            if not pipe.passed:
                return pipe

    # artificial intelligence related functions
    def look(self):
        if config.pipes:

            # line to top pipe
            self.vision[0] = max(0, self.rect.center[1] - self.closest_pipe().top_rect.bottom) / 500
            pygame.draw.line(
                config.window,
                self.color,
                self.rect.center,
                (self.rect.center[0], config.pipes[0].top_rect.bottom)
            )

            # line to top pipe
            self.vision[1] = max(0, self.closest_pipe().x - self.rect.center[0]) / 500
            pygame.draw.line(
                config.window,
                self.color,
                self.rect.center,
                (config.pipes[0].x, self.rect.center[1])
            )
            # line to bottom pipe
            self.vision[2] = max(0, self.closest_pipe().bottom_rect.top - self.rect.center[1]) / 500
            pygame.draw.line(
                config.window,
                self.color,
                self.rect.center,
                (self.rect.center[0], config.pipes[0].bottom_rect.top)
            )


    def think(self):
        self.decision = self.brain.feed_forward(self.vision)
        if self.decision > 0.73:
            self.bird_flap()

    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Player
        clone.fitness = self.fitness
        clone.brain = self.brain.clone()
        self.brain.generate_net()
        return clone