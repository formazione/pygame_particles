# pygame.math module
# https://www.pygame.org/docs/ref/math.html
#
# Pygame swap text with another text
# https://stackoverflow.com/questions/60944070/pygame-swap-text-with-another-text/60953697#60953697
#
# GitHub - PyGameExamplesAndAnswers - Draw 2D - snow_flakes_list
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_2D.md

import pygame
import random
import sys


pygame.mixer.init()
pygame.mixer.music.load("snow.mp3")
FPS = 30


class Particle:
    "Makes particles to appear on the screen"

    def __init__(self):
        "Setting up screen, clock and loading images"

        pygame.init()
        
        # the two main surfaces
        self.screen = pygame.display.set_mode((1111, 834), pygame.NOFRAME)
        self.new_surface = pygame.Surface((1111, 834))

        self.frame_rate = pygame.time.Clock().tick
        # loading images for the script
        self.bg = pygame.image.load("redcat.png").convert_alpha()
        # self.cloud = pygame.image.load("cloud.png").convert_alpha()
        self.fg = pygame.image.load("cat3.png").convert_alpha()
        self.snow_flakes_list = []
        self.snow_flakes_list2 = []
        self.rain_drops_list = []
        self.resize = 0
        self.snow_type = 1

    def update(self):
        "How to quit the window"
        self.frame_rate(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.run = False
            if event.type == pygame.VIDEORESIZE:
                self.resize = 1
                self.w, self.h = event.w, event.h
        # ====================================== background
        self.new_surface.blit(self.bg, (0, 0))
        self.snow_flakes_generator() # ============= particles
        # self.new_surface.blit(self.fg, (0, 0))
        # ====================================== foreground
        if self.resize:
            self.screen.blit(pygame.transform.scale(self.new_surface.convert_alpha(), (self.w, self.h)), (0, 0))
        else:
            self.screen.blit(self.new_surface.convert_alpha(), (0, 0))
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

    def generate_one_particle(self, dim, start=30, end=1111):
        direction = [random_pos(start, end), random.randint(1, 5)]
        # direction of x and next y pos incremented of 0.01
        # change the 2 to change the way the snow flake falls
        angle_vel = [random.randint(0, 20) / 10 - 1, 2]
        radius = random.randint(4, 6)
        if dim == 4:
            angle_vel = [0, 7]
            radius = 1
        return [direction, angle_vel, radius]

    def snow_flakes_generator(self):
        "circles move from random start position at the top until bottom and the disappear"
        self.snow()
        # self.snow2()
        # self.rain()

    def snow(self):
        self.snow_flakes_list.append(self.generate_one_particle(6, 0, 1111))
        self.color = (255, 255, 255)
        self.gravity = 0.01
        self.snow_type = 1
        self.falling_elements(self.snow_flakes_list)
        

    def snow2(self):
        self.snow_flakes_list2.append(self.generate_one_particle(6, 500, 510))
        self.color = (0, 222, 222)
        self.gravity = 0.005
        self.snow_type = 2
        self.falling_elements(self.snow_flakes_list2)

    def rain(self):
        for drop in range(20): # 5 drops for frame
            self.rain_drops_list.append(self.generate_one_particle(4))
        self.color = (200, 200, 200)
        self.gravity = 0.05
        self.falling_elements(self.rain_drops_list)

    def falling_elements(self, elements_list):

        # Every particle  moves... if snow_flakes_list[2] (the radius) is >= than 0 it is removed
        for particle in elements_list:
            
            # parameters for new position (aka speed) and shrinking
            direction = particle[1][0]      # random direction fixed
            velocity = particle[1][1]  # how fast the flake falls
            gravity = self.gravity           # how fast it falls
            melting = 0.005         # how fast it shrinks

            # DIRECTION
            particle[0][0] += direction # increase the x position of an angle (to the right or left)
            particle[0][1] +=  velocity # the y movement going down speed fixed 2
                                            # but it is increased of 0.01 down here, so it goes down at the same speed
            particle[2] -= melting # the snowflake shriks
            particle[1][1] += gravity # * random.randint(-3, 6) # increase down speed a bit
            if particle[0][1] > 834: # when the radius is 0 it is removed, so we do not see it anymore and it's not in the memory
                elements_list.remove(particle)

        # draws a circle on the screen white, at x y corrds and with a ray of particle[2]
        for particle in elements_list:
            pos = particle[0][0]
            speed = particle[0][1]
            radius = particle[2]
            # circle: surface, color, pos, radius
            # if self.snow_type == 2:
            #     self.new_surface.set_alpha(122)
            # else:
            #     self.new_surface.set_alpha(255)

            pygame.draw.circle(
            	self.new_surface,
            	(self.color), # color
            	(
            		round(pos), # Pos x, y
            		round(speed)), # direction / speed
            		round(radius)) # radius
def random_pos(start=30, end=60):
	" to make a flame like snow_flakes_list [150, 20] # flame, so that all circles with start at the same point"
	return random.randint(start, end)
	# return 150



fx = Particle()
fx.mainloop() # => self.update => snow_flake_generator =>
