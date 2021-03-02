# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Pygame swap text with another text
# https://stackoverflow.com/questions/60944070/pygame-swap-text-with-another-text/60953697#60953697
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - list_of_particles
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame
import random
import sys


pygame.mixer.init()
pygame.mixer.music.load("snow.mp3")
FPS = 60


class Particle:
    "Makes particles to appear on the screen"

    def __init__(self):
        "Setting up screen, clock and loading images"

        pygame.init()
        
        # the two main surfaces
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.new_surface = pygame.Surface((800, 600))

        self.frame_rate = pygame.time.Clock().tick
        # loading images for the script
        self.bg = pygame.image.load("snow6.png").convert()
        self.cloud = pygame.image.load("cloud.png")
        self.fg = pygame.image.load("snow7.png")
        self.list_of_particles = []
        self.resize = 0

    def update(self):
        "How to quit the window"
        self.frame_rate(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.VIDEORESIZE:
                self.resize = 1
                self.w, self.h = event.w, event.h
        self.images_display()

    def images_display(self):
        "Make snow fall down - blitting images and calling the flake generator"
        self.new_surface.blit(self.bg, (0, 80))
        self.snow_flakes_generator()
        # self.new_surface.blit(self.cloud, (-110,-100))
        self.new_surface.blit(self.cloud, (-50, 290))
        self.new_surface.blit(self.cloud, (450, 290))
        self.new_surface.blit(self.fg, (0, 0))
        if self.resize:
            self.screen.blit(pygame.transform.scale(self.new_surface, (self.w, self.h)), (0, 0))
        else:
            self.screen.blit(self.new_surface, (0, 0))
        pygame.display.flip()

    def mainloop(self):
        "A call to the self.update method to run stuffs"
        
        # Start the mp3 loaded at the beginning
        pygame.mixer.music.play()
        self.run = True
        while self.run:
            run = self.update()
        pygame.quit()
        exit()

    # the surface with the snow as a background

    def generate_one_particle(self):
        direction = [random_pos(), 50]
        # direction of x and next y pos incremented of 0.01
        # change the 2 to change the way the snow flake falls
        velocity = [random.randint(0, 20) / 10 - 1, random.randint(2, 10)]
        radius = random.randint(4, 6)
        return [direction, velocity, radius]

    def snow_flakes_generator(self):
        "circles move from random start position at the top until bottom and the disappear"
        
        self.list_of_particles.append(self.generate_one_particle())

        # Every particle  moves... if list_of_particles[2] (the radius) is >= than 0 it is removed
        for particle in self.list_of_particles[:]:
            
            # parameters for new position (aka speed) and shrinking
            direction = particle[1][0]      # random direction fixed
            velocity = particle[1][1]  # how fast the flake falls
            gravity = 0.01            # how fast it falls
            melting = 0.005         # how fast it shrinks

            # DIRECTION
            particle[0][0] += direction # increase the x position of an angle (to the right or left)
            particle[0][1] +=  velocity # the y movement going down speed fixed 2
                                            # but it is increased of 0.01 down here, so it goes down at the same speed
            particle[2] -= melting # the snowflake shriks
            particle[1][1] += gravity # * random.randint(-3, 6) # increase down speed a bit
            if particle[0][1] > 330: # when the radius is 0 it is removed, so we do not see it anymore and it's not in the memory
                self.list_of_particles.remove(particle)

        # draws a circle on the screen white, at x y corrds and with a ray of particle[2]
        for particle in self.list_of_particles:
            pos = particle[0][0]
            speed = particle[0][1]
            radius = particle[2]
            # circle: surface, color, pos, radius
            pygame.draw.circle(
            	self.new_surface,
            	(255, 255, 255), # color
            	(
            		round(pos), # Pos x, y
            		round(speed)), # direction / speed
            		round(radius)) # radius
def random_pos():
	" to make a flame like list_of_particles [150, 20] # flame, so that all circles with start at the same point"
	return random.randint(30, 800)
	# return 150



fx = Particle()
fx.mainloop()
