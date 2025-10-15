
import pygame
from sys import exit
import config
import components

pygame.init()
clock = pygame.time.Clock()

FPS = 60

def generate_pipes():
    config.pipes.append(
        components.Pipes(config.win_width)
    )

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10
    while True:
        quit_game()
        config.window.fill((0, 0, 0))

        # ground
        config.ground.draw(config.window)

        #pipes
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for pipe in config.pipes:
            pipe.draw(config.window)
            pipe.update()
            if pipe.off_screen:
                config.pipes.remove(pipe)

        clock.tick(FPS)
        pygame.display.flip()
        
main()