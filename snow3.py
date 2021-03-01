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
jingle = pygame.mixer.music.load("snow.mp3")
class Particle:
    def __init__(self):
        "Setting up screen, clock and loading images"

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.frame_rate = pygame.time.Clock().tick
        self.snow = pygame.image.load("snow6.png").convert()
        self.cloud = pygame.image.load("cloud.png")
        self.window2 = pygame.image.load("snow5.png")
        self.list_of_particles = []

    def update(self):
        "How to quit the window"
        self.frame_rate(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        self.images_display()

    def images_display(self):
        "Make snow fall down - blitting images and calling the flake generator"

        self.screen.blit(self.snow, (0,0))
        self.snow_flakes_generator()
        self.screen.blit(self.cloud, (-110,-100))
        self.screen.blit(self.cloud, (-50, 250))
        self.screen.blit(self.cloud, (450, 250))
        self.screen.blit(self.window2, (0, 0))
        pygame.display.flip()

    def mainloop(self):
        "A call to the self.update method to run stuffs"
        pygame.mixer.music.play()
        self.run = True
        while self.run:
            run = self.update()
        pygame.quit()
        exit()

    # the surface with the snow as a background


    def generate_one_particle(self):
        starting_pos = [random_pos(), 50]
        # direction of x and next y pos incremented of 0.01
        move_pos = [random.randint(0, 20) / 10 - 1, 2]
        radius = random.randint(4, 6)
        return [starting_pos, move_pos, radius]



    def snow_flakes_generator(self):
        "circles move from random start position at the top until bottom and the disappear"
        
        self.list_of_particles.append(self.generate_one_particle())

        # Every particle  moves... if list_of_particles[2] (the radius) is >= than 0 it is removed
        for particle in self.list_of_particles[:]:
            
            # parameters for new position (aka speed) and shrinking
            direction = particle[1][0]      # random direction fixed
            velocity = particle[1][1]  # get the next position on the y axes
            gravity = 0.01            # how fast it falls
            melting = 0.005         # how fast it shrinks

            # the starting point changes going right or left
            particle[0][0] += direction # increase the x position of an angle (to the right or left)
            particle[0][1] +=  velocity # the y movement going down speed fixed 2
                                            # but it is increased of 0.01 down here, so it goes down at the same speed
            particle[2] -= melting # the snowflake shriks
            particle[1][1] += gravity # * random.randint(-3, 6) # increase down speed a bit
            if particle[2] <= 0: # when the radius is 0 it is removed, so we do not see it anymore and it's not in the memory
                self.list_of_particles.remove(particle)

        # draws a circle on the screen white, at x y corrds and with a ray of particle[2]
        for particle in self.list_of_particles:
            pos = particle[0][0]
            speed = particle[0][1]
            radius = particle[2]
            # circle: surface, color, pos, radius
            pygame.draw.circle(
            	self.screen,
            	(255, 244, 255), # color
            	(
            		round(pos), # Pos x, y
            		round(speed)), # direction / speed
            		round(radius)) # radius
def random_pos():
	" to make a flame like list_of_particles [150, 20] # flame, so that all circles with start at the same point"
	return random.randint(30, 8000)
	# return 150



fx = Particle()
fx.mainloop()
