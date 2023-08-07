import pygame
import sys
import random
#represents the moving snake
class snake(object):
    def__init__(self):
    pass
    def get_head_position(self):
        pass
    def turn(self,point):
        pass
    def move(self):
        pass
    def reset(self):
        pass
    def draw(self, surface):
        pass
    def handle_keys(self):
        pass
#represents the stationary food that the snake must eat
class food(object):
    def__init__(self):
    pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass

#function to update the surface when a action is performed
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if(x+y) % 2 ==0: # to make the grid a checkered background
                r= pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface(93, 216, 228), r)
            else: # to draw a even darker square
                rr= pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface(84, 194, 205), rr)
 #***********Global variables**********************
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT/GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH/GRIDSIZE

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

#************MAIN GAME LOOP******************************
def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    #surface that gets updated when an action gets performed
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake()
    food = food()

    score = 0 #initalize the game score to zero
    while (True):
        clock.tick(10) #set 10 frames per second
        # handle event

main()
