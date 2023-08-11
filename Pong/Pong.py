import pygame,sys

#General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong') #give the window a title


#the origin of the window is tip left by pygame convention, when drawing he should have that in account
#Game rectangle, this three rectagles are empty to draw them will be in the loop using pygame.draw(surface, color, rect)
ball = pygame.Rect(screen_width/2- 15,screen_height/2 -15,30,30)#the subraction and division is to center the ball, 15 is half of the ball lenght
player = pygame.Rect(screen_width - 20,screen_height/2 -70 ,10,140) #70 is half of the lenght 140
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

while True:
    #Handling input
    for event in pygame.event.get(): # check for all the user actions like pressing a key
        if event.type == pygame.QUIT: #cheks if the user have clicked the "x" in the top of the screen
            pygame.quit() #method that closes is the opposite of pygame.init() that starts all the pygame methods (starts the game)
            sys.exit() #makes sure that the program is not still runing in the back

    # Updating the window
    pygame.display.flip() # thakes everything that comes from the loop and draws in the screen
    clock.tick(60) #limits how fast the loop runs


#I'm at 10.32 minutes
#https://www.youtube.com/watch?v=Qf3-aDXG8q4&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k