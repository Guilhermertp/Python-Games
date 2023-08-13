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

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x = 7
ball_speed_y = 7

while True:
    #Handling input
    for event in pygame.event.get(): # check for all the user actions like pressing a key
        if event.type == pygame.QUIT: #cheks if the user have clicked the "x" in the top of the screen
            pygame.quit() #method that closes is the opposite of pygame.init() that starts all the pygame methods (starts the game)
            sys.exit() #makes sure that the program is not still runing in the back

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball. left <=0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    #Visuals
    screen.fill(bg_color)#add the background color by filling the entire display surface
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2,screen_height))#line that separates both sides
#Atention to the order in the loop, because the elements will be drawn on top of each other, by example screen.fill(bg_color) in the end will give an output of only a background
    # try to remove the comment to check it his code runs in the end screen.fill(bg_color)

    # Updating the window
    pygame.display.flip() # thakes everything that comes from the loop and draws in the screen
    clock.tick(60) #limits how fast the loop runs


#I'm at 18 minutes
#https://www.youtube.com/watch?v=Qf3-aDXG8q4&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k