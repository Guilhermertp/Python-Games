import pygame
import sys
import random
#represents the moving snake


class Snake():
    def __init__(self):
        self.length = 1 #the snake length starts at 1
        self.positions = [((screen_width/2),(screen_height/2))] #sets the snake at the center position of the screen
        self.direction = random.choice([up, down, left, right]) #the direction the snake is headed
        self.color = (17, 24, 47) #the snake color

        self.score = 0

    def get_head_position(self):
        return self.positions[0] #returns the position of the head of the snake that is stored in the positions list property

    #if the snake is only one block it can move in any direction but if have more than one block it can only move in 3 directions(can't reverse direction immediately)
    def turn(self,point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    #calculates a new position based on the current position and the direction of the snake
    def move(self):

        cur = self.get_head_position() #gets the position of the head of the snake
        x, y = self.direction # gets the current position of the snake by accessing the snake's direction property
        new = (((cur[0] + (x*gridsize)) % screen_width),(cur[1] + (y*gridsize)) % screen_height ) #using the grid size and the screen width calculates the new location of the head of the snake
        if len(self.positions) > 2 and new in self.positions[2:]: #if the length of the snake is bigger then 2 and the new location of the head of the snake overlaps with any other part of the snake, this mean the game is ended
            self.reset() #if the game is ended the snake is reseted
        else:
    #if the game is not ended this code will add the new head position to the beginning of the positons list and pop the last element

            self.positions.insert(0, new)
            if len(self.positions)> self.length:

                self.positions.pop()

    #when the game ends this resets the snake to the default values(same values defined in the initial code for the snake class)
    def reset(self):
        self.lenght = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]  # sets the snake at the center position of the screen
        self.direction = random.choice([up, down, left, right])  # the direction the snake is headed

        self.score = 0

    def draw(self, surface): #draw method to show the snake on the screen surface
        #draw a block for each xy position of the snake using some functions built in pygame
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]),(gridsize, gridsize) )
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self): #method that handles when a player presses a key

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() #exit the program using the sys method to make sure it shutsdown everything
            #if the program doesn't exit then check for the press of the key up,down,left, right and turn the snake ansed ont he key pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)


#represents the stationary food that the snake must eat
class Food():
    def __init__(self):
        self.position = (0, 0)  # xy position
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self): #this method will return a random position on the grid for the food
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)



    def draw(self, surface): #show the snake on the screen surface
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
#****************ABOVE ist the code i copy pasted**********************


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if(x+y)% 2 ==0: # to make the grid a checkered background
                r= pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93, 216, 228), r)
            else: # to draw a even darker square
                rr= pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(84, 194, 205), rr)

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake() #to avoid the error "local variable 'snake' referenced before assignment" the class is in capital letters, for test you can change the class name to snake and here to get the error
    food = Food()

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        clock.tick(10) #set 10 frames per second
        snake.handle_keys()
        drawGrid(surface)
        snake.move() #move the snake according to the key press
        if snake.get_head_position() == food.position: #check if the head is the same as the food position if True the snake have eaten the food and add 1
            snake.length += 1
            snake.score += 1#increase the game score by one
            food.randomize_position() #randomize the position of the next food block
        snake.draw(surface)
        food.draw(surface)
        # update and refresht he screen and the surface
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0)) #Create a text box to display "Score" in the upper hand left corner of the game
        screen.blit(text, (5,10))
        pygame.display.update()

main()